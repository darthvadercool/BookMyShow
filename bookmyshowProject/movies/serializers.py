from rest_framework import serializers

from .models import Movies, Moviegenre, Movielanguages, Agecategory, Moviedimension, Actor, \
    Movielanguagemap, Agecategory


class MoviesListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = ['id', 'movies_name', 'about', 'release_date', 'duration']


class MoviesDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movies
        fields = ['id', 'movies_name', 'about', 'release_date',
                  'duration', 'created_on', 'updated_on', 'is_deleted']


class MoviesLanguageListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movielanguages
        fields = ['id', 'language']


class MoviesLanguageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movielanguages
        fields = ['id', 'language',  'created_on', 'updated_on', 'is_deleted']


class MoviesGenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moviegenre
        fields = ['id', 'genre_name']


class MoviesDimensionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moviedimension
        fields = ['id', 'dimension']


class MoviesCertificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agecategory
        fields = ['id', 'certification']


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['id', 'firstname', 'lastname']


class ActorDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['id', 'firstname', 'lastname',
                  'created_on', 'updated_on', 'is_deleted']


class MovieLangMapSerializer(serializers.ModelSerializer):

    movie = MoviesDetailSerializer()
    certification = MoviesLanguageDetailSerializer()

    class Meta:
        model = Movielanguagemap
        fields = ['id', 'movie', 'movielanguage']


class CertificationMapSerializer(serializers.ModelSerializer):

    movie = MoviesDetailSerializer()
    certification = MoviesCertificationSerializer()

    class Meta:
        model = Movielanguagemap
        fields = ['id', 'movie', 'certification']
