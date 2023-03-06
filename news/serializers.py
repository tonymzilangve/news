from rest_framework import serializers

from feedback.serializers import CommentSerializer
from .models import *


class NewsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'author', 'text', 'timestamp', 'likes', 'comments')   # 'last_10_comments'


class PostNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'text')
