from django.db import models

# Create your models here.
class Event(models.Model):
    photo = models.ImageField(upload_to='photo/events')
    projet = models.CharField(max_length=150)
    lieu = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=False)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __str__(self):
        return self.lieu


class Cause(models.Model):
    photo = models.ImageField(upload_to='photo/Causes')
    titre = models.CharField(max_length=150)
    domaine = models.CharField(max_length=250)
    description = models.TextField()
    gaol = models.CharField(max_length=50)
    raised = models.CharField(max_length=50)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Cause"
        verbose_name_plural = "Causes"

    def __str__(self):
        return self.titre

class Type_don(models.Model):
    nom = models.CharField(max_length=150)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )    

    class Meta:
        verbose_name = "Type_don"
        verbose_name_plural = "Type_dons"

    def __str__(self):
        return self.nom


class Montant(models.Model):
    prix = models.CharField(max_length=50)
    other_amount = models.CharField(max_length=250)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Montant"
        verbose_name_plural = "Montants"

    def __str__(self):
        return self.prix

class Organizer(models.Model):
    nom = models.CharField(max_length=250)
    lieu = models.CharField(max_length=150)
    biograpie = models.TextField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Organizer"
        verbose_name_plural = "Organizers"

    def __str__(self):
        return self.nom

class Donate(models.Model):
    titre = models.CharField(max_length=150)
    type_don = models.ForeignKey(Type_don, related_name='type_don_donate', on_delete=models.CASCADE)
    montant_don = models.ForeignKey(Montant, related_name='montant_donate', on_delete=models.CASCADE)
    organizer = models.ForeignKey(Organizer, related_name='organizer_donate', on_delete=models.CASCADE)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Donate"
        verbose_name_plural ="Donates"

    def __str__(self):
        return self.titre

class Personal_name(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=150)
    country = models.CharField(max_length=250)
    adresse = models.CharField(max_length=250)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )    

    class Meta:
        verbose_name = "Personal_name"
        verbose_name_plural = "Personal_names"

    def __str__(self):
        return self.name

   




