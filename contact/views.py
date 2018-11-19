from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .forms import ContactForm

# Create your views here.

def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
			#phone_number = request.POST.get('phone_number', '')
            message = request.POST.get('message', '')

            # Email the profile with the contact information
            template = get_template('reply_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
				#'phone_number': phone_number,
                'message': message,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "AV Empire" +'',
                [contact_name],
                headers = {'Reply To': contact_email }
            )
            email.send()
			#messages.success(request, 'Thanks for getting in touch! We will get back to you as soon as we can.')
            return redirect('index')

    return render(request, 'contact.html', {
        'form': form_class,
    })