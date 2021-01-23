from django.shortcuts import render
from .models import items
from django.http import JsonResponse

from serializers import items_serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def home(request):
    api_urls = {
        'List' : '/task-list',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-create/',
        'Update' : '/task-update/<str:pk>',
        'Delete' : '/task-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def task_list(request):
    item = items.objects.all().order_by('-id')
    serializer = items_serializer(item, many=True)
    