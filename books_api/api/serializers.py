from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'birth_date']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
       model = Book
       fields = '__all__'

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user.author
        return super().create(validated_data)