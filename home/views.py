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

from django.http import JsonResponse
from .models import Job
from .tasks import run_esmfold_job

def start_esmfold_job(request):
    seq = request.POST.get("sequence")  # or from JSON

    job = Job.objects.create(
        job_type="esmfold",
        input_sequence=seq,
        status="PENDING",
    )

    # Enqueue Celery task
    run_esmfold_job.delay(job.id)

    return JsonResponse({"job_id": job.id, "status": job.status})

from django.shortcuts import get_object_or_404

def job_status(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return JsonResponse(
        {
            "job_id": job.id,
            "status": job.status,
            "result_json": job.result_json,
            "error": job.error_message,
        }
    )
