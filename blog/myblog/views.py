from django.shortcuts import redirect, render
from .models import Blog
from django.shortcuts import get_object_or_404
from .forms import CommentForm  


# Create list views.
def blog_list(request):
    posts = Blog.objects.all()  # Récupère tous les articles
    carousel_posts = Blog.objects.all().order_by('-id')[:5]  # Récupère les 5 derniers articles
    
    return render(request, 'list.html', {'posts': posts, 'carousel_posts': carousel_posts})



#Create detail views:
# pk:(primary key) is a common convention in Django that refer to the unique identifier of a model instance.the first post have pk=1, the second post pk=2, and so on.
 
def blog_detail(request, pk):
    posts = get_object_or_404(Blog, pk=pk)  # Récupère l'article par son ID ou renvoie une erreur 404 si non trouvé
    
    # comments:
    comments = posts.comments.all()  # Récupère tous les commentaires associés à l'article
    
    if request.method == 'POST':
        if 'like' in request.POST:
            posts.likes += 1
            posts.save()
            return redirect('detail', pk=pk)
        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.posts = posts  # Associe le commentaire à l'article
                comment.save()
                return redirect('detail', pk=pk)  # Redirige vers la même page après la soumission du commentaire
    else:
        form = CommentForm()
    
    return render(request, 'detail.html', {'posts': posts, 'comments': comments, 'form': form})



# Likes functionality (optional)
def post_like(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.likes += 1
    post.save()
    return redirect('detail', pk=pk)




def search(request):
    query = request.GET.get('q', '')
    if query:
        results = Blog.objects.filter(title__icontains=query)  # Recherche dans les titres des articles
    else:
        results = Blog.objects.none()  # Aucun résultat si la requête est vide
    
    return render(request, 'search.html', {'results': results, 'query': query}  )



#utiliser les modèles Blog et Comment dans vos vues (views.py) pour récupérer des articles et les afficher dans les templates list.html et detail.html.