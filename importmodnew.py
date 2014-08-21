#module:

import csv

# import the relevant model
from search.models import Module,Metamodule

#fields = ['modulename','description','moduleversion','metamodule','metamoduleversion','release','recordcreated','createdby'] 
masterdata = csv.reader(open('/root/Django-1.6.5/django/bin/dashboard/source/modulenew.csv'),delimiter=',')
#loop:
for row in masterdata:
 p = Module(name = row[0],
     version = row[1],
     description = row[2],
     createdate = row[4],
     manager = row[5],
     owner = row[6])
 p.save()
 metamodules =  Metamodule.objects.filter(name=row[3]).order_by('-createdate')[:1]
 for metamodule in metamodules:
     p.metamodules.add(metamodule)
 try:
     p.save()
 except:
     print "there was a problem with line", i 

