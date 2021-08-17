from django.shortcuts import render,redirect
from .models import Data

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date_of_birth = request.POST['dob']
        description = request.POST['description']
        job = request.POST['job']
        degree = request.POST['degree']
        dod = request.POST['dod']
        experience = request.POST['job_experience']
        YoE = request.POST['YoE']
        jd = request.POST['jd']

        new = Data(name=name, email=email, phone=phone, date_of_birth=date_of_birth, description=description, job=job, degree=degree, dod=dod, experience=experience, YoE=YoE, job_desc=jd)
        new.save()
        return redirect('/')

    else:
        record = Data.objects.all()
        return render(request, 'home.html', {'records': record})
