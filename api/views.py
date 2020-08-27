from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def home(request):
    return Response({
        "users/": "list of all users",
        "users/": "send a POST JSON request to create new user",
        "users/login/": "login a user",
        "users/logout/": "logout a user",
        "users/<int:id>/": "send a PUT request to update name of a user",
        "items/list/": 'list of all items',
        "items/user-item/": 'list of all items of current user',
        "items/add-item/": 'add an item',
        "items/update-item/<int:id>/": 'update an item',
        "items/delete-item/<int:id>/": 'delete an item',
    })
