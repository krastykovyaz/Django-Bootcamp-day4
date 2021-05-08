from django.shortcuts import render

def gen_colors(request):
    colors = range(0, 255, 5)[1:][::-1]
    return render(request, 'ex03/table_col.html', {'colors': colors})

