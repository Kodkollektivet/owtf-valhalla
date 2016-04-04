
from rest_framework import serializers


class OwtfContainerSerializer(serializers.Serializer):
    image = serializers.CharField(max_length=254, required=False)
    image_id = serializers.CharField(max_length=254, required=False)
    image_name = serializers.CharField(max_length=254, required=False)
    image_version = serializers.CharField(max_length=254, required=False)
    image_path = serializers.CharField(max_length=254, required=False)

    container_id = serializers.CharField(max_length=254, required=False)
    container_name = serializers.CharField(max_length=254, required=False)
    container_tag = serializers.CharField(max_length=254, required=False)

    config = serializers.JSONField()
    ip_address = serializers.CharField(max_length=254, required=False)

    is_image_build = serializers.BooleanField()
    is_container_build = serializers.BooleanField()
    is_valid = serializers.BooleanField()
    is_running = serializers.BooleanField()


class CommandSerializer(serializers.Serializer):
    command_obj = serializers.JSONField()