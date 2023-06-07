from django.contrib import admin
from django.urls import path
from user.views import UserRegisterAPIView, EmailTokenObtainPairView,UserListApiView, UserDetailAPIView, UserDeleteAPIView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView


from user.server import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', UserRegisterAPIView.as_view(), name='register'),
    path('api/login/', EmailTokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', UserListApiView.as_view(), name = "users"),
    path('api/user/<int:pk>', UserDetailAPIView.as_view(), name="user_detail"),
    path('api/user-delete/<int:pk>', UserDeleteAPIView.as_view(), name="user_delete"),
    path('serve/', serve(), name="serve"),
    # path('api/ser/', MyView.as_view(), name='ser')
]
