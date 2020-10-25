from django.shortcuts import render

def suggest(request):
    students = [{'name':'Rahul','email':'student@gmail.com','standard':'4th','hobbies':'Singing,Playing','roll_no':'12','bio':'NoBio','id':1}]
    teachers = [{'id':'1','name':'RJN','Department':'OKAAAY','email':'teacher@gmail.com'}]
    return render(request,'Suggest/suggest.html',{'students':students,'teachers':teachers})