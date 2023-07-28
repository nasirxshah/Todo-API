from rest_framework import serializers
from .models import ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ['id','title','description','is_completed','created_at','last_update']
    
    def create(self, validated_data):
        return ToDoItem.objects.create(profile=self.context['profile'],**validated_data)
    

