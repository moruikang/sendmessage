from rest_framework import serializers


class SmsSerializer(serializers.Serializer):
    # mandatory
    username = serializers.CharField(max_length=30, min_length=4)
    phone = serializers.CharField(max_length=11)
    verify_code = serializers.CharField(max_length=6)
    content = serializers.CharField(max_length=300)


class EmailSerializer(serializers.Serializer):
    # mandatory
    username = serializers.CharField(max_length=30, min_length=4)
    email = serializers.CharField(max_length=30)
    verify_code = serializers.CharField(max_length=6)
    content = serializers.CharField(max_length=300)