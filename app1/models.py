from django.db import models

# Create your models here.
class Topic(models.Model):
  topic_name=models.CharField(max_length=100,primary_key=True)
  num_of_players=models.PositiveIntegerField(default=0)

  def __str__(self):
    #only srting data can be returned
    return self.topic_name

