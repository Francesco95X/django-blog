from django.shortcuts import render

def post_list(request):
    return render(request, 'djangoblog/post_list.html', {})
