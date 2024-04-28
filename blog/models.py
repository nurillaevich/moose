from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=212)
    image = models.ImageField(auto_created='author', null=True, blank=True)
    profession = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tage(models.Model):
    name = models.CharField(max_length=212)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    image = models.ImageField('articles', null=True, blank=True)
    title = models.CharField(max_length=212)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tage, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=212)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    title = models.CharField(max_length=212)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=212)
    email = models.EmailField(null=True, blank=True)
    subject = models.TextField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
