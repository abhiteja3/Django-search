# open file & create csvreader


#release:

import csv
from search.models import Release
reldata = csv.reader(open('/root/Django-1.6.5/django/bin/dashboard/source/release_jnpr.csv'),delimiter=',')
for row in reldata:
 q = Release(number = row[0],
     notes=row[1],
     changes=row[2])
 try:
     q.save()
 except:
     print "line"

