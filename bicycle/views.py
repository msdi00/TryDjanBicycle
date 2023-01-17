from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
# Create your views here.


bike_description = {
    'mount': 'Широкий протектор, неплохая амортизация',
    'gravel': 'Лучшая амортизация',
    'folding': 'Удобны при транспортировке',
    'fatbikes': 'При езде по полям и пескам',
    'racing': 'Тонкая резина, менее управляемый',
    'urban': 'Универсальный байк',
}

views_bike = {
        'mount': 'Горные',
        'gravel': 'Гравийные',
        'folding': 'Складные',
        'fatbikes': 'Фэтбайки',
        'racing': 'Гоночные',
        'urban': 'Городские',
    }

def get_bicycle(request):
    context = {
        'bikes': views_bike,
    }
    return render(request, 'bicycle/bicycle.html', context=context)


def get_description(request, model: str):
    context = {
        'model_descr': bike_description[model],
        'name_mod': views_bike[model],
    }
    return render(request, 'bicycle/description.html', context=context)
