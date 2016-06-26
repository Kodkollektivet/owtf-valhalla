from rest_framework import serializers


class OwtfContainerSerializer(serializers.Serializer):
    """This serializer object maps to the OwtfContainer object.
    The reason for this is to more easily transfer between a Python obj and a JSON object.
    This object is mainly used in views.py where we map OwtfContainer to OwtfContainerSerializer
    and send the OwtfContainerSerializer object as JSON.
    """
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
    port = serializers.IntegerField(required=False)

    results = serializers.JSONField(required=False)

    is_image_built = serializers.BooleanField()
    is_container_built = serializers.BooleanField()
    is_valid = serializers.BooleanField()
    is_running = serializers.BooleanField()

    # Lazy urls
    build_url = serializers.URLField(required=True)
    remove_url = serializers.URLField(required=False)
    build_image_url = serializers.URLField(required=True)
    remove_image_url = serializers.URLField(required=False)
    build_container_url = serializers.URLField(required=False)
    remove_container_url = serializers.URLField(required=False)
    start_url = serializers.URLField(required=False)
    stop_url = serializers.URLField(required=False)
    execute_url = serializers.URLField(required=False)


class CommandSerializer(serializers.Serializer):
    """This is the serializer for the commands that we receive through the Rest API.
    The command is a JSON object that we then will pass on to the associated container
    and the container executes the command.
    """
    command = serializers.CharField(allow_blank=False)
    code = serializers.CharField()
    noise = serializers.CharField()
    target = serializers.CharField(required=False, allow_blank=True)
    description = serializers.CharField()
    results = serializers.CharField(required=False, allow_blank=False)


