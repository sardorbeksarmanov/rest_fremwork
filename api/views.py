from rest_framework.views import APIView
from rest_framework import status
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer, AlbomSerializer, SongSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class ArtistViewSet(APIView):
    def get(self, request, id=None):
        if id:
            try:
                artist = Artist.objects.get(id=id)
                serializer = ArtistSerializer(artist)
                return Response(data=serializer.data)
            except Artist.DoesNotExist:
                raise NotFound("Artist not found")
        else:
            queryset = Artist.objects.all()
            serializer = ArtistSerializer(queryset, many=True)
            return Response(data=serializer.data)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(artist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artist = Artist.objects.get(id=id)
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AlbomViewSet(APIView):
    def get(self, request, id=None):
        if id:
            try:
                albom = Albom.objects.get(id=id)
                serializer = AlbomSerializer(albom)
                return Response(data=serializer.data)
            except Albom.DoesNotExist:
                raise NotFound("Albom not found")
        else:
            alboms = Albom.objects.all()
            serializer = AlbomSerializer(alboms, many=True)
            return Response(data=serializer.data)

    def post(self, request):
        serializer = AlbomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = AlbomSerializer(albom, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        albom = Albom.objects.get(id=id)
        serializer = AlbomSerializer(albom, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        albom = Albom.objects.get(id=id)
        albom.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongViewSet(APIView):
    def get(self, request, id=None):
        if id:
            try:
                song = Songs.objects.get(id=id)
                serializer = SongSerializer(song)
                return Response(data=serializer.data)
            except Songs.DoesNotExist:
                raise NotFound("Song not found")
        else:
            queryset = Songs.objects.all()
            serializer = SongSerializer(queryset, many=True)
            return Response(data=serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        song = Songs.objects.get(id=id)
        serializer = SongSerializer(song, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        song = Songs.objects.get(id=id)
        serializer = SongSerializer(song, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        song = Songs.objects.get(id=id)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
