from django.shortcuts import render
from search.forms import ModuleForm,ReleaseForm,MetaForm
from django.http import HttpResponse
from search.models import Module,Metamodule,Release

def searchview(request):
     form1 = ModuleForm(prefix="form1")
     form2 = MetaForm(prefix="form3")
     if request.method == 'GET':
	if 'form1' in request.GET:
	  form1 = ModuleForm(request.GET, prefix="form1")
	  if form1.is_valid():
	    module_name = form1.cleaned_data['module_name']
	    results = Module.objects.filter(name=module_name)
	    return render(request,'search/search_result.html',{'form1': form1, 'results': results})
	elif 'form2' in request.GET:
	  form2 = MetaForm(request.GET, prefix="form3")
	  if form2.is_valid():
    	    metamodule_name = form2.cleaned_data['metamodule_name']
    	    results = Module.objects.filter(metamodule__name=metamodule_name)
	    return render(request,'search/meta_result.html',{'form2': form2, 'results': results})

     else:
	  form1 = ModuleForm() 
	  form2 = MetaForm() 
     return render(request, 'search/search_form.html',{'form1': form1, 'form2': form2,})