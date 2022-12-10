from django.shortcuts import render, redirect
from .models import Job
from .forms import JobForm

# подключение хтмл страниц


def index(request):
    # jobs = Job.objects.all()
    jobs = Job.objects.order_by('-id')

    return render(request, 'main/index.html', {'title': 'Job vacancies', 'jobs': jobs})


def about(request):
    return render(request, 'main/about.html')


def view(request, pk):
    # error = ''
    job = Job.objects.get(id=pk)

    # form = JobForm(instance=job)

    # form = JobForm(request.POST, instance=job)

    context = {
        'job': job
    }

    return render(request, 'main/viewJob.html', context)


def create(request):
    error = ''

    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Oops... Something went wrong!"

    form = JobForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/createJob.html', context)


def update(request, pk):
    error = ''
    job = Job.objects.get(id=pk)

    form = JobForm(instance=job)

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Oops... Something went wrong!"

    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/updateJob.html', context)


def delete(request, pk):
    job = Job.objects.get(id=pk)

    if request.method == 'POST':
        job.delete()
        return redirect('home')

    context = {
        'job': job
    }

    return render(request, 'main/deleteJob.html', context)
