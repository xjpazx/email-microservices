from django.conf import settings

from django.core.mail import EmailMessage



settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    EMAIL_USE_TLS=True,
    EMAIL_HOST='smtp.gmail.com',
    EMAIL_PORT=587,
    EMAIL_HOST_USER='pazgenes1@gmail.com',
    EMAIL_HOST_PASSWORD='00000000',
)





def enviar_email(para,asunto,cuerpo):

    e = EmailMessage()
    e.subject = asunto
    e.to = [para]
    e.body = cuerpo
    e.send()


