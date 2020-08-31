from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Siteinfo(models.Model):
    telephone = models.CharField(max_length=50)
    couriel = models.EmailField(max_length=254)
    copyrights = models.CharField(max_length=80)
    adresse = models.CharField(max_length=200)
    slogan = models.CharField(max_length=200)
    logo_slogan = models.ImageField(upload_to='imageSlogan/siteinfo')
    image_don = models.ImageField(upload_to='imagedon/siteinfo')
    message_join_volunteers = models.TextField()
    logo = models.ImageField(upload_to='logo/siteinfo', null=True)
    logo_footer = models.ImageField(upload_to='logo_footer/siteinfo', null=True)
    background_about = models.ImageField(upload_to='background/about')
    background_blog = models.ImageField(upload_to='background/blog')
    background_blogSingle = models.ImageField(upload_to='background/blog-single')
    background_causes = models.ImageField(upload_to='background/causes')
    background_causeSingle = models.ImageField(upload_to='background/cause-single')
    background_contact = models.ImageField(upload_to='background/contact')
    background_donate = models.ImageField(upload_to='background/donate')
    background_events = models.ImageField(upload_to='background/events')
    background_faq = models.ImageField(upload_to='background/faq')
    background_index = models.ImageField(upload_to='background/index')
    background_volunteers = models.ImageField(upload_to='background/volunteers')
    background_footer = models.ImageField(upload_to='background/footer')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Siteinfo"
        verbose_name_plural = "Siteinfos"

    def __str__(self):
        return self.telephone

class Carousel(models.Model):
    titre = models.CharField(max_length=150)
    image = models.ImageField( upload_to='image/carousel')

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )
    class Meta:
        verbose_name = "Carousel"
        verbose_name_plural = "Carousels"

    def __str__(self):
        return str(self.titre)

class Newletter(models.Model):
    email = models.EmailField(max_length=254)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Newletter"
        verbose_name_plural = "Newletters"

    def __str__(self):
        return str(self.email)

class ReseauSociau(models.Model):
    icon = [
        ('fab fa-facebook-f', 'facebook'),
        ('fab fa-twitter', 'twitter'),
        ('fab fa-vimeo-v', 'vimeo'),
        ('fab fa-instagram', 'instagram'),
        ('fab fa-youtube', 'youtube'),

    ]
    nom = models.CharField(max_length=70)
    lien = models.URLField(max_length=200)
    icones = models.CharField(choices=icon, max_length=50)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "ReseauSociau"
        verbose_name_plural = "ReseauSociaux"

    def __str__(self):
        return self.icones

class Lieu(models.Model):
    pays = models.CharField(max_length=250)
    email= models.EmailField(max_length=254)
    phone = models.CharField(max_length=250)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name =  "Lieu"
        verbose_name_plural = "Lieux"

    def __str__(self):
        return self.pays

    

class Contact(models.Model):
    titre = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    message = models.TextField()
    image = models.ImageField(upload_to='image/contact')
    ICONES = [
        ('icon-1 paroller', 'paroller-1'),
        ('icon-2 paroller', 'paroller-2')
    ]
    nom = models.CharField(choices = ICONES, max_length=250)
    lieu = models.ForeignKey('Lieu', related_name='lieu_contact', on_delete=models.CASCADE)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.titre

class Information(models.Model):
    nom = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=50)
    helps = models.CharField(max_length=250)
    message = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Information"
        verbose_name_plural =   "Informations"

    def __str__(self):
        return self.nom

class Need_help(models.Model):
    titre = models.CharField(max_length=250)
    adresse = models.CharField(max_length=250)
    lien_video = models.URLField(max_length=200)
    proposition = models.CharField( max_length=50)
    description = models.TextField()

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Need_help"
        verbose_name_plural = "Need_helps"

    def __str__(self):
        return self.titre

class Fundrising(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField()
    
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Fundrising"
        verbose_name_plural = "Fundrisings"

    def __str__(self):
        return self.titre

class Temoignage(models.Model):
    message = models.TextField()
    nom = models.CharField(max_length=250)   
    fonction = models.CharField(max_length=150) 

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )
    class Meta:
        verbose_name = "Temoignage"
        verbose_name_plural = "Temoignages"

    def __str__(self):
        return self.nom

class PaymentAmount(models.Model):
    card_number = models.CharField(max_length=150)
    expery = models.CharField(max_length=150)
    cvc = models.CharField(max_length=250)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "PaymentAmount"
        verbose_name_plural = "PaymentAmounts"

    def __str__(self):
        return self.card_number

class Adopt(models.Model):
    photo = models.ImageField(upload_to='photo/adopt') 
    titre = models.CharField(max_length=250)
    description = models.TextField()
    name = models.CharField(max_length=250)
    ages = models.CharField(max_length=50)
    races = models.CharField(max_length=150)
    gender = models.CharField(max_length=90)
    lien_story = models.URLField(max_length=200)


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Adopt"
        verbose_name_plural = "Adopts"

    def __str__(self):
        return self.titre

class Utilisateur(models.Model):
    photo = models.ImageField(upload_to='image/utilisateur')
    user = models.ForeignKey(User, related_name='userprofile', on_delete=models.CASCADE)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True )

    class Meta:
        verbose_name = "Utilisateur"
        verbose_name_plural = "Utilisateurs"

    def __str__(self):
        return str(self.photo)

