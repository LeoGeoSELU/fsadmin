# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BaseScore, DataSource
from rest_framework import viewsets
from .serializers import BaseScoreSerializer
import requests


class BaseScoreList(APIView):

    def get(self, request):
        print(request)
        base_scores = BaseScore.objects.all()
        serializer = BaseScoreSerializer(base_scores, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class BaseScoreViewSet(viewsets.ModelViewSet):
    queryset = BaseScore.objects.all()
    serializer_class = BaseScoreSerializer


def datalist(request):
    datasources = list(DataSource.objects.all())
    for sources in datasources:
        print(sources.request_url)
    return render(request, "api/sourcelist.html", {'datasources': datasources})


def datacall(request, source_id):
    call_source = get_object_or_404(DataSource, id=source_id)
    call_response = requests.get(call_source.request_url)
    print(call_response.json())
    return render(request, 'api/datacall.html', {'callresponse': call_response.json()})
