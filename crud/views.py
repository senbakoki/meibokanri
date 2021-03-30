from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,  
)
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from .models import Message
from .forms import MessageForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import LoginForm


#一覧表示
def index(request):
    d = {
        'messages': Message.objects.all(),
    }
    return render(request, 'crud/index.html', d)

#登録用
def add(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        Message.objects.create(**form.cleaned_data)#多分データベースに新しく作るコマンド
        return redirect('crud:index')

    d = {
        'form': form,
    }
    return render(request, 'crud/edit.html', d)#新しくできたデータを渡す

#編集用
def edit(request, editing_id):
    message = get_object_or_404(Message, id=editing_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message.teacher_name = form.cleaned_data['teacher_name']
            message.time13_1 = form.cleaned_data['time13_1']
            message.time13_2 = form.cleaned_data['time13_2']
            message.time14_1 = form.cleaned_data['time14_1']
            message.time14_2 = form.cleaned_data['time14_2']
            message.time17_1 = form.cleaned_data['time17_1']
            message.time17_2 = form.cleaned_data['time17_2']
            message.time18_1 = form.cleaned_data['time18_1']
            message.time18_2 = form.cleaned_data['time18_2']
            message.time20_1 = form.cleaned_data['time20_1']
            message.time20_2 = form.cleaned_data['time20_2']
            message.save()
            return redirect('crud:index')
    else:
        # GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
        form = MessageForm({'teacher_name': message.teacher_name, 'time13_1': message.time13_1, 'time13_2': message.time13_2, 'time14_1': message.time14_1, 'time14_2': message.time14_2})
    d = {
        'form': form,
    }
    return render(request, 'crud/edit.html', d)

#削除用
@require_POST
def delete(request):
    delete_ids = request.POST.getlist('delete_ids')
    if delete_ids:
        Message.objects.filter(id__in=delete_ids).delete()
    return redirect('crud:index')
#p
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from .forms import LoginForm


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'crud/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = 'crud/login.html'