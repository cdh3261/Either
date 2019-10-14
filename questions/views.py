from django.shortcuts import render,redirect
from .models import Question,Choice
import random
from django.db.models import Max

# Create your views here.
def index(request):
    question = Question.objects.order_by('?').first()
    choices=Choice.objects.filter(question=question)
    blue,red=0,0
    for choice in choices:
        if choice.pick == 2:
            red += 1
        else:
            blue += 1
    avg = round(blue*100/(blue+red),2)
    avg2 = round(red*100/(blue+red),2)
    context = {
        'question': question,
        'choices': choices,
        'blue': blue,
        'red': red,
        'avg': avg,
        'avg2':avg2
    }
    return render(request, 'index.html', context)

def create(request):
    if request.method == 'POST':
        Question.objects.create(
            title = request.POST.get('title'),
            option_a = request.POST.get('option_a'),
            option_b = request.POST.get('option_b'),
            img_a = request.POST.get('img_a'),
            img_b = request.POST.get('img_b')
        )
        return redirect('questions:index')
    else:

        return render(request, 'form.html')

def update(request, id): 
    question = Question.objects.get(id=id)
    if request.method == "POST":
        
        title = request.POST.get('title')
        option_a = request.POST.get('option_a')
        option_b = request.POST.get('option_b')
        img_a = request.POST.get('img_a')
        img_b = request.POST.get('img_b')
        question.title = title
        question.option_a = option_a
        question.option_b = option_b
        question.img_a = img_a
        question.img_b = img_b
        question.save()

        return redirect('questions:index')
    else:
        context = {
            'question': question
        }
        return render(request, 'create.html', context)

def delete(request,id):
    Question.objects.get(id=id).delete()
    return redirect('questions:index')

def detail(request, id):
    question = Question.objects.get(id=id)
    choices=Choice.objects.filter(question=question)
    blue,red=0,0
    for choice in choices:
        if choice.pick == 2:
            red += 1
        else:
            blue += 1
    avg = round(blue*100/(blue+red),2)
    avg2 = round(red*100/(blue+red),2)
    context = {
        'question': question,
        'choices': choices,
        'blue': blue,
        'red': red,
        'avg':avg,
        'avg2':avg2
    }
    return render(request, 'detail.html', context)

def answer_create(request,id):
    question = Question.objects.get(id=id)
    if request.method == "POST":

        comment = request.POST.get('comment')
        username = request.POST.get('username')
        comment_date = request.POST.get('comment_date')
        pick = request.POST.get('pick')
        choice = Choice.objects.create(question=question,comment=comment, username=username, comment_date=comment_date,pick=pick)
        
        return redirect('questions:detail',id)
    else:
        context = {
            'question': question
        }
        return render(request, 'create.html', context)

def answer_update(request, question_id, answer_id):
    question = Question.objects.get(id=question_id)
    if request.method == "POST":
        choice = Choice.objects.get(id=answer_id)
        comment = request.POST.get('comment')
        
        choice.comment = comment
        choice.question = question
        choice.save()
        return redirect('questions:detail', question_id)
    else:
        choices=Choice.objects.filter(question=question)
        blue,red=0,0
        for choice in choices:
            if choice.pick == 2:
                red += 1
            else:
                blue += 1    
        avg = round(blue*100/(blue+red),2)
        avg2 = round(red*100/(blue+red),2)
        context = {
            'question': question,
            'choices': choices, 
            'answer_id': answer_id,
            'blue': blue,
            'red': red,
            'avg':avg,
            'avg2':avg2
        }
        return render(request, 'answer_update.html', context)

def answer_delete(request, question_id, answer_id):
    Choice.objects.get(id=answer_id).delete()
    return redirect('questions:detail', question_id) 

def search(request):
    if request.method == 'POST':
        keyword = request.POST.get("keyword")
        questions = Question.objects.filter(title__icontains=keyword)

        context = {
            'questions': questions
        }
        return render(request, 'search.html', context)
    else:
        questions = Question.objects.all()
        context = {
            'questions': questions
        }
        return render(request, 'search.html',context)
    