from django.urls import path
from .views import zone_list

from .views import main
from .views import zone_delete
from .views import create

urlpatterns = [
    path('list/', zone_list, name="zone_list"),
    path('delete/<int:id>/', zone_delete, name="zone_delete"),
    path('create/', create, name="create"),
    path('', main, name="main"),
    #path('main/<int:id>/', main, name="main"),
]

