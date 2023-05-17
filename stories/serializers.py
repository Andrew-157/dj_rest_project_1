from rest_framework import serializers
from stories.models import Story
from users.models import CustomUser


class StorySerializer(serializers.HyperlinkedModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    author = serializers.HyperlinkedRelatedField(
        view_name='author-detail', read_only=True
    )

    class Meta:
        model = Story
        fields = ['url', 'id', 'title', 'content',
                  'pub_date', 'author_name', 'author']


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    # You can prefix view_name with app's name, but
    # then you'll have to write url field explicitly in all
    # other views that are using HyperlinkedModelSerializer
    # to prefix view_names with app's name
    url = serializers.HyperlinkedIdentityField(
        view_name='author-detail')
    stories = serializers.HyperlinkedRelatedField(
        many=True, view_name='story-detail', read_only=True
    )

    class Meta:
        model = CustomUser
        fields = [
            'url', 'id', 'username', 'stories',
        ]
