from django.shortcuts import render
import random
# Create your views here.

def test(request):
    return render(request, ' core/testPage.html')

def form(request):
    return render(request, 'core/form.html')

def magic_number(request):
    if request.method =='POST':
        number = request.POST['number']
        print(request.POST)
        print(number)
        number = int(number)
        random_number = random.randint(1,5)

        if number == random_number:
            result = 'Поздравляю :)'
        else:
            result = f"Не угадали, число  было {random_number} :("

        return render(request, 'core/magic_number.html', {'result': result})
    else:
        return render(request, 'core/magic_number.html')

