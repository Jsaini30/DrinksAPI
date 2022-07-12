from rest_framework import serializers
from .models import Drink, Writer, book


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'desc']


class bookserializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = ['id', 'title', 'author', 'totalpages', 'category']


class writerserializer(serializers.ModelSerializer):
    Books_Written = bookserializer(many= True, read_only=True)
    class Meta:
        model = Writer
        fields = ['id', 'name', 'gender','Books_Written']
