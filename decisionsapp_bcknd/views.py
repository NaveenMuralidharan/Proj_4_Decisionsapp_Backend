# from django.shortcuts import render
from .models        import Decision
from rest_framework import viewsets
from rest_framework import permissions
from .serializers   import DecisionSerializer

# Create your views here.
class DecisionViewSet(viewsets.ModelViewSet):
    queryset = Decision.objects.all()
    serializer_class = DecisionSerializer
    permission_classes = [permissions.AllowAny]
    