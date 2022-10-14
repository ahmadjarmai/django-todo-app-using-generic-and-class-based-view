from django.db import models

class Article(models.Model) :
    name =models.CharField(max_length=200)
    title =models.CharField(max_length=200)
    body =models.TextField()
    created =models.DateTimeField(auto_now_add=True)

    class Meta :
        ordering =['-name']

    def __str__(self) :
        return self.title
