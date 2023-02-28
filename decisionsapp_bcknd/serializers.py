from .models import Decision
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class DecisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Decision
        fields = ['id','regBody', 'companyName', 'decisionType', 'allegationType']
    