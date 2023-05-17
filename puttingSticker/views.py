from django.shortcuts import render

# Create your views here.
def sticker_on(request):
  return render(request, 'sticker/sticker_on.html')
