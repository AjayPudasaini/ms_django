from rest_framework import serializers
from posts.models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['post_by', 'title', 'body', 'image']