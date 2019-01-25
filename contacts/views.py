from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = Contact(listing=listing, listing_id=listing_id,
        name=name,email=email,phone=phone,message=message,user_id=user_id)

        #check if user has made inquiry before

        if request.user.is_authenticated:
            user_id = user_id
            has_contacted = Contact.objects.filter(listing_id=listing_id,
                user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inqury for this listing')
                return redirect('/listings/' +listing_id)


        contact.save()

        #Send mail
# import smtplib
# fromMy = 'yourMail@yahoo.com' # fun-fact: from is a keyword in python, you can't use it as variable, did abyone check if this code even works?
# to  = 'SomeOne@Example.com'
# subj='TheSubject'
# date='2/1/2010'
# message_text='Hello Or any thing you want to send'
#
# msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( fromMy, to, subj, date, message_text )
#
# username = str('yourMail@yahoo.com')
# password = str('yourPassWord')
#
# try :
#     server = smtplib.SMTP("smtp.mail.yahoo.com",587)
#     server.login(username,password)
#     server.sendmail(fromMy, to,msg)
#     server.quit()
#     print 'ok the email has sent '
# except :
#     print 'can\'t send the Email'

        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
            'themanlahind@yahoo.com',
            [realtor_email, 'maduabuchiokonkwo@gmail.com'],
            fail_silently = False
        )

        messages.success(request, 'Your request has been submitted someone will get back to you soon')

        return redirect('/listings/'+listing_id)
