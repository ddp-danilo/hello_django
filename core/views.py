from django.shortcuts import render, HttpResponse

# Create your views here.
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
