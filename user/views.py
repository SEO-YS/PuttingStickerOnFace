from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from user.forms import UserForm





def main (request):
    print(1)
    return render(request,'mainpage.html')

def signup (request):
    print(request)
    if request.method == "POST":
        form = UserForm(request.POST)
        print('hi')
        if form.is_valid():
            form.save()
            print('hi')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            print(raw_password)
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            print(user.password)
            login(request, user)
            print(1)# 로그인
            return redirect('main')
        else:
            print(form.errors)
    else:
        form = UserForm()
        print('hi2')
    return render(request, 'user/signup.html', {'form': form})


