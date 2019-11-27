from search_engine_parser import GoogleSearch
from xlwt import Workbook
import pprint

link=[]
title=[]
description=[]

#creating excel file to store results
wb = Workbook()
file = wb.add_sheet('file')
file.write(0, 0, 'URLs')
file.write(0, 1, 'Titles')
file.write(0, 2, 'Description')

for i in range(1,6):
    #parsing search engine results
    search_args = ('web crawling king', i)
    gsearch = GoogleSearch()
    gresults = gsearch.search(*search_args)
    for j in range(10):
        link.append(gresults["links"][j])
        title.append(gresults["titles"][j])
        description.append(gresults["descriptions"][j])

#saving in excel file
for k in range(2,52):
    file.write(k, 0, link[k-2])
    file.write(k, 1, title[k-2])
    file.write(k, 2, description[k-2])
wb.save('parsing-results.xls')
