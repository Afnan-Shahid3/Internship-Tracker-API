from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import CompanySerializer, InterviewSerializer, ContactSerializer, ApplicationSerializer
from rest_framework import viewsets
from .models import Company, Interview, Application, Contact
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['POST'])
def login_api(request):
    try:

        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username = username, password = password)
        if user:
            token = Token.objects.get_or_create(user = user)
            return Response({'status' : 200, 'token' : str(token)})

        return Response({'status' : 300, 'message' : "Invalid Credentials"})

    except Exception as e:
        print(e)
    return Response({
        'status' : 400,
        'message': "Something went wrong"
    })

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class CompanyModelViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    
    def queryset(self):
        return Company.objects.filter(user = self.request.user)



@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class InterviewModelViewSet(viewsets.ModelViewSet):
    serializer_class = InterviewSerializer
    def queryset(self):
        return Interview.objects.filter(user = self.request.user)



@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ApplicationModelViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    def queryset(self):
        return Application.objects.filter(user = self.request.user)




@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ContactModelViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    def queryset(self):
        return Contact.objects.filter(user = self.request.user)



    

