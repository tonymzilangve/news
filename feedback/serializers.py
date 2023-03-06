from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
    news = serializers.RelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'news', 'author', 'text', 'timestamp')


class PostCommentSerializer(serializers.ModelSerializer):
    news = serializers.RelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'news', 'text')    # -news
