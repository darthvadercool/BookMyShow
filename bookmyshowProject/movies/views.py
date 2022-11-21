
from rest_framework import generics

from .serializers import MoviesListSerializer, MoviesDetailSerializer, \
    MoviesLanguageListSerializer, MoviesLanguageDetailSerializer, \
    MoviesGenreSerializer, MoviesDimensionSerializer, MoviesCertificationSerializer, \
    ActorListSerializer, ActorDetailSerializer, MovieLangMapSerializer, CertificationMapSerializer


from .models import Movies, Movielanguages, Moviegenre, Moviedimension, Agecategory, Actor, Movielanguagemap, Moviecertificationmap


class MovieList(generics.ListCreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesListSerializer


class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesDetailSerializer


class MovieLanguageList(generics.ListCreateAPIView):
    queryset = Movielanguages.objects.all()
    serializer_class = MoviesLanguageListSerializer


class MovieLangDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movielanguages.objects.all()
    serializer_class = MoviesLanguageDetailSerializer


class MovieGenreList(generics.ListCreateAPIView):
    queryset = Moviegenre.objects.all()
    serializer_class = MoviesGenreSerializer


class MovieGenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moviegenre.objects.all()
    serializer_class = MoviesGenreSerializer


class MovieDimensionList(generics.ListCreateAPIView):
    queryset = Moviedimension.objects.all()
    serializer_class = MoviesDimensionSerializer


class MovieDimensionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Moviedimension.objects.all()
    serializer_class = MoviesDimensionSerializer


class MovieCertificationList(generics.ListCreateAPIView):
    queryset = Agecategory.objects.all()
    serializer_class = MoviesCertificationSerializer


class MovieCertificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agecategory.objects.all()
    serializer_class = MoviesCertificationSerializer


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer


class LangMap(generics.ListCreateAPIView):
    queryset = Movielanguagemap.objects.all()
    serializer_class = MovieLangMapSerializer


class CertificationMap(generics.ListCreateAPIView):
    queryset = Moviecertificationmap.objects.all()
    serializer_class = CertificationMapSerializer
