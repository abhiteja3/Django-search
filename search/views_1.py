from django.shortcuts import render
from search.forms import MetamodForm,ReleaseForm,ModuleForm
from django.http import HttpResponse
from search.models import Module,Metamodule,Release

def searchview(request):
     form1 = MetamodForm(prefix="form1")
     form2 = ReleaseForm(prefix="form2")
     form3 = ModuleForm(prefix="form3")
     if request.method == 'GET':
	if 'form1' in request.GET:
	  form1 = MetamodForm(request.GET, prefix="form1")	
	  if form1.is_valid():
	    metamodule_name = form1.cleaned_data['metamodule_name']
	    results = Module.objects.filter(metamodules__name=metamodule_name)
	    return render(request,'search/meta_result.html',{'form1': form1, 'results': results})
	elif 'form2' in request.GET:
	  form2 = ReleaseForm(request.GET, prefix="form2")
	  if form2.is_valid():
    	    release_num = form2.cleaned_data['release_num']
    	    results = Module.objects.filter(metamodules__release__number=release_num)
	    return render(request,'search/rel_result.html',{'form2': form2, 'results': results})
	elif 'form3' in request.GET:
	  form3 = ModuleForm(request.GET, prefix="form3")
	  if form3.is_valid():
	    module_name = form3.cleaned_data['module_name']
	    results = Module.objects.filter(name=module_name)
	    return render(request,'search/test_result.html',{'form3': form3, 'results': results})
     else:
	  form1 = MetamodForm()
	  form2 = ReleaseForm()
	  form3 = ModuleForm() 
     return render(request, 'search/index.html',{'form1': form1, 'form2': form2, 'form3': form3})




def fullview(request):
     form1 = ReleaseForm(prefix="form1")
     form2 = ModuleForm(prefix="form2")
     form3 = MetamodForm(prefix="form3")	
     if request.method == 'GET':
	form1 = ReleaseForm(request.GET, prefix="form1")
	form2 = ModuleForm(request.GET, prefix="form2")
	form3 = MetamodForm(request.GET, prefix="form3")	
	if form1.is_valid() and form2.is_valid() and form3.is_valid():
	  release_num = form1.cleaned_data['release_num']
	  metamodule_name = form3.cleaned_data['metamodule_name']
	  module_name = form2.cleaned_data['module_name']
	  results = Module.objects.filter(metamodules__release__number=release_num).filter(metamodules__name=metamodule_name).filter(name=module_name)
	  return render(request,'search/full_result.html',{'form1': form1, 'form2': form2, 'form3': form3, 'results': results})
     else:
	  form1 = ReleaseForm() 
	  form2 = ModuleForm()  
          form3 = MetamodForm()   
     return render(request, 'search/index2.html',{'form1': form1, 'form2': form2, 'form3': form3})