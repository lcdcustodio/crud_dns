from django.urls import path
from .views import zone_list
from .views import zone_new
from .views import main
from .views import zone_delete

from .views import create

urlpatterns = [
    path('list/', zone_list, name="zone_list"),
    path('new/', zone_new, name="zone_new"),
    #path('main/', main, name="main"),
    path('delete/<int:id>/', zone_delete, name="zone_delete"),
    path('create/', create, name="create"),
    path('', main, name="main"),
]

