# -*- coding: utf-8 -*-
from __future__ import absolute_import


from celery import Celery
from celery import platforms

app = Celery('proj',
             broker="amqp://tcsd:vd8-nem-qVD-2FP@t1.map.design:5672//tilefactory",
             backend="redis://localhost:6379",
             include=['gettiles_task'])
platforms.C_FORCE_ROOT = True

if __name__ == '__main__':
    app.start()
