from django.db import models

# Create your models here.

class sentiment(models.Model):

    id = models.AutoField(primary_key=True)
    input_sentiment = models.CharField(max_length=500)
    title = models.CharField(max_length=100, default=1)
    #files = models.FileField(null = True)
    timestamp = models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.title

class output_sent(models.Model):

    id = models.AutoField(primary_key=True)
    sent_id = models.ForeignKey(sentiment, on_delete=models.CASCADE)
    op_text = models.CharField(max_length=100)


    def __str__(self):
        return self.op_text