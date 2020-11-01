from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from call.core.models import Person


def index(request):
    context = {
        'persons': Person.objects.all().order_by('name')
    }
    return render(request, 'core/index.html', context)


@require_POST
def add(request):
    person = Person.objects.create(name=request.POST['name'])
    data = {
        'status': 200,
        'data': person.name
    }
    return JsonResponse(data)


def search(request):
    name = request.GET.get('name', False)
    context = dict(can_add=False, message='Pessoa já existe')
    if name:
        if not Person.objects.filter(name=name).exists():
            context['message'] = 'Pessoa não existe'
            context['can_add'] = True

    return JsonResponse(context)
