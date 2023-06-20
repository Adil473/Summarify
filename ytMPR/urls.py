from django.contrib import admin
from django.urls import path
from ytMPR import views

urlpatterns = [
    path('', views.index, name="ytMPR"),
    path('about', views.about, name="about"),
    path('ytsummarize', views.ytsummarize, name="ytsummarize"),
    path('article_summary' , views.article_summary , name="article-summary"),
    path('video', views.video , name="video"),
]
