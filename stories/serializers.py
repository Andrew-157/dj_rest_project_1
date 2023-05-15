from rest_framework import serializers
from stories.models import Story


class StorySerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Story
        fields = ['url', 'id', 'title', 'content', 'author', 'pub_date']
