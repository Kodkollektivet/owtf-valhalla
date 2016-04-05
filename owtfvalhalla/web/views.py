from pprint import pprint
import json

from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from web import serializers

from owtfcontainer import get_owtf_c


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class ListAll(APIView):
    """Lists all the containers."""

    def get(self, request, format=None):

        serializer = serializers.OwtfContainerSerializer(
            get_owtf_c()[1],  # Get all containers
            many=True
        )

        return Response(serializer.data, status=status.HTTP_200_OK)


class Info(APIView):
    """Get info about a specific container."""

    def get(self, request, image, *args, **kwargs):

        sts, image = get_owtf_c(image=image)

        if sts:
            serializer = serializers.OwtfContainerSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return HttpResponse('Failed!')


class BuildImage(APIView):
    """Build image"""

    def get(self, request, image, *args, **kwargs):

        sts, image = get_owtf_c(image=image)

        if sts:
            image.build_image()
            serializer = serializers.OwtfContainerSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return HttpResponse('Failed!')


class RemoveImage(APIView):
    """Remove image"""

    def get(self, request, image, *args, **kwargs):

        sts, image = get_owtf_c(image=image)

        if sts:
            image.remove_image()
            serializer = serializers.OwtfContainerSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return HttpResponse('Failed!')


class BuildContainer(APIView):
    """Build container"""

    def get(self, request, image, *args, **kwargs):

        sts, image = get_owtf_c(image=image)

        if sts:
            image.build_container()
            serializer = serializers.OwtfContainerSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return HttpResponse('Failed!')


class RemoveContainer(APIView):
    """Remove container"""

    def get(self, request, image, *args, **kwargs):

        sts, image = get_owtf_c(image=image)

        if sts:
            image.remove_container()
            serializer = serializers.OwtfContainerSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return HttpResponse('Failed!')


class Start(APIView):
    """Start container"""

    def get(self, request, image, *args, **kwargs):

        sts, image = get_owtf_c(image=image)

        if sts:
            image.start()
            serializer = serializers.OwtfContainerSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return HttpResponse('Failed!')


class Stop(APIView):
    """Stop container"""

    def get(self, request, image, *args, **kwargs):

        sts, image = get_owtf_c(image=image)

        if sts:
            image.stop()
            serializer = serializers.OwtfContainerSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return HttpResponse('Failed!')


class Execute(APIView):
    """Get a command and the pass it on to the associated container"""

    def get(self, request, image, *args, **kwargs):

        sts, image = get_owtf_c(image=image)

        if sts:
            serializer = serializers.OwtfContainerSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return HttpResponse('Failed!')

    def post(self, request, image, *args, **kwargs):
        sts, image = get_owtf_c(image=image)

        if sts:

            command = serializers.CommandSerializer(data=request.data)
            pprint(command.command)
            serializer = serializers.OwtfContainerSerializer(image)
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return HttpResponse('Failed!')
