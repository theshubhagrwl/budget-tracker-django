from rest_framework import routers
from django.urls import path, include

# from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)

urlpatterns = [
    path('login/', views.signin, name='signin'),
    # path('login/', obtain_auth_token, name='signin'),
    path('logout/<int:id>/', views.signout, name='signout'),
    path('', include(router.urls)),
]
