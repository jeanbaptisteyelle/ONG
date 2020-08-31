from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categorie(models.Model):
    nom = models.CharField(max_length=250)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Categorie"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.nom

class Tags(models.Model):
    nom = models.CharField(max_length=250)
    lien = models.CharField(max_length=150)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Tags"
        verbose_name_plural = "Tagss"

    def __str__(self):
        return self.nom


class Beneficiaire(models.Model):
    titre = models.CharField(max_length=150)
    image = models.ImageField(upload_to='image/beneficiaire')
    description = models.TextField()
    categorie = models.ForeignKey(Categorie, related_name='categorie_beneficiaire', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Beneficiaire"
        verbose_name_plural = "Beneficiaires"

    def __str__(self):
        return self.titre

class Like(models.Model):
    item = models.ForeignKey('Beneficiaire', related_name='item_like', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_like', on_delete=models.CASCADE)
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"

    def __str__(self):
        return str(self.item)


class Volunteers(models.Model):
    image = models.ImageField(upload_to='image/volunteers')
    nom = models.CharField(max_length=250)
    fonction = models.CharField(max_length=250)
    montant = models.CharField(max_length=50)
    type_don = models.CharField(max_length=250)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Volunteers"
        verbose_name_plural = "Volunteerss"

    def __str__(self):
        return self.nom

class Faq(models.Model):
    titre = models.CharField(max_length=250)
    lien = models.CharField(max_length=250)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Faq"
        verbose_name_plural = "Faqs"

    def __str__(self):
        return self.titre
