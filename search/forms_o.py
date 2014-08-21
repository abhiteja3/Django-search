from django import forms
from search.models import Module,Release,Metamodule

class ReleaseForm(forms.Form):
     release_num = forms.ModelChoiceField(queryset=Release.objects.all(),empty_label='Pick a Release',required=False)
     
     def clean_release_number(self):
       try:
          release_num = int(self.cleaned_data["release_num"])
                    
       except:
          release_num = None

       if release_num and Module.objects.exclude(metamodule__release__number=release_num).exists():
           raise forms.ValidationError("Please enter a valid release number")
       else:
	   return release_num  



class ModuleForm(forms.Form):
     module_name = forms.ModelChoiceField(queryset=Module.objects.all(),empty_label='Pick a Module')
     
     def clean_release_number(self):
       try:
          module_name = int(self.cleaned_data["module_name"])
	  
       except:
          module_name = None

       if module_name and Module.objects.exclude(name=module_name).exists():
           raise forms.ValidationError("Please enter a valid module name")
       else:
	   return module_name   


class MetamoduleForm(forms.Form):
     metamodule_name = forms.ModelChoiceField(queryset=Metamodule.objects.all(),empty_label='Pick a Meta module')

     def clean_metamodule_name(self):
       try:
          metamodule_name = int(self.cleaned_data["metamodule_name"])
       except:
          metamodule_name = None
	 
       if metamodule_name and Module.objects.exclude(metamodule__name=metamodule_name).exists():
           raise forms.ValidationError("Please enter a valid metamodule name")
       else:
	   return metamodule_name          
     