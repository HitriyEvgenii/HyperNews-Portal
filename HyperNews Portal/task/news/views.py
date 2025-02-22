from django.shortcuts import render
import datetime
# Create your views here.
from django.views import generic
from django.conf import settings
import json
import itertools
from django.views import View
from django.shortcuts import redirect

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
    json_data.close()
    for cont in cont:
        if cont['link'] == post_id:
            print(cont)
            context = cont
            print(context)
            return render(request, template_name, context=context)

def news_list(request):
    template_name = 'news_list.html'
    json_data = open('hypernews/news.json', 'r')
    json_dict =json.load(json_data)
    print(json_dict)
    for i in json_dict:
        i["created"] = datetime.datetime.strptime(i["created"],'%Y-%m-%d %H:%M:%S').date()

    cont = {'news': json_dict }

    return render(request, template_name, context=cont)

class CreateArticle(View):
    template_name = 'create_article.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        form = request.POST
        #title = form.Queryset
        title = form['title']

        date_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(date_now)
        article = {"created": date_now,
                   "text": form['text'],
                   "title": form['title']}
        with open('hypernews/news.json', 'r') as json_file:
            json_dict = json.load(json_file)
            json_dict.append(article)
        print(json_dict)
        with open('hypernews/news.json', 'w', encoding='utf-8') as json_file:
            json.dump(json_dict, json_file)

        return redirect('/news/')
