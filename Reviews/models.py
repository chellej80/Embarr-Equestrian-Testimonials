from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver #add this
from django.db.models.signals import post_save #add this

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='test_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    

class Comment(models.Model):

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    location = models.CharField(max_length=80, default='e.g Dublin')
    email = models.EmailField()
    body = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default='5')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Profile(models.Model):   #add this class and the following fields
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	products = models.ManyToManyField(Product)
