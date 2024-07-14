from django.db import models

class Article(models.Model):
    # Atributos de la clase Article
    title = models.CharField(max_length=100)
    content = models.TextField()
    # Otros campos y métodos si es necesario
