from celery import Celery

celery_app= Celery(__name__, broker='redis://localhost:6379/0')

@celery_app.task
def registrar_log(usuario,fecha):
    with open ('log.txt', 'a+') as archivo:
        archivo.write('{} -- inicio de sesion {}\n'.format(usuario,fecha))
