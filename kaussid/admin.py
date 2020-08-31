from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
# Register your models here.


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('photo_view','lieu','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('lieu',)
    date_hierarchy = 'date_add'
    list_display_links = ['lieu']

    fieldsets = [
          ('Event_infos', {'fields':['lieu','date','projet','photo']}),
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


@admin.register(models.Cause)
class CauseAdmin(admin.ModelAdmin):
    list_display = ('photo_view','titre','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']

    fieldsets = [
          ('Cause_infos', {'fields':['titre','domaine','description','gaol','raised','photo']}),
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


@admin.register(models.Type_don)
class Type_donAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']

    fieldsets = [
          ('Type_don_infos', {'fields':['nom']}),
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



@admin.register(models.Montant)
class MontantAdmin(admin.ModelAdmin):
    list_display = ('prix','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('prix',)
    date_hierarchy = 'date_add'
    list_display_links = ['prix']

    fieldsets = [
          ('Montant_infos', {'fields':['prix','other_amount']}),
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


@admin.register(models.Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ('nom','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('nom',)
    date_hierarchy = 'date_add'
    list_display_links = ['nom']

    fieldsets = [
          ('Organizer_infos', {'fields':['nom','lieu','biograpie']}),
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


@admin.register(models.Donate)
class DonateAdmin(admin.ModelAdmin):
    list_display = ('titre','type_don','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('titre',)
    date_hierarchy = 'date_add'
    list_display_links = ['titre']

    fieldsets = [
          ('Donate_infos', {'fields':['titre','montant_don','organizer']}),
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


@admin.register(models.Personal_name)
class DonateAdmin(admin.ModelAdmin):
    list_display = ('name','email','date_add','date_update','status')
    list_filter = ('date_add','date_update','status')
    search_fields = ('name',)
    date_hierarchy = 'date_add'
    list_display_links = ['name']

    fieldsets = [
          ('Donate_infos', {'fields':['name','email','phone','country','adresse']}),
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

