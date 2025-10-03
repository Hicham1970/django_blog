from django.shortcuts import render
from .models import Blog


# Create your views here.
def blog_list(request):
    posts = Blog.objects.all()  # Récupère tous les articles
    carousel_posts = Blog.objects.all().order_by('-id')[:5]  # Récupère les 5 derniers articles
    
    return render(request, 'list.html', {'posts': posts, 'carousel_posts': carousel_posts})




def blog_detail(request):
    return render(request, 'detail.html')


#utiliser les modèles Blog et Comment dans vos vues (views.py) pour récupérer des articles et les afficher dans les templates list.html et detail.html.