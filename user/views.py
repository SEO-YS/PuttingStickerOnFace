from django.shortcuts import render



def main (request):
    return render(request,'mainpage.html')

def singup (request):
    return render(request , 'user/signup.html')

