from django.contrib import admin
from dogs.models import Dog, Breed


# Register your models here.


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ['name', 'breed', 'birth_date']
    list_filter = ['breed']
