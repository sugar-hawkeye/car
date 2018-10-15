# coding=utf-8
import sys
import os
import multiprocessing

current_file = os.path.abspath(__file__)
current_dir = os.path.split(current_file)[0]


bind = "127.0.0.1:8007"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class='gevent'
threads = 2
reload = True

pidfile = '%s/run/car.pid' % current_dir
accesslog = '%s/log/gunicorn_access.log' % current_dir
access_log_format = '%(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"  %(p)s %(h)s %(T)s %(D)s %(L)s'
errorlog = '%s/log/gunicorn_error.log' % current_dir
loglevel = 'info,warning,debug,error,critical'