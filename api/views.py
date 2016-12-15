# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import BaseScore, DataSource
from rest_framework import viewsets
from .serializers import BaseScoreSerializer
import requests
import dateutil.parser
from django.utils.dateparse import parse_datetime


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
    # res = call_response.json()
    # response_dict = {
    #     'name': '',
    #     'location': {},
    #     'variablename': {},
    #
    # }
    # for k in res['value']['timeSeries']:
    #     if response_dict['name'] == '':
    #         response_dict['name'] = k['sourceInfo']['siteName']
    #     if not response_dict['geolocation']:
    #         response_dict['geolocation'] = k['sourceInfo']['geoLocation']['geogLocation']
    #     response_dict['variablename'][k['variable']['variableName']] = k['variable']['variableName']
    #     for val in k['values']:
    #         response_dict['variablename'][k['variable']['variableName']] = []
    #         for output in val['value']:
    #             print('\t' + str(output))
    #             print(dateutil.parser.parse(output['dateTime']))
    print(call_response.json())
    return render(request, 'api/datacall.html', {'callresponse': call_response.json()})


def response(request, source_id):
    call_source = get_object_or_404(DataSource, id=source_id)
    call_response = requests.get(call_source.request_url)
    res = call_response.json()
    ts = res['value']['timeSeries']
    sourceinfo = ts[0]['sourceInfo']
    sourcegeoinfo = sourceinfo['geoLocation']['geogLocation']

    siteDict = {'name': sourceinfo['siteName'], 'geolocation': sourcegeoinfo, 'data': {}}

    for x in ts:
        siteDict['data'][x['variable']['variableCode'][0]['value']] = [
            {
                'timeseries': x['name'],
                'description': x['variable']['variableDescription'],
                'unit': x['variable']['unit']['unitCode']
            }
        ]
        for y in x['values'][0]['value']:
            siteDict['data'][x['variable']['variableCode'][0]['value']].append(
                {'value': y['value'], 'datetime': dateutil.parser.parse(y['dateTime']),})

    return render(request, 'api/response.html', {'callresponse': siteDict})
