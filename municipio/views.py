from .models import Region, Municipio
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from .forms import MunicipioForm, RegionForm

# Create your views here.
def municipio_view(request):
    #cod = Municipio.Maquina.objects.get(id=pk)
    muns = Municipio.objects.all()
    regs = Region.objects.all()
    context = {
        "muns": muns,
        "regs": regs,
    }
    return render (request, 'municipio.html', context)


def municipio_new(request):
    if request.method == "POST":
        form = MunicipioForm(request.POST)
        if form.is_valid():
            muni = form.save(commit=False)
            muni.save()
            return redirect('municipio:municipio_view')
    else:
        form = MunicipioForm()
    return render(request, 'municipio_edit.html', {'form': form})

def region_new(request):
    if request.method == "POST":
        form = RegionForm(request.POST)
        if form.is_valid():
            muni = form.save(commit=False)
            muni.save()
            return redirect('municipio:municipio_view')
    else:
        form = RegionForm()
    return render(request, 'municipio_edit.html', {'form': form})
 

def municipio_detail(request, pk):
    mun = get_object_or_404(Municipio, pk=pk)
    #return redirect('municipio_detail', pk=mun.pk)                

    context = {
    'mun': mun,
    }    
    return render(request, 'municipio_detail.html', context)  
###
def region_detail(request, pk):
    reg = get_object_or_404(Region, pk=pk)          
    context = {
    'reg': reg,
    }    
    return render(request, 'region_detail.html', context)  
###

def municipio_edit(request, pk):
    mun = get_object_or_404(Municipio, pk=pk)
    if request.method == "POST":
        form = MunicipioForm(request.POST, instance=mun)
        if form.is_valid():
            mun = form.save(commit=False)
            mun.save()
            return redirect('municipio:municipio_detail', pk=mun.pk)
        else:
             form = MunicipioForm(instance=mun)
             context = {
                'form': form,
            }    
        return redirect(request, 'municipio_edit.html', context)    
    else:
        return redirect('municipio:municipio_view')



def municipio_delete(request,pk):            
    mun = get_object_or_404(Municipio, pk=pk)
    mun.delete()
    return redirect('municipio:municipio_view')


###
def region_delete(request,pk):            
    reg = get_object_or_404(Region, pk=pk)
    reg.delete()
    return redirect('municipio:municipio_view')    
###  

def region_edit(request, pk):
    reg = get_object_or_404(Region, pk=pk)
    if request.method == "POST":
        form = RegionForm(request.POST, instance=reg)
        if form.is_valid():
            reg = form.save(commit=False)
            reg.save()
            return redirect('region_detail', pk=reg.pk)
        else:
             form = MunicipioForm(instance=reg)
             context = {
                'form': form,
            }    
        return render(request, 'region_edit.html', context)    
    else:
        return redirect('municipio:municipio_view')  
