from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView

from . import models
from . import permissions
from .serializers import MySerializer, UserSerializer


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

    def put(self, request, pk=None):
        return Response({'message': 'this is put'})

    def patch(self, request, pk=None):
        return Response({'message': 'this is patch'})

    def delete(self, request, pk=None):
        return Response({'message': 'this is delete'})


class MyViewSet(viewsets.ViewSet):
    serializer_class = MySerializer

    def list(self, request):
        data = [f'item#{x}' for x in range(5)]
        return Response({'data': data})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({'message': f'hey {serializer.validated_data.get["name"]}'})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def destroy(self, request, pk=None):
        return Response({'message': 'destroyed smth'})

    def update(self, request, pk=None):
        return Response({'message': 'updated smth'})

    def partial_update(self, request, pk=None):
        return Response({'message': 'partially updated smth'})

    def retrieve(self, request, pk=None):
        return Response({'message': 'retrieved smth'})


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = models.MyUser.objects.all()
    permission_classes = (permissions.MyPermission,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'email')


class AuthViewApi(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
