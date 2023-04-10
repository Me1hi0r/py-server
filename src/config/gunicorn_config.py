pythonpath = '/home/me1hior/Project/tutorial/py-server/src'
bind = 'localhost:9000'
workers = 3

loglevel = 'debug'
accesslog = '/home/me1hior/Project/tutorial/py-server/log/gunicorn.access.log'
errorlog = '/home/me1hior/Project/tutorial/py-server/log/gunicorn.error.log'
acceslogformat = "%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
