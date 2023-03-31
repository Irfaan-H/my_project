from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import workersSerializers
from .models import workers   


class workersList(APIView):
    def get(self,request):
        workers1=workers.objects.all()
        serializer=workersSerializers(workers1,many=True)
        return Response(serializer.data)
    
class workersDetail(APIView):

    def workersdetail(request,pk):
        workers1=workers.objects.get(id=pk)
        serializer=workersSerializers(workers1,many=False)
        return Response(serializer.data)
         