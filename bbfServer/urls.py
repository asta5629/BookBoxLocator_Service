from django.urls import path
from .views import getAllBoxes, getBoxesByZip, getBoxesOnMap, getBoxesNearby, getBoxesByCityState

urlpatterns = [
    path('getAllBoxes/', getAllBoxes, name="getAllBoxes"),
    path('getBoxesByZip', getBoxesByZip, name="getBoxesByZip"),
    path('getBoxesOnMap', getBoxesOnMap, name="getBoxesOnMap"),
    path('getBoxesNearby', getBoxesNearby, name="getBoxesNearby"),
    path('getBoxesByCityAndState', getBoxesByCityState, name="getBoxesByCityAndState")
]