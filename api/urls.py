from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', include("api.users.urls")),
    path('items/', include("api.budget_app.urls")),
]
