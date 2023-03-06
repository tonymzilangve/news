from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    news_title = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'news', 'news_title', 'author', 'text', 'timestamp')

    def get_news_title(self, obj):
        return obj.news.title

    def get_author(self, obj):
        return obj.author.username


class PostCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'news', 'text')


class UnderCommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)

    def get_author(self, obj):
        return obj.author.username

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'timestamp')
