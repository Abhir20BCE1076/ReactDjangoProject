from rest_framework.response import Response
from rest_framework.decorators import api_view 
from .serializers import UserSerializer
from djangoRestApp.models import User
@api_view(['POST'])
def registerUser(request):
    user = request.data 
    serializer = UserSerializer(data = user) 
    if serializer.is_valid():
        serializer.save() 
    return Response("User created!!")


@api_view(['POST'])
def loginUser(request):
    user = request.data 
    valid_user = User.objects.get(userName = user.get("userName"))
    if valid_user and valid_user.passWord == user.get("passWord"):
        return Response("User authenticated!!!")
    else:
        return Response("Invalid credentials!!")