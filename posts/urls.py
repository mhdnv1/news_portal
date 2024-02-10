from django.urls import path
from .views import *

urlpatterns = [
    path('', index , name='index'),
    path('category/<int:category_id>/', get_category , name='category'),
    path('add_news/'  , add_news , name='add_news'),
    path('register/' , register , name="register"),
    path('login/' , userLogin , name="login"),
    path('logout/', userClose, name='logout'),
    path('news/<int:id>' , getIdNews , name="get_id_news"),
    path('news/delete/<int:id>', delete_news , name='delete_news')
]
