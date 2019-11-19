from django.shortcuts import get_object_or_404

from rest_framework.response import Response  # JSON 응답 생성기
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny  # 회원가입은 인증을 볼 필요없음

from .serializers import UserCreationSerializer, UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny, ])
def signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return Response(status=200, data={'message': '회원가입 성공'})


@api_view(['GET'])
def my_todos(request):
    user = request.user  # JWT를 통해서 요청보낸 사용자를 잡아 냄
    serializer = UserSerializer(user)
    return Response(serializer.data)