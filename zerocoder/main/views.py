from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
        'caption': "Графики и диаграммы",
        }
    return render(request, 'main/index.html', context=data) #, context:{'caption':"График"})

def page2(request):
    return render(request, 'main/page2.html', context={'caption':"Линейные графики"})

def page3(request):
    return render(request, 'main/page3.html', context={'caption':"Столбчатые диаграммы"})

def page4(request):
    return render(request, 'main/page4.html', context={'caption':"Круговые диаграммы"})
def page5(request):
    return render(request, 'main/page5.html', context={'caption':"Гистограммы"})
def page6(request):
    return render(request, 'main/page6.html', context={'caption':"Точечные графики"})
def page7(request):
    return render(request, 'main/page7.html', context={'caption':"Пузырьковые графики"})
def page8(request):
    return render(request, 'main/page8.html', context={'caption':"Диаграммы потока"})