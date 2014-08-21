from django import forms
from search.models import Module,Release,Metamodule

class MetaForm(forms.Form):
     meta_name = forms.ModelChoiceField(queryset=Metamodule.objects.all(),empty_label='Pick a Meta module')
          
     def clean_meta_name(self):
       try:
          meta_name = int(self.cleaned_data["meta_name"])
       except:
          meta_name = None
	 
       if meta_name and Module.objects.exclude(metamodule__name=meta_name).exists():
           raise forms.ValidationError("Please enter a valid metamodule name.")
       else:
	   return meta_name          