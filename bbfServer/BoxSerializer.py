from rest_framework import serializers
from .models import Box


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ('Id', 'City', 'State', 'Country', 'Zip_code', 'Latitude', 'Longitude', 'address')
