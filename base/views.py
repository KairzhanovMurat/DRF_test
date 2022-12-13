from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MySerializer
from rest_framework import status

# Create your views here.

class ProfileApi(APIView):
    serializer_class = MySerializer

    def get(self, request):
        data = ['some shit', 'another shit', 'fuck off']
        return Response({'data': data})

    def post(self, request):
        name = self.serializer_class(data=request.data)
        if name.is_valid():
            _name = name.validated_data.get('name')
            message = f'Hello {_name}'
            return Response({'message': message})
        else:
            return Response(
                name.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        return Response({'message':'this is put'})

    def patch(self,request,pk=None):
        return Response({'message':'this is patch'})

    def delete(self,request,pk=None):
        return Response({'message':'this is delete'})
