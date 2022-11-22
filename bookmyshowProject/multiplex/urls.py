from django.urls import path
from .views import CountryList, CountryDetail, StateList, StateDetail, CityList, CityDetail


urlpatterns = [
    path('country/', CountryList.as_view()),
    path('country/<int:pk>/', CountryDetail.as_view()),

    path('state/', StateList.as_view(), name='get_all_states'),
    path('state/<int:pk>/', StateDetail.as_view(),
         name='get_delete_update_state'),

    path('city/', CityList.as_view()),
    path('city/<int:pk>/', CityDetail.as_view())

    # path('movie-genre/', MovieGenreList.as_view()),
    # path('movie-genre/<int:pk>/', MovieGenreDetail.as_view()),

    # path('movie-dimension/', MovieDimensionList.as_view()),
    # path('movie-dimension/<int:pk>/', MovieDimensionDetail.as_view()),

    # path('movie-certification/', MovieCertificationList.as_view()),
    # path('movie-certification/<int:pk>/', MovieCertificationDetail.as_view()),


]
