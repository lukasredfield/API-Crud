from .models import Project
from rest_framework import serializers 

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
       model = Project 
       fields = ('id', 'title','description','technology','created_at')
       read_only_fields = ('created_at', )

