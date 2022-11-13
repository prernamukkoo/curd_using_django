from django.shortcuts import render
from .models import Info
from .form import InfoForm

# Create your views here.
def index(request):
    template = 'application/index.html'
    data = Info.objects.all()
    context = {
        'form':InfoForm,
        'data':data
    }
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context.update({
                'error': form.errors
            })    
    return render(request,template,context)
