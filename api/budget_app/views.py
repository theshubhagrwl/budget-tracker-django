from re import search
from api.users.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import ItemSerializer
from .models import Items
import json
from django.core.exceptions import ObjectDoesNotExist


class UserItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    # perimission_classes = [IsAuthenticated]
    # queryset = Items.objects.all()

    def get_queryset(self,  *args):
        return Items.objects.filter(user=self.request.user.id)


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Items.objects.all()
    # permission_classes = [IsAuthenticated]


@csrf_exempt
@permission_classes([IsAuthenticated])
@api_view(['POST', ])
def addItem(request):
    item = Items(user=request.user)
    if request.method == "POST":
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@csrf_exempt
# @permission_classes([IsAuthenticated])
@api_view(['DELETE', ])
def deleteItem(request, pk):
    try:
        item = Items.objects.get(user=request.user, id=pk)
        item.delete()
        return JsonResponse({"success": "deleted item"})
    except ObjectDoesNotExist:
        return JsonResponse({"error": 'invalid id'})


@csrf_exempt
# @permission_classes([IsAuthenticated])
@api_view(['PUT', ])
def updateItem(request, pk):

    try:
        item = Items.objects.filter(user=request.user, id=pk)
        # item.update(request.data)
        item = Items.objects.get(id=pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Invalid Id"})

        # item = Items.objects.filter(user=request.user, id=pk)

        # if request.method == "POST":
        #     serializer = ItemSerializer(item, data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data)
        #     return Response(serializer.errors)

        # @login_required
        # def updateItem(request, pk):
        #     u_items = BudgetItem.objects.filter(user=request.user).get(id=pk)
        #     form = addItemForm(instance=u_items)

        #     if request.method == "POST":
        #         form = addItemForm(request.POST, instance=u_items)
        #         form.save()
        #         return redirect(items)

        #     return render(request, 'budget_app/updateItem.html', {'items': u_items, 'form': form})
