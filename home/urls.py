from django.urls import path
from .views import home_page, loading_page, model_home, folding_models, function_models, design_models, visualization_models

# urlpatterns = [
#     path('', loading_page, name='loading'),
#     path('home/', home_page, name='home'),  # Redirect here after loading
#     path('models/', model_home, name='models_home'),
#     path('models/folding/', folding_models, name='folding_models'),
#     path('models/function/', function_models, name='function_models'),
#     path('models/design/', design_models, name='design_models'),
#     path('models/visualization/', visualization_models, name='visualization_models'),
# ]

from django.urls import path
from .views import home_page, loading_page, model_home, chat_home

urlpatterns = [
    path('', loading_page, name='loading'),
    path('home/', home_page, name='home'),
    path('models/', model_home, name='models_home'),
    path('chat/', chat_home, name='chat_home'),  # ✅ placeholder
]
