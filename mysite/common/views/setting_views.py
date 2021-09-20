from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm


@login_required(login_url='common:login')
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "비밀번호가 변경되었습니다.")
            return redirect('pybo:index')
        else:
            messages.success(request, "잘못된 값을 입력하였습니다.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'common/password_form.html', {'form': form})