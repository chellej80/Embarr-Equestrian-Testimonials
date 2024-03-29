"""Models Imports"""
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Set service post status


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class UserProfile(models.Model):
    """
    Model for the update of the user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    """
    Model for the creation & management of the Service posts
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='test_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        """order by created date/time"""
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Review(models.Model):
    """
    Class review model that creates and saves the review in the DB
    """

    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='reviews')
    name = models.CharField(max_length=80)
    location = models.CharField(max_length=80, default='e.g Dublin')
    email = models.EmailField()
    body = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default='5 stars')
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    class Meta:
        """order by created date/time"""
        ordering = ['created_on']

    def __str__(self):
        return 'Review {} by {}'.format(self.body, self.name)

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('post_detail', args=[self.post.slug])
