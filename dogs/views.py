from django.shortcuts import render
from dogs.models import Breed, Dog


def index(request):
    context = {
        "object_list": Breed.objects.all(),  # "object_list": Breed.objects.all()[:2],
        'title': "Питомник - Главная"
    }
    return render(request, 'dogs/index.html', context)


def breed(request):
    context = {
        "object_list": Breed.objects.all(),  # "object_list": Breed.objects.all()[:2],
        'title': "Питомник - Все породы"
    }
    return render(request, 'dogs/breed.html', context)


def dogs_breed(request, pk):
    breed_item = Breed.objects.get(pk=pk)

    context = {
        "object_list": Dog.objects.filter(breed_id=pk),  # "object_list": Breed.objects.all()[:2],
        'title': f"Собаки породы - {breed_item.name}"
    }
    return render(request, 'dogs/dogs.html', context)
