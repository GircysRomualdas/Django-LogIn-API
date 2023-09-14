from django.shortcuts import render
import requests
import json

from login.form import LoginForm

def indexView(request):
    context = {}
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            login = loginApi(form.cleaned_data['username'], form.cleaned_data['password'])
            if login['login']:
                return render(request, 'main.html', context = {'login': login,})

    loginForm = LoginForm()
    context['loginForm'] = loginForm
    return render(request, 'index.html', context)

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
