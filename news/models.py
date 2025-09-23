from django.db import models

# Create your models here.
'''
class Headline(models.Model):
  title = models.CharField(max_length=200)
  image = models.URLField(null=True, blank=True)
  url = models.TextField()
  def __str__(self):
    return self.title
''' 

from django.db import models

class Headline(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    url = models.URLField()
    #image = models.URLField()
    image = models.URLField(default='https://i.ibb.co/6BFNgXx/College-SREC.jpg')  # Example def __str__(self):return self.title

    def __str__(self):
        return self.title
