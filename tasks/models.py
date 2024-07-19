from django.db import models

# Create your models here.
class task (models.model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def _start_(self):
        return self.title