from django.urls import path, include

from watchlist_app.models import Review
from .views import ReviewDetail, ReviewDetailGonchu, ReviewListGonchu, StreamPlatformVSGonchu, movie_detail, movie_list, MovieListAV, MovieDetailAV , StreamPlatformAV, WatchListAV, WatchDetailAV, StreamPlatformDetailAV,ReviewList, ReviewCreate, StreamPlatformVS, UserReview, WatchList
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')
router.register('streamgonchu',StreamPlatformVSGonchu,basename='streamplatformgonchu')

urlpatterns = [
    path('list/',movie_list,name='movie_list'),
    path('list/<int:pk>',movie_detail,name='movie_detail'),
    path('listAV/',MovieListAV.as_view(),name='movie_listAV'),
    path('listAV/<int:pk>',MovieDetailAV
.as_view(),name='movie_detailAV'),
    path('watchAV/',WatchListAV.as_view(),name='movie_listAV'),
    path('watchAV/<int:pk>',WatchDetailAV
.as_view(),name='movie_detailAV'),
    # path('stream/',StreamPlatformAV.as_view(),name='stream'),
    # path('stream/<int:pk>',StreamPlatformDetailAV.as_view(),name='streamplatform-detail'),
    # path('stream/<int:pk>/review',ReviewList.as_view(),name='review-list'),
    # path('stream/review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),
    path('review',ReviewListGonchu.as_view(),name='review-list'),
    path('review/<int:pk>',ReviewDetailGonchu.as_view(),name='review-detail'),
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(), name='review-create'),
    path('reviews/<str:username>/',UserReview.as_view(),name='user-review-detail'),
    path('reviews/',UserReview.as_view(),name='user-review-detailfff'),
    path('new-list/',WatchList.as_view(),name='watch-list'),
    path('',include(router.urls))
]

