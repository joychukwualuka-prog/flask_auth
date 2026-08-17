# from extension import mail
from config import Config
from flask import current_app


def send_verification_email(email, subject, html):
    try:
        from brevo import Brevo
        from brevo.transactional_emails import (
            SendTransacEmailRequestSender,
            SendTransacEmailRequestToItem,
        )
    except ImportError:
        raise RuntimeError(
            "Missing 'brevo' package. Install it with 'pip install brevo' and add it to requirements.txt."
        )

    client = Brevo(api_key=current_app.config["BREVO_API_KEY"])
    client.transactional_emails.send_transac_email(
        subject=subject,
        html_content=html,
        sender=SendTransacEmailRequestSender(
            name=current_app.config["MAIL_FROM_TITLE"],
            email=current_app.config["MAIL_FROM"],
        ),
        to=[
            SendTransacEmailRequestToItem(email=email),
        ],
    )