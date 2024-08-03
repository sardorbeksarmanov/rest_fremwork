from rest_framework import serializers
from .models import Artist, Albom, Songs

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['first_name', 'last_name', 'username', 'create_at']

class AlbomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ['id', 'title', 'artist']

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Songs
        fields = ['id', 'title', 'albom']
