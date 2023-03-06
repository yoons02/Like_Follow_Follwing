from django.db import models
from django.contrib.auth.models import User
# 리시버 Import

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # followings = M2M_field("자신", related_name="followers", symmetrical=False)

# 팔로잉 리시버