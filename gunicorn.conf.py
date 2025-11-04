import multiprocessing

bind = "unix:/run/gunicorn.sock"
workers = max(multiprocessing.cpu_count() // 2, 2)
worker_class = "gthread"
threads = 2
timeout = 15
graceful_timeout = 10
keepalive = 5
accesslog = "-"
errorlog = "-"
loglevel = "info"
