from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        attrs['username'] = attrs.get('email')
        data = super().validate(attrs)
        user = self.user
        data["user"] = {
            "id": str(user.id),
            "email": user.email,
            "role": user.role
        }
        return data