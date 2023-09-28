from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)



class Hadith(models.Model):
    CATEGORY = (
        ('Hadith', 'Hadith'),
        ('Quran', 'Quran'),
        ('Others', 'Others')
    )
    tag = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=200, null=True)
    detail = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    category = models.CharField(max_length=100, null=True, blank=True, choices=CATEGORY)

    def __str__(self):
        return self.tag

    def preview(self):
        return self.detail[:500] + "(show more...)"
    

