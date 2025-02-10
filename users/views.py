from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer
from django.http import HttpResponse
from django.shortcuts import render

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

def home(request):
    return HttpResponse("Welcome to My Social Network!")
def index(request):
    return render(request, 'index.html')
