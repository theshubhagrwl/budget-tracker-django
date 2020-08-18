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
    # path('', include(router.urls)),



    # path('signup/', views.signupuser, name='signupuser'),
    # path('logout/', views.logoutuser, name='logoutuser'),
    # path('login/', views.loginuser, name='loginuser'),
    # # App stuff
    # path('add/', views.addItem, name='addItem'),
    # path('items/', views.items, name='items'),
    # path('about/', views.about, name='about'),
    # path('update/<int:pk>', views.updateItem, name='updateItem'),
    # path('delete/<int:pk>', views.deleteItem, name='deleteItem'),
]
