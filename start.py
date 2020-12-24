from subprocess import Popen

commands = ['python manage.py runserver', 'celery -A ArticleAggregator worker -l info',
            'celery -A ArticleAggregator beat -l info']

procs = [Popen(i) for i in commands]
for p in procs:
    p.wait()
