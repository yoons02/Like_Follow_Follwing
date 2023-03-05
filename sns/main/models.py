from django.db import models
from users.models import User

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField()
    body = models.TextField()
    like = models.ManyToManyField(User, related_name='likes',blank=True)
    like_count = models.PositiveIntegerField(default=0) #0또는 양수만 받는 필드

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]
    
