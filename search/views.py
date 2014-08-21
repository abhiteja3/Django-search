from django.shortcuts import render
from search.forms import MetamodForm,ModuleForm,ReleaseForm,MainForm
from django.http import HttpResponse
from search.models import Module,Metamodule,Release,Moduledep

def searchview(request):
     form1 = MetamodForm(request.GET)
     form2 = ModuleForm(request.GET)
     form3 = ReleaseForm(request.GET)
     if request.method == 'GET':
       if 'form1' in request.GET: 
	form1 = MetamodForm(request.GET)	
	if form1.is_valid():
	  metamodule_name = form1.cleaned_data['metamodule_name']
	  results = Module.objects.filter(metamodules__name=metamodule_name)
	  return render(request,'search/meta_result.html',{'form1': form1, 'results': results})
       elif 'form2' in request.GET: 
	form2 = ModuleForm(request.GET)	
	if form2.is_valid():
	  module_name = form2.cleaned_data['module_name']
	  results = Module.objects.filter(name=module_name)
	  results1 = Moduledep.objects.filter(modulename__name=module_name)
	  return render(request,'search/mod_result.html',{'form2': form2, 'results': results, 'results1': results1})
       elif 'form3' in request.GET: 
	form3 = ReleaseForm(request.GET)	
	if form3.is_valid():
	  release_num = form3.cleaned_data['release_num']
	  results = Module.objects.filter(metamodules__release__number=release_num)
	  return render(request,'search/rel_result.html',{'form3': form3, 'results': results})

     else:
	  form1 = MetamodForm()
          form2 = ModuleForm()
          form3 = ReleaseForm()    
     return render(request, 'search/search_form.html',{'form1': form1, 'form2': form2, 'form3': form3})



def fullview(request):
     if request.method == 'GET':
	form = MainForm(request.GET)	
	if form.is_valid():
	  release_num = form.cleaned_data['release_num']
	  metamodule_name = form.cleaned_data['metamodule_name']
	  module_name = form.cleaned_data['module_name']
	  results = Module.objects.filter(metamodules__release__number=release_num).filter(metamodules__name=metamodule_name).filter(name=module_name)
	  return render(request,'search/search_result.html',{'form': form, 'results': results})
     else:
	  form = MainForm()    
     return render(request, 'search/search_form12.html',{'form': form})