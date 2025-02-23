
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
# Create your views here.

def home(request):
    return render(request, 'vive_app/home.html')

def particulier(request):
    return render(request, 'vive_app/particulier.html')


def collectivite(request):
    return render(request, 'vive_app/collectivite.html')


def manifeste(request):
    return render(request, 'vive_app/manifeste.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Sauvegarder le formulaire
            contact = form.save()

            # Préparer le message email
            message_corps = f"""
            Nouveau message de {contact.prenom} {contact.nom}
            Type: {contact.type_contact}
            Email: {contact.email}

            Message:
            {contact.message}
            """

            # Envoyer l'email
            send_mail(
                subject=f'Nouveau contact de {contact.prenom} {contact.nom}',
                message=message_corps,
                from_email={contact.email},
                recipient_list=['lovelyneperrin@gmail.com'],
                fail_silently=False,
            )

            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'vive_app/contact.html', {'form': form})