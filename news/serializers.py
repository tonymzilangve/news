from rest_framework import serializers
from feedback.serializers import UnderCommentSerializer
from .models import *


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    last_comments = serializers.SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return obj.author.username

    def get_last_comments(self, obj):
        query = obj.comments.all().order_by('-timestamp')[:10]
        serializer = UnderCommentSerializer(query, many=True)
        return serializer.data

    class Meta:
        model = News
        fields = ('id', 'title', 'author', 'text', 'timestamp', 'likes', 'total_comments', 'last_comments')


class PostNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'text')
