from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from stories.models import Story
from stories.serializers import StorySerializer
from stories.permissions import IsAuthorOrReadOnly


class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.select_related('author').all()
    serializer_class = StorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
