from django.db import models
from django.utils import timezone

class poet(models.Model):
    poet = models.CharField(max_length=200 ,null = True)
    def __str__(self):
        return self.poet
    

class poem(models.Model):
    poet = models.ForeignKey(poet, related_name="poet_poet",on_delete=models.CASCADE,null = True ,blank=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        
        return self.title
        
    def __str__(self) -> str:
        
        return self.text
    
