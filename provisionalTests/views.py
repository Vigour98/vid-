from django.shortcuts import render
from .models import Prov_Questions
import random

def home(request):
    return render(request, 'provisionalTests/home.html')

def notes(request):
    return render(request, 'provisionalTests/notes.html')

''' The test comprises 25 muitiple choice questions
    I have made it to have 15 theory questions,
    5 road diagrams questions and 5 questions that
    ask about which car goes first.

    Each time the user take a test, the random questions 
    will bbe selected.
'''
def test(request): 
       
    theory = Prov_Questions.objects.filter(category='theory') 
    theory = list(theory) 
    theory = random.sample(theory,15)
   
    road_diag = Prov_Questions.objects.filter(category='road_diag') 
    road_diag = list(road_diag) 
    road_diag = random.sample(road_diag,5)    
    
    car_diag = Prov_Questions.objects.filter(category='car_diag') 
    car_diag = list(car_diag) 
    car_diag = random.sample(car_diag,5)
    
    test = theory + road_diag + car_diag
    test = random.sample(test,25)

    context = { 'questions' : test, 'num': len(test) } 
    return render(request, 'provisionalTests/test.html', context)

def marks(request):
    if request.method == 'POST': 
        total = request.POST['total'] 
        corrections = list()  
        marks = 0     
        for i in range(1, int(total) + 1):
            question_id = request.POST['qsn' + str(i)]           
            given_answer = request.POST['answer' + str(question_id)]
            
            the_answer = Prov_Questions.objects.get(id=question_id)                   
            pic = the_answer.Q_Image    

            ''' 
                In the following conditional statements the color variables 
                are used only to style the wrong or the correct answer when the
                page is rendered
            '''
            if given_answer == the_answer.answer:
                color = 'black'
                corrections.append([ the_answer.question, the_answer.answer, pic, color ])
                marks += 1
            else:                
                color ='red'
                corrections.append([ the_answer.question, the_answer.answer, pic, color ])
    context = {'corrections':corrections, 'marks':marks, 'total':total}
    return render(request, 'provisionalTests/results.html', context)

