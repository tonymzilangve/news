from rest_framework import serializers

from feedback.models import Comment
from news.models import News
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=16, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password',)

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=16, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'token')

        read_only_fields = ['token']


class UserSerializer(serializers.ModelSerializer):
    news_count = serializers.SerializerMethodField(read_only=True)
    comments_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'news_count', 'comments_count')

    # check!
    def get_news_count(self, obj):
        return News.objects.filter(author=obj).count()   # author = self/

    def get_comments_count(self, obj):
        return Comment.objects.filter(author=obj).count()
