from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status, views, permissions
from rest_framework.exceptions import AuthenticationFailed
from UserManagement.serializers import LoginSerializer,UserSerializer
from django.contrib.auth import get_user_model
Users = get_user_model()

class LoginUserView(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            # Access the tokens from the serializer's validated data
            access_token = serializer.validated_data.get('access')
            refresh_token = serializer.validated_data.get('refresh')
            # Do something with the tokens, if needed
            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_200_OK)
        except AuthenticationFailed as e:
            return Response({'detail': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            # Handle other unexpected exceptions
            return Response({'detail': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

     





class IamUserDetailsView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer
    queryset = Users.objects.all()

    def get_object(self):
        obj = Users.objects.get(pk=self.request.user.pk)
        self.check_object_permissions(self.request, obj)
        return obj