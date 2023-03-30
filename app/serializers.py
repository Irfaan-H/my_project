from rest_framework import serializers
from .models import workers

class workersSerializers(serializers.ModelSerializer):

    class Meta:
        model  = workers

        fields ='__all__'
