from django.urls import path
from .views import MovieList, MovieDetail, MovieLanguageList, \
    MovieLangDetail, MovieGenreList, MovieGenreDetail, \
    MovieDimensionList, MovieDimensionDetail, \
    MovieCertificationList, MovieCertificationDetail, \
    ActorList, ActorDetail, LangMap

urlpatterns = [
    path('movies/', MovieList.as_view()),
    path('movies/<int:pk>/', MovieDetail.as_view()),

    path('movie-language/', MovieLanguageList.as_view()),
    path('movie-language/<int:pk>/', MovieLangDetail.as_view()),

    path('movie-genre/', MovieGenreList.as_view()),
    path('movie-genre/<int:pk>/', MovieGenreDetail.as_view()),

    path('movie-dimension/', MovieDimensionList.as_view()),
    path('movie-dimension/<int:pk>/', MovieDimensionDetail.as_view()),

    path('movie-certification/', MovieCertificationList.as_view()),
    path('movie-certification/<int:pk>/', MovieCertificationDetail.as_view()),

    path('actor/', ActorList.as_view()),
    path('actor/<int:pk>/', ActorDetail.as_view()),

    path('language-map/', LangMap.as_view()),


]
