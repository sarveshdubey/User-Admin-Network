from rest_framework import generics, serializers
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime 
import jwt 


#local imports
from .models import Admin, UserModel
from .serializers import AdminSerializer, UserSerializer

# Create your views here.

  ###Advisor Panel###
class AdminView(generics.CreateAPIView): #tested with Postman
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

  ###User Panel###
#Registering User
class UserRegisterView(APIView):
    def post(self, request):
        serializer_class = UserSerializer(data=request.data)
        serializer_class.is_valid(raise_exception=True)
        serializer_class.save()
        return Response(serializer_class.data)

#User Login
class UserLoginView(APIView):
    def post(self,request):
        email = request.data['email']
        u_name = request.data['u_name']
        password = request.data['password']

        user = UserModel.objects.filter(u_name=u_name).first() #searching user by u_name

        if user is None:
            raise AuthenticationFailed("No User registered with this name")
        
        if user.password != password :
            raise AuthenticationFailed('Incorrect Password')
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow(),
        }
        
        token = jwt.encode(payload,'secret',algorithm='HS256').decode('utf-8')
        
        return Response({
            'jwt': token,
            'id':user.id
        })
        


        








    
    

    
