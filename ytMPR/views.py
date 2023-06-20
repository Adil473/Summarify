from multiprocessing import context
from unittest.util import _MAX_LENGTH
from django.shortcuts import render, HttpResponse
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from IPython.display import YouTubeVideo, HTML, IFrame
from .models import Display_Video

# Create your views here.
def index(request):
    #return HttpResponse("This is ytMPR")
    context = {
        'variable1' : "This is sent",
        'variable2' : "This is test"
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("This is about")

def ytsummarize(request):
    youtube_video = request.GET['video_url']
    video_id = youtube_video.split("=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    YouTubeVideo(video_id)
    result = ""
    for i in transcript:
        result += " " + i["text"]
    
    summarizer = pipeline("summarization")
    
    num_iters = int(len( result) / 1000 )
    summarized_text = []
    for i in range(0,num_iters + 1):
        start = 0
        start = i*1000
        end = (i+1) * 1000
        out = summarizer(result[start:end], max_length = 50, min_length = 10, do_sample= False)
        out = out[0]
        out = out["summary_text"]
        summarized_text.append(out)
    text_summary = ""
    x = len(summarized_text)
    for i in range(x):
        text_summary += ". " + summarized_text[i]
    return render(request , 'ytsummarize.html', {'vid_url' : text_summary , 'transcript_length' : len(result), 'vid_url_display' : youtube_video} )


def article_summary(request):
    article = request.GET['article']
    summarizer = pipeline("summarization")
    num_iters = int(len( article) / 500 )
    summarized_text = []
    for i in range(0,num_iters + 1):
        start = 0
        start = i*500
        end = (i+1) * 500
        out = summarizer(article[start:end], max_length = 50, min_length = 10, do_sample= False)
        out = out[0]
        out = out["summary_text"]
        summarized_text.append(out)
    #for i in article:
    #   art += article[i]
    text_summary = ""
    x = len(summarized_text)
    for i in range(x):
        text_summary += ". " + summarized_text[i]
    return render(request, 'article_summary.html' , {'article_sum' : text_summary})
    


def video(request):
    obj = Display_Video.objects.all()
    return render(request, 'video.html', {'obj' : obj})