from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # topic can have multiple room | a room can have one topic
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)  # null for db | blank for Textview
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)  # whenever update
    created = models.DateTimeField(auto_now_add=True)  # just for first created

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # one to many coz of user can have many msgs
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # when room is deleted, all children will be deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)  # whenever update
    created = models.DateTimeField(auto_now_add=True)  # just for first created

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]








