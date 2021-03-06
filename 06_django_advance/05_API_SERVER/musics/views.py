from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Artist, Music
from .serializers import ArtistSerializer, MusicSerializer, ArtistDetailSerializer, CommentSerializer, MusicDetailSerializer

import json

# 달라, 써라, 수정해라, 삭제해라
# Read, Create, Update, Delete
# GET, POST, PATCH, DELETE


@api_view(['GET'])  # get요청만 처리 하겠다
def artist_list(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    # data_set = []
    # for artist in artists:
    #     d = {
    #         "id": artist.id,
    #         "name": artist.name,
    #     }
    #     data_set.append(d)
    
    # # 공용어(string)로 바꾸다. (Serialization: 직렬화)
    # res_data = json.dumps(data_set)
    # print(type(res_data), res_data)

    return Response(serializer.data)


@api_view(['GET'])
def artist_detail(request, artist_id):
    artists = get_object_or_404(Artist, id=artist_id)
    serializer = ArtistDetailSerializer(artists)
    return Response(serializer.data)


@api_view(['GET'])
def music_list(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def music_detail(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    ser = MusicSerializer(music)
    return Response(ser.data)


@api_view(['POST'])
def create_comment(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    ser = CommentSerializer(data=request.data)  # request.POST vs request.data
    if ser.is_valid(raise_exception=True):
        ser.save(music_id=music.id)  # 저장 완료
    return Response(ser.data)  # 저장한 데이터



