from django.db import models

# Create your models here.
class About(models.Model):
    titre = models.CharField(max_length=150)
    publicite = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='image/about')

    date_add = models.DateTimeField( auto_now_add=True)
    date_update = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.titre


class Service(models.Model):
    ICONES = [
        ('flaticon-care','Care'),
        ('flaticon-pigeon','pigeon'),
        ('flaticon-harvest','harvest'),
    ]
    titre = models.CharField(max_length=250)
    description = models.TextField()
    icones = models.CharField(choices = ICONES, max_length=50)

    date_add = models.DateTimeField( auto_now_add=True)
    date_update = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.titre

class Icones(models.Model):
    Icon = [
        ('flaticon-donation-2', 'donation'),
        ('flaticon-world-1', 'world'),
        ('flaticon-blood-2', 'blood'),
    ]
    
    nom = models.CharField(choices=Icon, max_length=50)
    titre = models.CharField(max_length=150)

    date_add = models.DateTimeField( auto_now_add=True)
    date_update = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Icones"
        verbose_name_plural = "Icones"

    def __str__(self):
        return self.nom


class Domaine_don(models.Model):
    icons = [
        ('flaticon-first-aid-kit', 'first-aid-kit'),
        ('flaticon-book', 'book'),
        ('flaticon-shelter', 'shelter')
    ]

    titre = models.CharField(max_length=250)
    description = models.TextField()
    icones = models.CharField(choices=icons, max_length=50)

    date_add = models.DateTimeField( auto_now_add=True)
    date_update = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Domaine_don"
        verbose_name_plural = "Domaine_dons"

    def __str__(self):
        return self.titre


class Objectif(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField()
    
    date_add = models.DateTimeField( auto_now_add=True)
    date_update = models.DateTimeField( auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Objectif"
        verbose_name_plural = "Objectifs"

    def __str__(self):
        return self.titre



    


    