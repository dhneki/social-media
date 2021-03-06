from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns =[
    path('profiles/',ProfileListCreateApiView.as_view(),name='profile_liste_create'),
    path('profiles/<int:pk>/',profile_page,name='profile_rud'),
    path('publications/',PublicationListCreateApiView.as_view(),name='publication_liste_create'),
    path('publications/<int:pk>/',PublicationRetrieveUpdateDestroyApiView.as_view(),name='publication_rud'),
    path('comments/',CommentListCreateApiView.as_view(),name='comment_liste_create'),
    path('comments/<int:pk>/',CommentRetrieveUpdateDestroyApiView.as_view(),name='comment_rud'),
    path('likes/',LikeDislikeApiView.as_view(),name='like_liste_create'),
    path('follows/',FollowApiView.as_view(),name='follow_liste_create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('home/<int:pk>',home_api),
    path('invitations/<int:pk>/',invitations_api),
    path('notifications/<int:pk>/',notification_api)
]