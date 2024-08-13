from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author= models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)
    comment_num=models.IntegerField(default=0)
    upvote=models.ManyToManyField(User, related_name='upvoted_posts',blank=True)
    downvote=models.ManyToManyField(User, related_name='downvoted_posts',blank=True)
    views=models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    def add_downvote(self, user):
        if not self.downvote.filter(id=user.id).exists():
            self.downvote.add(user)
            return True
        return False
    
    def add_upvote(self, user):
        if not self.upvote.filter(id=user.id).exists():
            self.upvote.add(user)
            return True
        return False
    
    def total_votes(self):
        return self.upvote.count()-self.downvote.count()

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    content=models.TextField()
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]
    
    def save(self, *args, **kwargs):
        self.post.comment_num+=1
        self.post.save()
        super().save(*args, **kwargs)