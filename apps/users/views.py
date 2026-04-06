from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated , AllowAny
from apps.users.permissions import IsAdmin
from rest_framework_simplejwt.views import TokenObtainPairView
from .jwt import CustomTokenSerializer
from rest_framework.throttling import ScopedRateThrottle
from .throttles import LoginThrottle, RegisterThrottle


class RegisterView(APIView):
    permission_classes = [AllowAny] 

    throttle_classes = [RegisterThrottle]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "success": True,
                "message": "User registered successfully",
                "data": {
                    "user_id": str(user.id),
                    "role": user.role
                }
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateRoleView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def patch(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({
                "success": False,
                "message": "User not found"
            }, status=status.HTTP_404_NOT_FOUND)

        role = request.data.get("role")

        if role not in ['viewer', 'analyst', 'admin']:
            return Response({
                "success": False,
                "message": "Invalid role"
            }, status=status.HTTP_400_BAD_REQUEST)

        user.role = role
        user.save()

        return Response({
            "success": True,
            "message": "Role updated successfully",
            "data": {
                "user_id": str(user.id),
                "role": user.role
            }
        }, status=status.HTTP_200_OK)

class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny] 
    serializer_class = CustomTokenSerializer

    throttle_classes = [LoginThrottle]
    