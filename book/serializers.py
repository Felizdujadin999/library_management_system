from rest_framework import serializers


class AuthorSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    date_of_birth = serializers.DateField()
