from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404


# Create list views.
def blog_list(request):
    posts = Blog.objects.all()  # Récupère tous les articles
    carousel_posts = Blog.objects.all().order_by('-id')[:5]  # Récupère les 5 derniers articles
    
    return render(request, 'list.html', {'posts': posts, 'carousel_posts': carousel_posts})



#Create detail views:
# pk:(primary key) is a common convention in Django that refer to the unique identifier of a model instance.the first post have pk=1, the second post pk=2, and so on.
 
def blog_detail(request, pk):
    posts = get_object_or_404(Blog, pk=pk)  # Récupère l'article par son ID ou renvoie une erreur 404 si non trouvé
    
    return render(request, 'detail.html', {'posts': posts})




#utiliser les modèles Blog et Comment dans vos vues (views.py) pour récupérer des articles et les afficher dans les templates list.html et detail.html.