from check import views as v
from django.urls import path


urlpatterns = [   
    path('tag', v.TagList, name='tag'),
]


