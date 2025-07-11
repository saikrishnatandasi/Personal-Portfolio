from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    github_link = models.URLField(blank=True)
    live_demo = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    category = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


    
