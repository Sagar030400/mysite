
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import os
import pickle

with open("model.p",'rb') as pickled:
    data=pickle.load(pickled)
    model= data['logreg']
    vector= data['tfidf']

def index(request):

    if request.method == 'POST':
        a  = request.POST.get('Name')
        vector1=vector.transform([a])
        predict=model.predict(vector1)
        print(predict)
        if predict == 0:
            return render(request,"hello.html",{'abc':'"The Text Does not Contains References to self-harm..."'})
        else:
            return render(request,"hello.html",{'abc':'"The Text Contains References to self-harm..."'})
    else:
        return render(request,"hello.html")