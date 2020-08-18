from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def home(request):
    return Response({"users": "users/", "items": "items/"})
