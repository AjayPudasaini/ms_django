from rest_framework.decorators import APIView
from user.serializers import UserCreateSerializer, UserSerializer, TokenObtainPairSerializer, MySerializer
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import User

class UserRegisterAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['email'] = user.email
            return JsonResponse({
                'message': f"user ({ user.email }) created",
                'success': True,
                'status' : status.HTTP_201_CREATED,
                'result' : data
            })
        else:
            data = serializer.errors

        return Response(data)
    

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class UserListApiView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        user = User.objects.all()

        serializer = UserSerializer(user, many=True)

        return JsonResponse({'user': serializer.data})




class UserDetailAPIView(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserCreateSerializer(user)
        return JsonResponse({'user': serializer.data, "success":True})
    


class UserDeleteAPIView(APIView):
    permission_classes = (AllowAny, )
    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return JsonResponse({'user': user.email, 'message':"user deleted success", "success": True})



    

class MyView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = MySerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            
            return JsonResponse({
                'message': f"created",
                'success': True,
                'status' : status.HTTP_201_CREATED,
            })
        else:
            data = serializer.errors

        return Response(data)