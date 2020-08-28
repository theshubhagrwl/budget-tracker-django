from django.urls import path, include
from . import views

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.home, name='home'),
    path('users/', include("api.users.urls")),
    path('items/', include("api.budget_app.urls")),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
