from django.urls import path
from .views import blog_detail, blog_list, post_like   , search

urlpatterns = [
    path('', blog_list, name="list"),  # URL racine de l'app
   path('posts/<int:pk>', blog_detail, name="detail") ,  # Détail d'un article par son ID
   path('like_posts/<int:pk>/', post_like, name='like'), # URL pour liker un post
    path('post/search_results', search, name='search'),  # URL pour la recherche 
]

# Note: Assurez-vous que les noms des vues importées correspondent aux noms des fonctions dans views.py 
# Note: Le nom 'like' dans le path doit correspondre au nom utilisé dans les templates pour le lien de like.
# Note: Le nom 'detail' dans le path doit correspondre au nom utilisé dans les vues pour la redirection après la soumission du commentaire.     