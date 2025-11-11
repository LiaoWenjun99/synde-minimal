from django.shortcuts import render
from django.http import HttpResponse

def chat_home(request):
    return HttpResponse("<h1>SynDe Chat placeholder — coming soon</h1>")

def home_page(request):
    return render(request, 'home/index.html')

def loading_page(request):
    return render(request, 'home/loading.html')

def structure_viewer(request):
    return render(request, 'chat_model/viewer.html')

def model_home(request):
    return render(request, 'home/models_home.html')

def folding_models(request):
    return render(request, 'models/folding_models.html')

def function_models(request):
    return render(request, 'models/function_models.html')

def design_models(request):
    return render(request, 'models/design_models.html')

def visualization_models(request):
    return render(request, 'models/visualization_models.html')