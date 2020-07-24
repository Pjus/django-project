from django.shortcuts import render
import sqlite3

# Create your views here.
def home(request):
    return render(request, 'home.html')

def projects(request):
    return render(request, 'projects.html')

def list(request):
    data = request.GET.copy()
    with sqlite3.connect("D:\\SD_python\\django\\django-project\\matchdb.sqlite3") as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from matches")
        data['rows'] = cur.fetchall()
    return render(request, 'links.html', context=data)


