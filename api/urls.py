from django.urls import path, include

urlpatterns = [
    path('users/', include("api.users.urls")),
    path('items/', include("api.budget_app.urls")),
]
