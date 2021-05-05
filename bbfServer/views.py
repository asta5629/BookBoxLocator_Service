from math import cos, sqrt
from decimal import Decimal
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Box
from .BoxSerializer import BoxSerializer


@api_view(['GET'])
def getAllBoxes(request):
    if request.method == 'GET':
        boxes = Box.objects.all()
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getBoxesByZip(request):
    if request.method == 'GET':
        zip_code = request.query_params.get('zip_code')
        boxes = Box.objects.filter(Zip_code=zip_code)
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getBoxesOnMap(request):
    # coordinates are Lat/Long

    neCorner = request.query_params.get('neCorner').split(",")  # [45.087743601,-92.938096689]
    swCorner = request.query_params.get('swCorner').split(",")  # [44.65108237,-93.5031088069]
    if request.method == 'GET':
        boxes = Box.objects.filter(Latitude__lt=neCorner[0]).filter(Longitude__lt=neCorner[1]).filter(Latitude__gt=swCorner[0]).filter(Longitude__gt=swCorner[1])
        serializer = BoxSerializer(boxes, many=True)
        print(serializer.data)
        return Response(serializer.data)


@api_view(['GET'])
def getBoxesNearby(request):
    if request.method == 'GET':
        userlon = Decimal(request.query_params.get('Longitude'))
        userlat = Decimal(request.query_params.get('Latitude'))
        R = 6371000  # radius of the Earth in m
        def distance(lon1, lat1, lon2, lat2):
            x = (lon2 - lon1) * Decimal(cos(Decimal(0.5) * (lat2 + lat1)))
            y = (lat2 - lat1)
            return R * sqrt(x * x + y * y)

        Boxes = set(Box.objects.all())

        sortedBoxes = sorted(Boxes, key=lambda d: distance(Decimal(d.Longitude), Decimal(d.Latitude), userlon, userlat))
        nearBoxes = sortedBoxes[:5]
        serializer = BoxSerializer(nearBoxes, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getBoxesByCityState(request):
    if request.method == 'GET':
        city1 = request.query_params.get('City')
        state1 = request.query_params.get('State')
        boxes = Box.objects.filter(City=city1).filter(State=state1)
        serializer = BoxSerializer(boxes, many=True)
        return Response(serializer.data)
