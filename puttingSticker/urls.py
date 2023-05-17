from django.urls import path
import puttingSticker.views as sv

app_name = 'sticker'

urlpatterns = [
    path('sticker_on', sv.sticker_on, name='sticker_on'),
]
