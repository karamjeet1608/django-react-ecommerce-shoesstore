from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({'message': 'welcome to ecommerce apis'})

# Create your views here.
