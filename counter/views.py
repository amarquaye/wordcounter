from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'counter/index.html')

def display_amount(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter/count.html', {'amount': amount_of_words})