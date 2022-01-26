from django.shortcuts import render
from .hive_models import HiveTable
import re
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

# Create your views here.

catags =  []

def caTagDict():
    url = HiveTable('url_1')    
    URL_list=url.hqlGroupByCaTag()
    caTag_Dict = {}    
    for (tag_category, matched_tag, tag_count) in URL_list:
        if tag_category not in caTag_Dict.keys():
            caTag_Dict[tag_category]={'tags' : list(), 'count' : 0} 
        caTag_Dict[tag_category]['tags'].append((matched_tag, tag_count))   
        caTag_Dict[tag_category]['count'] = caTag_Dict[tag_category]['count']+tag_count
                
    return caTag_Dict


def URLList(catags):
    URL_List=[]
    caTag_Dict = {}
    for catag in catags:
        catagory, tag = catag.split('.')[0], catag.split('.')[1]
        
        if catagory not in caTag_Dict.keys():
               caTag_Dict[catagory]=[]
        caTag_Dict[catagory].append(tag)   
        
        url = HiveTable('url_1')
        UrlList=url.hqlFilter(tag_category=catagory, matched_tag=tag)
        
        for (heading, preview_text, time_stamp, source_link, html_file, tag_category, matched_tag) in UrlList:
            url_Dict={}
            url_Dict['heading']=heading
            url_Dict['preview_text']=preview_text+' ...'
            url_Dict['time_stamp']=time_stamp
            url_Dict['source_link']=source_link
            url_Dict['html_file']=html_file
            url_Dict['tag_category']=tag_category
            url_Dict['matched_tag']=matched_tag
            URL_List.append(url_Dict)
            
    return caTag_Dict, URL_List



def UrlSearchForm(request):    
    caTag_Dict=caTagDict()
    context = {'caTag_Dict': caTag_Dict, 'rowRange': "0:6"}
    return render(request, 'UrlSearchCenter/UrlSearchForm.html', context)



def UrlSearchResult(request):
  global catags
  if request.method == 'POST':
    catags = request.POST.getlist('tag')
    if not len(catags):
        caTag_Dict=caTagDict()
        context = {'caTag_Dict': caTag_Dict, 'rowRange': "0:6", 'error_message': "Error : tags were not selected."}
        return render(request, 'UrlSearchCenter/UrlSearchForm.html', context)
    else:
        return HttpResponseRedirect('?page=1')
    
  if request.method == 'GET':
        page = request.GET.get('page')
        if page == '1':
            display='none'
        else:
            display='block'
            
        caTag_Dict, URL_List = URLList(catags)
        paginator = Paginator(URL_List, 16)        
        
        UrlPage = paginator.get_page(page)
        context = {'caTag_Dict': caTag_Dict, 'UrlPage': UrlPage, 'Count' : len(URL_List), 'display' : display}
        
        return render(request, 'UrlSearchCenter/UrlSearchResult.html', context)
    
def UrlContent(request, html_file):   
    return render(request, 'UrlSearchCenter/HtmlPages/'+html_file)



