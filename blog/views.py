from django.shortcuts import render
from .models import Article  # Asegúrate de importar los modelos necesarios

def article_list(request):
    articles = Article.objects.all()  # Ejemplo de obtención de artículos desde el modelo
    return render(request, 'articles.html', {'articles': articles})
