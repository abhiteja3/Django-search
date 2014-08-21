#moduledep:

import csv
from search.models import Moduledep,Module
metadata = csv.reader(open('/root/Django-1.6.5/django/bin/dashboard/source/mod_depen.csv'),delimiter=',')
for row in metadata:
 r = Moduledep(dependent = row[1])
 r.save()
 modulename =  Module.objects.filter(name=row[0]).order_by('-createdate')[:1]
 for module in modulename:
     r.modulename.add(module)

 try:
     r.save()
 except:
     print "there was a problem with line"
