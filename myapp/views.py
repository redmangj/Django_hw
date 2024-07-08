from django.http import HttpResponse
import re
def index(request):
    return HttpResponse("Hello, world!")


def acrticles(request):
    return HttpResponse("Hello, acrticles!")


def archive(request):
    return HttpResponse("Hello, archive!")


def users(request):
    return HttpResponse("Hello, users!")


def article_number(request, article_number):
    return HttpResponse("article number is {}!".format(article_number))


def article_number_slug(request, article_number, slug_text=''):
    return HttpResponse("article number is {}, {}!".format(article_number, "slug_text is {}".format(slug_text)))


def user_number(request, user_number):
    return HttpResponse("user_number is {}!".format(user_number))


def phone_number(requst, code_id, number):
    if code_id == 50 or code_id == 66 or code_id == 95 or code_id ==  99:
        return HttpResponse( f'Це оператор Vodafone Україна, ваш номер телофону 0{code_id}{number}')
    elif code_id == 67 or code_id == 68 or code_id == 96 or code_id == 97 or code_id == 98:
        return HttpResponse(f'Це оператор Київстар, ваш номер телофону 0{code_id}{number}')
    else:
        return HttpResponse (f'Ніякого оператора за таким кодом 0{code_id} не існує')


def interest(requst, four_numbers, six_numbers):
    result = re.match('[a-f1-9]{4}', four_numbers)
    result1 = re.match('[a-f1-9]{6}', six_numbers)
    if result and len(four_numbers) == 4 and result1 and len(six_numbers) == 6:
        return HttpResponse(f'URL {four_numbers}-{six_numbers} відповідає вимогам!')
    else:
        return HttpResponse(f'Помилка')