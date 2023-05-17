from django.shortcuts import render, redirect

# Create your views here.
def sticker_on(request):
  return render(request, 'puttingSticker/sticker_on.html')