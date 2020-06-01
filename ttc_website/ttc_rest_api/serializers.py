from rest_framework import serializers
from ttc_rest_api.models import TTC_POST_TB

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = TTC_POST_TB
        fields = ('title', 'content', 'postDate', 'modifiedDate', 'postBy')
