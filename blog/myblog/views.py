from django.shortcuts import render
# from django.http import FileResponse
# from django.conf import settings
# import os

# Create your views here.
def home(request):
    return render(request, 'home.html')



# def serve_static_file(request, filename):
#     file_path = os.path.join(settings.STATIC_ROOT, 'myblog', filename)
#     if os.path.exists(file_path):
#         return FileResponse(open(file_path, 'rb'))
#     else:
#         from django.http import HttpResponse
#         return HttpResponse('Fichier non trouvé', status=404)