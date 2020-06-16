from rest_framework import serializers
from ttc_rest_api.models import TTC_POST_TB, TTC_COMMENT_TB
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = TTC_POST_TB
        fields = ('title', 'content', 'postDate', 'modifiedDate', 'postBy', 'uuidPost')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTC_COMMENT_TB
        fields = ('uuidPost', 'commentBy', 'text', 'created_date')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


