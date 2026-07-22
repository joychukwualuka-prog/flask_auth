from flask_mail import Mail
from extension import mail

def send_verification_email(email, fullname, verification_link):
    msg = Message(
        subject="Verify your email address",
        recipients=[email],
      )
    msg.body=f"""
Hello {fullname},

Thank you for registering

Click the link below to verify your email address:

{verification_link}

If you didnt register, please ignore this email.

Regards,
Learning Pro
"""

    mail.send(msg)