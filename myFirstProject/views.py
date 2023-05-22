from django.shortcuts import render
def home(r):
    context={}
    context['id']=5555
    context['students']=[
        {
            'id':1,
            'name':'geahd'
        },
        {
            'id': 2,
            'name': 'noha'
        },
    ]
    return render(r,'index.html',context)