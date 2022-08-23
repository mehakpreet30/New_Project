from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.decorators import api_view
from rest_framework import status



# Create your views here.

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
 

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



# Login

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


# Staff

class StaffAPI(generics.GenericAPIView):
    serializer_class = StaffSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        staff = serializer.save()
        return Response({
        "staff": StaffSerializer(staff, context=self.get_serializer_context()).data,
        #"token": AuthToken.objects.create(staff)[1]
        })


# Creating a view

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Add': '/create',
        'Update': '/update/id',
        'Delete': '/item/id/delete'
    }
  
    return Response(api_urls)




# View ALl List of Staff
@api_view(['GET']) #get method to retrive data
def view_items(request):
    items = Staff.objects.all()
    serializer = StaffSerializer(items, many=True)

    # if there is something in items else raise error
    if items:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



# Create Staff
@api_view(['POST'])
def add_items(request):
    item = StaffSerializer(data=request.data)
  
    # validating for already existing data
    if Staff.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# Update Staff
@api_view(['POST'])
def update_items(request, id):
    item = Staff.objects.get(id=id)
    serializer = StaffSerializer(instance=item, data=request.data)
  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# Delete Staff
@api_view(['DELETE'])
def delete_items(request, id):
    staff = Staff.objects.get(id=id)
    if request.method == 'DELETE': 
        staff.delete() 
        return Response({'message': 'Staff was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)