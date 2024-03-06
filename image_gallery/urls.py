from django.urls import path
from .views import ImageGalleryAPIView, ImageView, ViewImageGalleryAPIView

urlpatterns = [
    # admin or users that have full access
    path('images/', ImageGalleryAPIView.as_view(), name='image_gallery_list'),
    path('images/<int:pk>/', ImageView.as_view(), name='image_detail'),
    path('images/<int:pk>/delete/', ImageView.as_view(), name='image_delete'),
    path('images/<int:pk>/update/', ImageView.as_view(), name='image_update'),

   # users that have no full access
    path('view-images/', ViewImageGalleryAPIView.as_view(), name='view_image_gallery_list'),
    path('view-images/<int:pk>/', ViewImageGalleryAPIView.as_view(), name='image_detail'),
    path('view-images/<int:pk>/delete/', ViewImageGalleryAPIView.as_view(), name='image_delete'),
    path('view-images/<int:pk>/update/', ViewImageGalleryAPIView.as_view(), name='image_update'),
]
