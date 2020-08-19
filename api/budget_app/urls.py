from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter()
router.register(r'list', views.ItemViewSet)
router.register(r'user-item', views.UserItemViewSet, basename='user-item')

urlpatterns = [
    # path('hello/', views.hello, name='hello'),
    path('', include(router.urls)),
    path('add-item/', views.addItem, name='add-item'),
    path('delete-item/<int:pk>/', views.deleteItem, name='delete-item'),
    path('update-item/<int:pk>/', views.updateItem, name='update-item'),
    # path('', include(router.urls)),



    # path('update/<int:pk>', views.updateItem, name='updateItem'),
]
