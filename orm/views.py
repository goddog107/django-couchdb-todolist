from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils.timezone import datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
import couchdb
import pandas as pd
import json

from .models import Post

# Create your views here.
couch = couchdb.Server('http://localhost:5984')
db = couch['posts']


def index(request):
  rows = db.view('_all_docs', include_docs=True)
  data = [row['doc'] for row in rows]
  for row in data:
    row['id'] = row['_id']  
  context = {'data': data}
  return render(request, 'orm/index.html', context)


def create(request):
  return render(request, 'orm/create.html')


def save(request, post_id):
  title = request.POST['title']
  content = request.POST['content']
  if(post_id == "0"):
    dt = datetime.now()
    df = DateFormat(dt)
    db.save({'title': title, 'content': content, 'posted_at': df.format('Y-m-d')})
  else:
    post = db.get(post_id)
    post["title"] = title
    post["content"] = content
    db.save(post)

  return redirect('/')


def delete(request):
  ids = json.loads(request.POST['ids'])
  for id in ids:
    post = db.get(id)
    post["_deleted"] = True
    db.save(post)

  return HttpResponse('success')


def edit(request, post_id):
  post = db[post_id]
  context = {
      "id": post_id,
      "title": post['title'],
      "content": post['content']
  }

  return render(request, 'orm/edit.html', context)


def show(request, post_id):
  post = db[post_id]
  context = {
      "id": post_id,
      "title": post["title"],
      "content": post["content"]
  }

  return render(request, 'orm/show.html', context)
