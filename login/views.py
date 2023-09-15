from django.shortcuts import render, redirect
import requests
import json
import ast

from login.form import LoginForm

def indexView(request):
    context = {}
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            login = loginApi(form.cleaned_data['username'], form.cleaned_data['password'])
            if login['login'] == 'true':
                request.session['login'] = login
                return redirect('main')
            else:
                context['error'] = 'Incorrect username or password'

    loginForm = LoginForm()
    context['loginForm'] = loginForm
    return render(request, 'index.html', context)

def mainView(request):
    context = {
        'tasks': getTaskApi(),
        'login': request.session['login'],
    }
    return render(request, 'main.html', context)

def loginApi(username, password):
    body = {
        "name": username,
        "password": password
        }
    url = 'http://localhost:8080/ords/development/users/logIn'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    response = requests.put(url, data=json.dumps(body), headers=headers)
    data = response.json()
    return data

def getTaskApi():
    url = 'http://localhost:8080/ords/development/task/getTasks'
    response = requests.get(url)
    data = response.text
    data = data[1:-2]
    data = data = json.loads(data)
    return data


