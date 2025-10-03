from django.urls import path
from .views import blog_detail, blog_list


urlpatterns = [
    path('', blog_list, name="list"),  # URL racine de l'app
   path('posts/', blog_detail, name="detail")
]