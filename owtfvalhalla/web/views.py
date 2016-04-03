from pprint import pprint
import json

from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from owtfcontainer import OwtfContainer
from owtfcontainer.handler import locate_owtf_containers, owtf_containers_located_in_container_folder


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class ListAllOwtfContainers(APIView):

    renderer_classes = (JSONRenderer,)

    def get(self, request, format=None):

        return HttpResponse([i.config for i in owtf_containers_located_in_container_folder], content_type='application/json')


