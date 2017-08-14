#coding=utf-8
from celery import Celery
import json
import os
import urllib2
# from bson.objectid import ObjectId
# from socketIO_client import SocketIO, LoggingNamespace
import getMvtTiles

# import redis
import math

import time
fpConfig = open('./config.json')
config = json.load(fpConfig)
fpConfig.close()

app = Celery('tasks', broker='amqp://tcsd:vd8-nem-qVD-2FP@t1.map.design:5672//tilefactory')



'''messageId 信息ID, messageState 信息状态, messageTitle 信息标题, messageDesc 信息描述, messageColor 信息颜色（'red'
        错误, 'green' 成功, 'blue'进行中）， task < option > {taskProcess < option > 任务进度(0 - 100), canCancel 任
        务是否可以取消，showProgress 是否显示进度}
        *client.emit('set msg', {eId: eId,msg: {messageId: messageId, messageState: messageState,
        messageTitle: messageTitle,messageDesc: messageDesc, messageColor: messageColor,task:
        {taskProcess: taskProcess, canCancel: canCancel,showProgress: showProgress}}});
'''



@app.task
def create(outputPath, minx, miny, maxx, maxy, stylePath, minz, maxz):
    try:
        # socketIO = SocketIO(config["socketio"]["host"], config["socketio"]["port"], LoggingNamespace)
        strprocess = unicode('正在处理...', 'utf-8')
        # socketIO.emit("set msg",{'eId':entName,'msg':{'messageId':strcnt,'messageState':strprocess,"messageTitle":tilesetName,'messageDesc':'','messageColor':'blue','task':{'taskProcess': 10, 'canCancel': False,'showProgress': True}}});
        getMvtTiles.gettile(outputPath, minx, miny, maxx, maxy, stylePath, minz, maxz )

        print "completed"
        return "add"

    except Exception as e:
        return str(e)

