from django.shortcuts import render
from search.forms import ModuleForm,ReleaseForm,MetaForm
from django.http import HttpResponse
from search.models import Module,Metamodule,Release

def searchview(request):
     form1 = ReleaseForm(prefix="form1")
     form2 = ModuleForm(prefix="form2")
     form3 = MetaForm(prefix="form3")	
     if request.method == 'GET':
	form1 = ReleaseForm(request.GET, prefix="form1")
	form2 = ModuleForm(request.GET, prefix="form2")
	form3 = MetaForm(request.GET, prefix="form3")	
	if form1.is_valid() and form2.is_valid() and form3.is_valid():
	  release_num = form1.cleaned_data['release_num']
	  metamodule_name = form3.cleaned_data['metamodule_name']
	  module_name = form2.cleaned_data['module_name']
	  results = Module.objects.filter(metamodule__release__number=release_num).filter(metamodule__name=metamodule_name).filter(name=module_name)
	  return render(request,'search/search_result.html',{'form1': form1, 'form2': form2, 'form3': form3, 'results': results})
     else:
	  form1 = ReleaseForm() 
	  form2 = ModuleForm()  
          form3 = MetaForm()   
     return render(request, 'search/search_form.html',{'form1': form1, 'form2': form2, 'form3': form3})