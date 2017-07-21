from snakeeyes.app import create_app
from snakeeyes.celery_example import make_celery

from celery import current_app
from celery.bin import worker

app = create_app()
def run():

    application = current_app._get_current_object()

    work = worker.worker(app=application)

    options = {
        'broker': app.config['CELERY_BROKER_URL'],
        'loglevel': 'INFO',
        'traceback': True,
    }
    work.run(**options)

if __name__ =='__main__':
    run()