from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Blog(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')
	body = models.TextField()
	like_user_set=models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_user_set', through='Like')
	

	@property
	def like_count(self):
		return self.like_user_set.count()
	

	def __str__(self):
		return self.title

class Like(models.Model):
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	blog=models.ForeignKey(Blog, on_delete=models.CASCADE)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True)

	class Meta:
		unique_together=(('user', 'blog'))