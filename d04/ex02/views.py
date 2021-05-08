from django.shortcuts import render
from . forms import CustomForm
import logging

logger = logging.getLogger('dj_post')

def like_django(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            logger.debug(form.cleaned_data['content'])
    else:
        form = CustomForm()
    try:
        data = list()
        with open("ex02/debug.log", "r") as fd:
            for line in fd:
                data.append(line)
        data = data[::-1]
    except:
        print("Something went wrong !")
    return render(request, 'ex02/like_django.html', {'form': form, 'data': data })