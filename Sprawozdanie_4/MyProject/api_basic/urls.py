from django.urls import path
from .views import Game_list, Game_detail, GameAPIView, GameDetails, GenericAPIView

urlpatterns = [
    #path('Game/', Game_list),
    path('Game/', GameAPIView.as_view()),
    #path('detail/<int:pk>/', Game_detail)
    path('detail/<int:id>/', GameDetails.as_view()),
    path('generic/Game/<int:id>/', GenericAPIView.as_view()),
]
