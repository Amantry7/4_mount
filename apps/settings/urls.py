from django.urls import path
from apps.settings.views import *
urlpatterns = [
    path('', index,name='index'),
    path('about/', index1, name='index1'),
    path('blog/', index2, name='index2'  ),
    path('index/', index3, name='index3' )
    
]
