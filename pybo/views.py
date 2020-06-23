from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import Question, Answer, Comment
from .forms import QuestionForm, AnswerForm, CommentForm





    
        
            
