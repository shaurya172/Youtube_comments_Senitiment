from django.shortcuts import render, redirect
from . forms import SentimentForm
from django.contrib import messages
import random
from urllib.parse import urlparse, parse_qs
import sqlite3
import datetime
import requests
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging
from datetime import datetime
from .models import sentiment
#from .models import sentiment,output_sent

logger = logging.getLogger("info")
logger.info('something')
# Create your views here.
def get_sentiment(url): 
    url_data = urlparse(url)
    query = parse_qs(url_data.query)
    video_id = query["v"][0]
    print(video_id)
    analyzer = SentimentIntensityAnalyzer()
    corpus = []
    count_neg = 0
    count_pos = 0
    count_neu = 0
    overall_emotion = 0
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?key=AIzaSyBtUS0Cajv3BHDG3Us10_KyQ-XrXL0KIo8&textFormat=plainText&part=snippet&videoId={video_id}&maxResults=100"
    json_url = requests.get(url)
    
    data = json.loads(json_url.text)
    print(data)
   
    #nextPageToken = data['nextPageToken']
    try:
        for i in range(0,99):
            comment = data['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'].replace('\n','')
            corpus.append(comment)
            print(comment)
            vs = analyzer.polarity_scores(comment)
            emotion = vs['compound']
            #likes = data['items'][i]['snippet']['topLevelComment']['snippet']['likeCount']
            #time = data['items'][i]['snippet']['topLevelComment']['snippet']['publishedAt']
            if emotion < 0:
                count_neg += 1

            elif emotion > 0:
                count_pos += 1

            else:
                count_neu += 1

            overall_emotion = overall_emotion + emotion
    
    except IndexError as e:
            
            print(e)           
                

    try:
        nextPageToken = data['nextPageToken']
        while nextPageToken != '':
            url = f"https://www.googleapis.com/youtube/v3/commentThreads?key=AIzaSyBtUS0Cajv3BHDG3Us10_KyQ-XrXL0KIo8&textFormat=plainText&part=snippet&videoId={video_id}&maxResults=100&pageToken={nextPageToken}"
            json_url = requests.get(url)
            data = json.loads(json_url.text)
            nextPageToken = data['nextPageToken']

            
            try:
                for i in range(0,99):
                    comment = data['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal'].replace('\n','')
                    corpus.append(comment)
                    print(comment)
                    vs = analyzer.polarity_scores(comment)
                    emotion = vs['compound']
                    if emotion < 0:
                        count_neg += 1
                    
                    elif emotion > 0:
                        count_pos += 1

                    else:
                        count_neu += 1

                    overall_emotion = overall_emotion + emotion
            except IndexError as e:
                print(e)
                        
            
                
                
    except KeyError as e:
        print(e)
        
    return count_neg, count_pos, count_neu, overall_emotion

def input_sentiment(request):
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form .is_valid():
            input_url = form.cleaned_data['input_sentiment']
            title = form.cleaned_data['title']
            hosts = form.cleaned_data['hosts']
            ts = datetime.now()
            if hosts == 'single_host':
                print('single host selected')
            else:
                print('multiple hosts selected')

            negative_comments, postive_comments, neutral_comments, overall_emotion = get_sentiment(input_url)

            if int(negative_comments) > int(postive_comments):
                senti = "Negative"

            else:
                senti = "Positive"
            # print(hosts)
            #print(input_sentiment)
            
            #print(sentiment)
            f = open("file123.html","w")
            print('file opened')
            # t = sentiment(input_sentiment = title)
            # st = t.objects.get(input_sentiment = title)
            # o = output_sent(input_sentiment = st,op_text= senti)
            # t.save()
            # o.save()
            t = sentiment(input_sentiment = input_url, title = title, timestamp = ts)
            t.save()
            string = f'Sentiment Analysis of the video:\n Negative Comments: {negative_comments}\n Positive Comments: {postive_comments}\n Neutral_comments: {neutral_comments}\n Overall Emotion: {overall_emotion}'
            f.write(string)
            f.close()
            messages.success(request, f'Sentiment Analysis of the video:\n Negative Comments: {negative_comments}\n Positive Comments: {postive_comments}\n Neutral_comments: {neutral_comments}\n Overall Emotion: {overall_emotion}')

    form = SentimentForm()

    return render(request, 'myform/cxform.html',{'form':form})

def sentiment_details(request):
    query_results = sentiment.objects.all()
    return render(request, "myform/details.html", context= {'query_results': query_results})

# def output_sentiment(request):
#     if request.method == 'POST':
#         form = SentimentForm(request.POST)
#         if form .is_valid():
#             input_url = form.cleaned_data['input_sentiment']
#             hosts = form.cleaned_data['hosts']
#             if hosts == 'single_host':
#                 print('single host selected')
#             else:
#                 print('multiple hosts selected')
#             # print(hosts)
#             #print(input_sentiment)
#             negative_comments, postive_comments, neutral_comments, overall_emotion = get_sentiment(input_url)

#             if int(negative_comments) > int(postive_comments):
#                 op_text = "Negative"

#             else:
#                 op_text = "Positive"


#     return render(request, {'op_text': op_text})
            

