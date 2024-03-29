from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stories import views

router = DefaultRouter()
router.register(r'stories', views.StoryViewSet, basename='story')
router.register(r'authors', views.AuthorViewSet, basename='author')

# app_name = 'stories'
urlpatterns = [
    path('', include(router.urls))
]
