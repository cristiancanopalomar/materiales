from celery import shared_task
from django.core.mail import EmailMultiAlternatives

@shared_task()
def send_trigger_email(
        subject_email,
        from_email,
        to_email,
        content_email,
        content_type,
    ):

    msg = EmailMultiAlternatives(
        subject=subject_email,
        from_email=from_email,
        to=to_email,
    )
    msg.attach_alternative(
        content_email,
        content_type,
    )
    msg.tags = []
    msg.metadata = {}
    msg.send()

    response_f = {}
    response_m = msg.mandrill_response[0]
    response_f = response_m
    if response_f['status'] == 'sent':
        print """as expected, the message was sent.
        """
    else:
        # msg.error(msg)
        print """
            unfortunately something went wrong and we
            have not managed to send the message.
        """
