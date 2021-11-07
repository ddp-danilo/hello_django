from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return redirect('admin/')
def hello_text(nome=None, idade=None):
    """retorna o texto para a funcão hello"""
    final_string = 'Hello '
    if nome == None:
        return final_string
    else:
        final_string += '{} '.format(nome)
        if idade == None:
            return final_string
        else:
            return final_string + 'Idade: {} '.format(idade)


def hello(request, nome=None, idade=None):
    return HttpResponse(hello_text(nome, idade))

#calc finctions
def soma(request, d1=0, d2=0):
    soma = d1 + d2
    return HttpResponse('A soma de {} com {} é {}'.format(d1, d2, soma))

def multi(request, d1=0, d2=0):
    prod = d1 * d2
    return HttpResponse('A Multiplicação de {} com {} é {}'.format(d1, d2, prod))
def divi(request, d1=0, d2=0):
    try:
        quociente = d1 / d2
    except ZeroDivisionError:
        return HttpResponse('Não é posivel dividir por zero.')
    else:
        return HttpResponse('A Divisão de {} com {} é {}'.format(d1, d2, quociente))
def sub(request, d1=0, d2=0):
    valor = d1 - d2
    return HttpResponse('A Subtração de {} com {} é {}'.format(d1, d2, valor))
def calc(request):
    return render(request, 'calc.html')
def calc_submit(request):
    n1 = request.POST.get('n1')
    n2 = request.POST.get('n2')
    op = request.POST.get('operacao')
    if op is not None:
        return redirect('/{}/{}/{}'.format(op,n1,n2))
    else:
        redirect('/calc')

