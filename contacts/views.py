from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
from django.contrib import messages

def contact(request) :
    if request.method == 'POST' :
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        realtor_email=request.POST['realtor_email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']

        if request.user.is_authenticated:
            user_id=request.user.id
            has_inquired=Contact.objects.all().filter(listing_id=listing_id, user_id=user_id )
            if has_inquired :
                messages.error(request,'Oops you have already made inquiry for this property :( ')
                return redirect('/listings/'+listing_id)

        contact=Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()
        send_mail(
        'Regarding Property Enquiry',
        'Hey ' + name + ' you have inquired about one of our property ' + listing + ' . Sign in for the next step :)' ,
        'shivesht99@gmail.com',
        [email, 'shivesht01@gmail.com'],
        fail_silently=False,
)





        messages.success(request, 'Thanks for filling the inquiry form . Our realtor will soon contact you :)')
        return redirect('/listings/'+listing_id)


