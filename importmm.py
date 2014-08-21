#metamodule:

import csv
from search.models import Metamodule,Release
metadata = csv.reader(open('/root/Django-1.6.5/django/bin/dashboard/source/meta_jnpr.csv'),delimiter=',')
for row in metadata:
 r = Metamodule(name = row[0],
     version = row[1],
     release = Release.objects.get(number=row[2]),
     owner = row[3],
     createdate = row[4])
 try:
     r.save()
 except:
     print "there was a problem with line"
