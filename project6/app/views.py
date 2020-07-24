from django.shortcuts import render

# Create your views here.
def signin(request):
    return render(request, 'signin.html')

def result(request):
    
    checkbox1 = request.GET.get('checkbox1')
    checkbox2 = request.GET.get('checkbox2')
    if(checkbox1=='true' and checkbox2=='true'):
        text = request.GET['text']
        email = request.GET['email']
        password1 = request.GET['password1']
        password2 = request.GET['password2']
        
        if(password1==password2):
            return render(request, 'result.html', {'result':'가입완료'})
        else:
            return render(request, 'result.html', {'result':'비밀번호 불일치'})
    else:
      return render(request, 'result.html', {'result' :'약관 동의해주세요'})