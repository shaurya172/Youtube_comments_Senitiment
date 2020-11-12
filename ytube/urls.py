from django.urls import path, include
from . import views 
urlpatterns = [
    path('', views.input_sentiment, name = 'cxform'),
    path('details/', views.sentiment_details, name = 'details'),
    
]
