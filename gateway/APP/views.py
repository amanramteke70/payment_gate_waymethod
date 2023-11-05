from django.shortcuts import render
import razorpay
from .models import Details
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get('lastname')
        address = request.POST.get('address') 
        city = request.POST.get('city')
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')
        country = request.POST.get('country')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        amount = int(request.POST.get('amount'))* 100
        client = razorpay.Client(auth=("rzp_test_VZ6O5qXR38PSUQ","cDGj5bvkyPkPufPBIrDotceU"))
        payment = client.order.create({'amount': amount, 'currency':'INR', 'payment_capture' : '1'})
        print(payment)
        details = Details(
            firstname = firstname, lastname = lastname, address = address, city = city, amount=amount, state = state, postcode= postcode, country = country, email = email, phone = phone, payment_id = payment['id']
        )
        details.save()
        context = {'payment' : payment,
                   'details' : details}
        return render(request,'index.html', context)

    return render(request,'index.html')


@csrf_exempt
def success(request): 
    # try:
    if request.method == 'POST':
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == "id":
                order_id = val
                
        print(order_id)
        user = Details.objects.filter(payment_id = order_id).first()
        print(user)
        user.paid = True
        user.save()
        return render(request,'success.html')

    # except:
    #     return render(request,'success.html')

