# from django.shortcuts import render  
# #importing loading from django template  
# from django.template import loader  
# # Create your views here.  
# from django.http import HttpResponse  
# def index(request):  
#     template = loader.get_template('home.html') # getting our template  
#     return HttpResponse(template.render())  

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# # Create your views here.
def home(request):
    return render(request,'home.html',{})

data = [
{'name': 'Google','link': 'https://www.google.com'},
{'name': 'Facebook','link': 'https://www.facebook.com/'},
{'name': 'Microsoft','link': 'https://www.microsoft.com'},
{'name': 'Yahoo','link': 'https://www.yahoo.com'},
{'name': 'More...','link': 'more.html'},
]

def about(request):
    context = {'data_list' : data}
    return render(request,'about.html',context)

class MorePageView(TemplateView):
    template_name = "more.html" 