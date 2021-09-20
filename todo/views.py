from django.shortcuts import render

# Create your views here.
def get_todo_list(request):
    # return HttpResponse("<h1>Hello World</h1><p>Para</p>")
    return render(request, "todo/to-do-list.html")