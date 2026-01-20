from django.shortcuts import render
from .forms import ContactForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def about(request):
    """Render about page"""
    return render(request, "about.html")

def index(request):
    """
    Handle form submission, save to database, and send email
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            # Extract cleaned data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            occupation = form.cleaned_data['occupation']
            
            # Save to database
            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation
            )
            
            # Send confirmation email
            msg_body = f"A new job application was submitted.\nThank You {first_name}!"
            email_msg = EmailMessage(
                "Form Submission Confirmation",  # Subject
                msg_body,                        # Body
                to=["ahmedkhalique220@gmail.com"],                       # Recipient
                cc=["khaliqueahmed917@gmail.com"],            # Optional CC
                bcc=["revathyvasundhara@gmail.com"],          # Optional BCC
            )
            email_msg.send()
            
            # Display success message
            messages.success(request, "Form Submitted Successfully!")
    
    return render(request, "index.html")