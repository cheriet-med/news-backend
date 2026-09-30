from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string


@shared_task
def send_second_email(data, language):
    # Determine the subject and HTML template for the second email
    if language == 'en':
        subject = 'Your Free Book is Here – Grab Your Copy Now!'
        html_message = render_to_string('padlevap/en.html', data)
    elif language == 'fr':
        subject = 'Rappel: Votre livre gratuit est ici – Téléchargez votre exemplaire maintenant !'
        html_message = render_to_string('padlevap/fr.html', data)
    elif language == 'ar':
        subject = 'تذكير: كتابك المجاني هنا – احصل على نسختك الآن!'
        html_message = render_to_string('padlevap/ar.html', data)
    elif language == 'de':
        subject = 'Erinnerung: Ihr kostenloses Buch ist da – Holen Sie sich jetzt Ihr Exemplar!'
        html_message = render_to_string('padlevap/de.html', data)
    elif language == 'es':
        subject = 'Recordatorio: Tu libro gratis está aquí – ¡Consigue tu copia ahora!'
        html_message = render_to_string('padlevap/es.html', data)
    elif language == 'it':
        subject = 'Promemoria: Il tuo libro gratuito è qui – Scarica la tua copia ora!'
        html_message = render_to_string('padlevap/it.html', data)
    elif language == 'nl':
        subject = 'Herinnering: Je gratis boek is hier – Download nu je exemplaar!'
        html_message = render_to_string('padlevap/nl.html', data)
    elif language == 'pt':
        subject = 'Lembrete: Seu Livro Grátis Está Aqui – Baixe Sua Cópia Agora!'
        html_message = render_to_string('padlevap/pt.html', data)
    elif language == 'ru':
        subject = 'Напоминание: Ваша бесплатная книга здесь – получите свою копию прямо сейчас!'
        html_message = render_to_string('padlevap/ru.html', data)
    else:
        subject = 'Påminnelse: Din gratis bok är här – hämta din kopia nu!'
        html_message = render_to_string('padlevap/sv.html', data)

    # Send the second email
    plain_message = html_message
    from_email = 'Padlev <support@azguer.com>'
    to = data['email']

    send_mail(subject, plain_message, from_email, [to], html_message=html_message)


@shared_task
def send_second_email(data, language):
    print(f"=== SEND SECOND EMAIL TASK STARTED ===")
    print(f"Data: {data}")
    print(f"Language: {language}")
    
    try:
        # Determine the subject and HTML template for the second email
        if language == 'en':
            subject = 'Your Free Book is Here – Grab Your Copy Now!'
            template_path = 'padlevap/en.html'
            print(f"Using template: {template_path}")
            html_message = render_to_string(template_path, data)
        elif language == 'fr':
            subject = 'Rappel: Votre livre gratuit est ici – Téléchargez votre exemplaire maintenant !'
            html_message = render_to_string('padlevap/fr.html', data)
        elif language == 'ar':
            subject = 'تذكير: كتابك المجاني هنا – احصل على نسختك الآن!'
            html_message = render_to_string('padlevap/ar.html', data)
        elif language == 'de':
            subject = 'Erinnerung: Ihr kostenloses Buch ist da – Holen Sie sich jetzt Ihr Exemplar!'
            html_message = render_to_string('padlevap/de.html', data)
        elif language == 'es':
            subject = 'Recordatorio: Tu libro gratis está aquí – ¡Consigue tu copia ahora!'
            html_message = render_to_string('padlevap/es.html', data)
        elif language == 'it':
            subject = 'Promemoria: Il tuo libro gratuito è qui – Scarica la tua copia ora!'
            html_message = render_to_string('padlevap/it.html', data)
        elif language == 'nl':
            subject = 'Herinnering: Je gratis boek is hier – Download nu je exemplaar!'
            html_message = render_to_string('padlevap/nl.html', data)
        elif language == 'pt':
            subject = 'Lembrete: Seu Livro Grátis Está Aqui – Baixe Sua Cópia Agora!'
            html_message = render_to_string('padlevap/pt.html', data)
        elif language == 'ru':
            subject = 'Напоминание: Ваша бесплатная книга здесь – получите свою копию прямо сейчас!'
            html_message = render_to_string('padlevap/ru.html', data)
        else:
            subject = 'Påminnelse: Din gratis bok är här – hämta din kopia nu!'
            html_message = render_to_string('padlevap/sv.html', data)
        
        print(f"Subject: {subject}")
        print(f"To: {data['email']}")
        
        # Send the second email
        plain_message = html_message
        from_email = 'Padlev <contact@padlev.com>'
        to = data['email']
        
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        
        print("✅ Second email sent successfully!")
        
    except Exception as e:
        print(f"❌ Error sending second email: {e}")
        import traceback
        traceback.print_exc()
        raise  # Re-raise to see error in Celery



@shared_task
def test_email_task():
    print("=== TEST EMAIL TASK ===")
    
    from django.conf import settings
    print(f"Using FROM email: {settings.DEFAULT_FROM_EMAIL}")
    
    try:
        send_mail(
            subject='hello this from django celery',
            message='This is a test email from Celery',
            from_email=settings.DEFAULT_FROM_EMAIL,  # CRITICAL: Use from settings
            recipient_list=['contact.azguer@gmail.com'],  # Your REAL email
            fail_silently=False,
        )
        return "✅ Email sent successfully!"
    except Exception as e:
        return f"❌ Failed to send email: {e}"

@shared_task
def simple_test_task():
    print("=== SIMPLE TASK STARTED ===")
    print("This should appear in Celery worker logs")
    return "Task completed successfully"



@shared_task
def send_third_email(data, language):
    print(f"=== SEND THIRD EMAIL TASK STARTED ===")
    print(f"Data: {data}")
    print(f"Language: {language}")
    
    try:
        # Determine the subject and HTML template for the second email
        if language == 'en':
            subject = 'Most Players Obsess Over Smashes… But This Wins More Points'
            template_path = 'email1/en.html'
            print(f"Using template: {template_path}")
            html_message = render_to_string(template_path, data)
        elif language == 'fr':
            subject = 'La plupart des joueurs sont obsédés par les smashs… mais ceci fait gagner plus de points'
            html_message = render_to_string('email1/fr.html', data)
        elif language == 'ar':
            subject = 'معظم اللاعبين مهووسون بالضربات الساحقة… لكن هذا ما يفوز بالمزيد من النقاط'
            html_message = render_to_string('email1/ar.html', data)
        elif language == 'de':
            subject = 'Die meisten Spieler sind besessen von Schmetterbällen… aber das hier gewinnt mehr Punkte'
            html_message = render_to_string('email1/de.html', data)
        elif language == 'es':
            subject = 'La mayoría de los jugadores se obsesionan con los remates… pero esto gana más puntos'
            html_message = render_to_string('email1/es.html', data)
        elif language == 'it':
            subject = 'La maggior parte dei giocatori è ossessionata dalle schiacciate… ma questo fa vincere più punti'
            html_message = render_to_string('email1/it.html', data)
        elif language == 'nl':
            subject = 'De meeste spelers zijn geobsedeerd door smashes… maar dit wint meer punten'
            html_message = render_to_string('email1/nl.html', data)
        elif language == 'pt':
            subject = 'A maioria dos jogadores é obcecada por smashes… mas isto ganha mais pontos'
            html_message = render_to_string('email1/pt.html', data)
        elif language == 'ru':
            subject = 'Большинство игроков зациклены на смэшах… но именно это приносит больше очков'
            html_message = render_to_string('email1/ru.html', data)
        else:
            subject = 'De flesta spelare är besatta av smashar… men det här vinner fler poäng'
            html_message = render_to_string('email1/sv.html', data)
        
        print(f"Subject: {subject}")
        print(f"To: {data['email']}")
        
        # Send the second email
        plain_message = html_message
        from_email = 'Padlev <contact@padlev.com>'
        to = data['email']
        
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        
        print("✅ third email sent successfully!")
        
    except Exception as e:
        print(f"❌ Error sending third email: {e}")
        import traceback
        traceback.print_exc()
        raise  # Re-raise to see error in Celery




@shared_task
def send_fourth_email(data, language):
    print(f"=== SEND FOURTH EMAIL TASK STARTED ===")
    print(f"Data: {data}")
    print(f"Language: {language}")
    
    try:
        # Determine the subject and HTML template for the second email
        if language == 'en':
            subject = 'Most Players Waste Time Stretching… Pros Do This Instead'
            template_path = 'email2/en.html'
            print(f"Using template: {template_path}")
            html_message = render_to_string(template_path, data)
        elif language == 'fr':
            subject = 'La plupart des joueurs perdent du temps à s’étirer… Les pros font ceci à la place'
            html_message = render_to_string('email2/fr.html', data)
        elif language == 'ar':
            subject = 'معظم اللاعبين يضيّعون وقتهم في الإطالة… المحترفون يفعلون هذا بدلاً من ذلك'
            html_message = render_to_string('email2/ar.html', data)
        elif language == 'de':
            subject = 'Die meisten Spieler verschwenden Zeit mit Dehnen… Profis machen stattdessen das'
            html_message = render_to_string('email2/de.html', data)
        elif language == 'es':
            subject = 'La mayoría de los jugadores pierden el tiempo estirando… Los profesionales hacen esto en su lugar'
            html_message = render_to_string('email2/es.html', data)
        elif language == 'it':
            subject = 'La maggior parte dei giocatori perde tempo a fare stretching… I professionisti fanno questo invece'
            html_message = render_to_string('email2/it.html', data)
        elif language == 'nl':
            subject = 'De meeste spelers verspillen tijd aan stretchen… Professionals doen dit in plaats daarvan'
            html_message = render_to_string('email2/nl.html', data)
        elif language == 'pt':
            subject = 'A maioria dos jogadores perde tempo alongando… Os profissionais fazem isto em vez disso'
            html_message = render_to_string('email2/pt.html', data)
        elif language == 'ru':
            subject = 'Большинство игроков тратят время на растяжку… Профессионалы делают это вместо этого'
            html_message = render_to_string('email2/ru.html', data)
        else:
            subject = 'De flesta spelare slösar tid på att stretcha… Proffs gör detta istället'
            html_message = render_to_string('email2/sv.html', data)
        
        print(f"Subject: {subject}")
        print(f"To: {data['email']}")
        
        # Send the second email
        plain_message = html_message
        from_email = 'Padlev <contact@padlev.com>'
        to = data['email']
        
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        
        print("✅ forth email sent successfully!")
        
    except Exception as e:
        print(f"❌ Error sending forth email: {e}")
        import traceback
        traceback.print_exc()
        raise  # Re-raise to see error in Celery






@shared_task
def send_fifth_email(data, language):
    print(f"=== SEND FIFTH EMAIL TASK STARTED ===")
    print(f"Data: {data}")
    print(f"Language: {language}")
    
    try:
        # Determine the subject and HTML template for the second email
        if language == 'en':
            subject = 'You Don’t Need Mind-Reading — Just Spot These 2 Tells'
            template_path = 'email3/en.html'
            print(f"Using template: {template_path}")
            html_message = render_to_string(template_path, data)
        elif language == 'fr':
            subject = 'Vous n’avez pas besoin de lire dans les pensées — repérez simplement ces 2 signes.'
            html_message = render_to_string('email3/fr.html', data)
        elif language == 'ar':
            subject = 'لست بحاجة إلى قراءة الأفكار — فقط لاحظ هاتين الإشارتين.'
            html_message = render_to_string('email3/ar.html', data)
        elif language == 'de':
            subject = 'Du brauchst keine Gedanken zu lesen — erkenne einfach diese 2 Hinweise.'
            html_message = render_to_string('email3/de.html', data)
        elif language == 'es':
            subject = 'No necesitas leer la mente — solo detecta estas 2 señales.'
            html_message = render_to_string('email3/es.html', data)
        elif language == 'it':
            subject = 'Non hai bisogno di leggere nella mente — basta individuare questi 2 segnali.'
            html_message = render_to_string('email3/it.html', data)
        elif language == 'nl':
            subject = 'Je hoeft geen gedachten te lezen — herken gewoon deze 2 signalen.'
            html_message = render_to_string('email3/nl.html', data)
        elif language == 'pt':
            subject = 'Você não precisa ler mentes — basta identificar estes 2 sinais.'
            html_message = render_to_string('email3/pt.html', data)
        elif language == 'ru':
            subject = 'Вам не нужно читать мысли — просто замечайте эти 2 сигнала.'
            html_message = render_to_string('email3/ru.html', data)
        else:
            subject = 'Du behöver inte läsa tankar — upptäck bara dessa 2 signaler.'
            html_message = render_to_string('email3/sv.html', data)
        
        print(f"Subject: {subject}")
        print(f"To: {data['email']}")
        
        # Send the second email
        plain_message = html_message
        from_email = 'Padlev <contact@padlev.com>'
        to = data['email']
        
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        
        print("✅ fifth email sent successfully!")
        
    except Exception as e:
        print(f"❌ Error sending fifth email: {e}")
        import traceback
        traceback.print_exc()
        raise  # Re-raise to see error in Celery






@shared_task
def send_sixth_email(data, language):
    print(f"=== SEND SIXTH EMAIL TASK STARTED ===")
    print(f"Data: {data}")
    print(f"Language: {language}")
    
    try:
        # Determine the subject and HTML template for the second email
        if language == 'en':
            subject = 'Great Doubles Players Don’t Chase—They Control the Net'
            template_path = 'email4/en.html'
            print(f"Using template: {template_path}")
            html_message = render_to_string(template_path, data)
        elif language == 'fr':
            subject = 'Les grands joueurs de double ne courent pas après la balle — ils contrôlent le filet.'
            html_message = render_to_string('email4/fr.html', data)
        elif language == 'ar':
            subject = 'أفضل لاعبي الزوجي لا يطاردون الكرة — بل يسيطرون على الشبكة.'
            html_message = render_to_string('email4/ar.html', data)
        elif language == 'de':
            subject = 'Großartige Doppelspieler jagen nicht dem Ball hinterher – sie kontrollieren das Netz.'
            html_message = render_to_string('email4/de.html', data)
        elif language == 'es':
            subject = 'Los grandes jugadores de dobles no persiguen la pelota — controlan la red.'
            html_message = render_to_string('email4/es.html', data)
        elif language == 'it':
            subject = 'I grandi giocatori di doppio non inseguono la palla — controllano la rete.'
            html_message = render_to_string('email4/it.html', data)
        elif language == 'nl':
            subject = 'Geweldige dubbelspelers jagen niet achter de bal aan — zij controleren het net.'
            html_message = render_to_string('email4/nl.html', data)
        elif language == 'pt':
            subject = 'Grandes jogadores de duplas não correm atrás da bola — eles controlam a rede.'
            html_message = render_to_string('email4/pt.html', data)
        elif language == 'ru':
            subject = 'Великие игроки в паре не гоняются за мячом — они контролируют сетку.'
            html_message = render_to_string('email4/ru.html', data)
        else:
            subject = 'Stora dubbelspelare jagar inte bollen — de kontrollerar nätet.'
            html_message = render_to_string('email4/sv.html', data)
        
        print(f"Subject: {subject}")
        print(f"To: {data['email']}")
        
        # Send the second email
        plain_message = html_message
        from_email = 'Padlev <contact@padlev.com>'
        to = data['email']
        
        send_mail(subject, plain_message, from_email, [to], html_message=html_message)
        
        print("✅ sixth email sent successfully!")
        
    except Exception as e:
        print(f"❌ Error sending sixth email: {e}")
        import traceback
        traceback.print_exc()
        raise  # Re-raise to see error in Celery

