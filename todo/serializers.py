from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        # fields = '__all__'
        # fields = []
        exclude = [
            'created_date',
            'updated_date',
        ]