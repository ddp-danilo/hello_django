from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import random

# Create your views here.
def senha(request):
    return render(request, 'senha.html')

class pass_gen():
    def __init__(self,tamanho=0, tem_cod=True, tem_num=True, tem_upper=True, tem_lower=True):
        self.tamanho = tamanho
        self.rnd = [(33,47),(48,57),(65,90),(97,122)]
        self.possible_digit = []
        if tem_cod:
            self.possible_digit.append(self.rnd[0])
        if tem_num:
            self.possible_digit.append(self.rnd[1])
        if tem_upper:
            self.possible_digit.append(self.rnd[2])
        if tem_lower:
            self.possible_digit.append(self.rnd[3])
    def rnd_ascii_num(self):
        pd_ln = len(self.possible_digit)
        if pd_ln != 1:
            y = random.randrange(1, pd_ln + 1)
        else:
            y = 1
        return random.randrange(self.possible_digit[y - 1][0],self.possible_digit[y - 1][1])
    def cria_senha(self):
        senha = ''
        for n in range(self.tamanho):
            senha += chr(self.rnd_ascii_num())
        return senha

def senha_submit(request):

    tam = int(request.POST.get('tam'))
    if request.POST.get('sym') is not None:
        sym = True
    else:
        sym = False
    if request.POST.get('num') is not None:
        num = True
    else:
        num = False
    if request.POST.get('upp') is not None:
        upp = True
    else:
        upp = False
    if request.POST.get('low') is not None:
        low = True
    else:
        low = False
    codigo = pass_gen(tam, sym,num,upp,low)

    messages.info(request, '{}'.format(codigo.cria_senha()))
    return redirect('/senha')