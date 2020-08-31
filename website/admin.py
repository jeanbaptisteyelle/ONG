from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(models.Siteinfo)
class SiteinfoAdmin(admin.ModelAdmin):
    list_display = ('slogan','couriel','date_add','date_update','status','logo_view','logo_footer_view','image_don_view','logo_slogan_view','background_about_view','background_blog_view','background_blogSingle_view','background_causes_view','background_causeSingle_view','background_contact_view','background_donate_view','background_events_view','background_faq_view','background_index_view','background_volunteers_view','background_footer_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('slogan',)
    date_hierarchy = 'date_add'
    list_display_links = ['slogan']
    fieldsets = [
          ('Siteinfo', {'fields':['telephone','couriel','copyrights','adresse','slogan','logo','logo_footer','logo_slogan','image_don','message_join_volunteers','background_about','background_blog','background_blogSingle','background_causes','background_causeSingle','background_contact','background_donate','background_events','background_faq','background_index','background_volunteers','background_footer']}),
          ('standard', {'fields':['status']}),
          ]


    def logo_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo.url))
    
    def logo_footer_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo_footer.url))
    

    def logo_slogan_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.logo_slogan.url))
    
    def image_don_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image_don.url))

    def background_about_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.background_about.url))

    def background_blog_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.background_blog.url))
    
    def background_blogSingle_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.background_blogSingle.url))

    def background_causes_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.background_causes.url))

    def background_causeSingle_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.background_causeSingle.url))

    def background_contact_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.background_contact.url))

    def background_donate_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.background_donate.url))

    def background_events_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.background_events.url))

    def background_faq_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.background_faq.url))

    def background_index_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.background_index.url))

    def background_volunteers_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.background_volunteers.url))

    def background_footer_view(self,obj):
        return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.background_footer.url))


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('titre','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
          ('Carousel_infos', {'fields':['titre','image_view']}),
          ('standards', {'fields':['status']}),
          ]

    def image_view(self,obj):
            return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'


@admin.register(models.Newletter)
class NewletterAdmin(admin.ModelAdmin):
    list_display = ('email','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('email',)
    date_hierarchy = 'date_add'
    list_display_links = ['email']
    fieldsets = [
          ('Newletter_infos', {'fields':['email']}),
          ('standards', {'fields':['status']}),
          ]

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'


@admin.register(models.ReseauSociau)
class ReseauSociauAdmin(admin.ModelAdmin):
    list_display = ('nom','lien','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('ReseauSociau_infos', {'fields':['nom','lien','icones',]}),
          ('standards', {'fields':['status']}),
          ]

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'


@admin.register(models.Lieu)
class LieuAdmin(admin.ModelAdmin):
    list_display = ('pays','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('pays',)
    date_hierarchy = 'date_add'
    list_display_links = ['pays']
    fieldsets = [
          ('Lieu_infos', {'fields':['pays','email','phone',]}),
          ('standards', {'fields':['status']}),
          ]

    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('titre','description','message','date_add','date_update','status','image_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
          ('Contact_infos', {'fields':['titre','description','message','nom','lieu','image_view']}),
          ('standards', {'fields':['status']}),
          ]

    def image_view(self,obj):
            return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.image.url))


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('nom','email','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Information_infos', {'fields':['nom','email','telephone','helps','message']}),
          ('standards', {'fields':['status']}),
          ]


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'


@admin.register(models.Need_help)
class Need_helpAdmin(admin.ModelAdmin):
    list_display = ('titre','adresse','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
          ('Need_help_infos', {'fields':['titre','adresse','lien_video','proposition','description']}),
          ('standards', {'fields':['status']}),
          ]


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'


@admin.register(models.Fundrising)
class FundrisingAdmin(admin.ModelAdmin):
    list_display = ('titre','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
          ('Fundrising_infos', {'fields':['titre','description']}),
          ('standards', {'fields':['status']}),
          ]


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'


@admin.register(models.Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    fieldsets = [
          ('Temoignage_infos', {'fields':['nom','message','fonction']}),
          ('standards', {'fields':['status']}),
          ]


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.PaymentAmount)
class PaymentAmountAdmin(admin.ModelAdmin):
    list_display = ('card_number','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('card_number',)
    date_hierarchy = 'date_add'
    list_display_links = ['card_number']
    fieldsets = [
          ('PaymentAmount_infos', {'fields':['card_number','expery','cvc']}),
          ('standards', {'fields':['status']}),
          ]


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

@admin.register(models.Adopt)
class AdoptAdmin(admin.ModelAdmin):
    list_display = ('titre','date_add','date_update','status','photo_view')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']
    fieldsets = [
          ('Adopt_infos', {'fields':['titre','description','name','ages','races','gender','lien_story','photo']}),
          ('standards', {'fields':['status']}),
          ]

    def photo_view(self,obj):
            return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.photo.url))


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'


@admin.register(models.Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('photo_view','date_add','date_update','status')
    list_filter = ('date_add','date_update','status','user')
    search_fields = ('user',)
    date_hierarchy = 'date_add'
    fieldsets = [
          ('Utilisateur_infos', {'fields':['user','photo']}),
          ('standards', {'fields':['status']}),
          ]

    def photo_view(self,obj):
            return mark_safe("<img src='{url}' width='100px',height='50px'>".format(url=obj.photo.url))


    actions = ('active','desactive')
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'La selection a été activé avec succès')
    active.short_description = 'activer'
        
    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'La selection a été desactivé avec succès')
    desactive.short_description = 'desactiver'

