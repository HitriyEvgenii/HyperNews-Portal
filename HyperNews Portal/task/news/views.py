from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.conf import settings
import json



class Index(generic.TemplateView):
    template_name = 'index.html'

'''class Article(generic.TemplateView):
    template_name = 'article.html'
    context_object_name = 'art'

    json_data = open('hypernews/news.json', 'r')
    cont = json.load(json_data)

    #context = json.loads(json_data)
    def get(self,request, post_id, *args, **kwargs):
        for i in self.cont:
            if

        return context

    def post(self, request, post_id, *args, **kwargs):
        self.context['link']= post_id
        print(post_id)
 '''
def article(request, post_id):
    template_name = 'article.html'
    json_data = open('hypernews/news.json', 'r')
    cont = json.load(json_data)
    for cont in cont:
        if cont['link'] == post_id:
            print(cont)
            context = cont
            print(context)
            return render(request, template_name, context=context)