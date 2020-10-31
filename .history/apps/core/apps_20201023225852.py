from django.apps import AppConfig
import os
import notifyall.py as jobs

class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from notifyall import jobs
        print('Hello')
        if os.environ.get('RUN_MAIN', None) != 'true':
            jobs.start_scheduler()