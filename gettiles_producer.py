#coding=utf-8


import gettiles_task
import json
# from bson.objectid import ObjectId
import datetime

from math import atan
from math import cos
from math import exp
from math import log
from math import pi
from math import sin

fpConfig = open('./config.json')
config = json.load(fpConfig)
fpConfig.close()

outputBasePath = config["outputBasePath"]
styleBasePath = config["styleBasePath"]

DEG_TO_RAD = pi / 180
RAD_TO_DEG = 180 / pi


# app = Flask(__name__)


def minmax (a, b, c):
    a = max(a, b)
    a = min(a, c)
    return a

class GoogleProjection:
    def __init__(self, levels=18):
        self.Bc = []
        self.Cc = []
        self.zc = []
        self.Ac = []
        c = 256
        for d in range(0, levels):
            e = c / 2
            self.Bc.append(c / 360.0)
            self.Cc.append(c / (2 * pi))
            self.zc.append((e, e))
            self.Ac.append(c)
            c *= 2

    def fromLLtoPixel(self, ll, zoom):
        d = self.zc[zoom]
        e = round(d[0] + ll[0] * self.Bc[zoom])
        f = minmax(sin(DEG_TO_RAD * ll[1]), -0.9999, 0.9999)
        g = round(d[1] + 0.5 * log((1 + f) / (1-f)) * -self.Cc[zoom])
        return (e, g)

    def fromPixelToLL(self, px, zoom):
        e = self.zc[zoom]
        f = (px[0] - e[0]) / self.Bc[zoom]
        g = (px[1] - e[1]) / -self.Cc[zoom]
        h = RAD_TO_DEG * (2 * atan(exp(g)) - 0.5 * pi)
        return (f, h)





def createTileSet(outputPath, minx, miny, maxx, maxy, stylePath, minz, maxz):
    ret = {"success": False, "msg": "error"}
    try:
        outputPath = outputBasePath + outputPath
        stylePath = styleBasePath + stylePath


        if stylePath and outputPath:
            id = gettiles_task.create.delay(outputPath, minx, miny, maxx, maxy, stylePath, minz, maxz)
            ret['msg'] = "accepted task"
            ret['success'] = True
            ret['taskId'] = str(id)
        return json.dumps(ret)
    except Exception as e:
        ret["msg"] = str(e)
        return json.dumps(ret)



if __name__ == '__main__':
    # app.run(host = '0.0.0.0',port = 5000,use_reloader=False)
    # createTileSet("heilongjiang_test.mbtiles", 126.559291, 45.678115, 126.599804, 45.702577, "map_heilongjiang_new.xml", 10, 10)
    #bbox = (126.49291, 45.638115, 126.809804, 45.902577)
    bbox = (120.6, 43.2, 135.2, 53.7)
    # bbox = (120.705845, 43.036705, 135.55936, 53.826539)
    gprj = GoogleProjection(16)
    range_left_top = (bbox[0], bbox[3])
    range_right_down = (bbox[2], bbox[1])

    px0 = gprj.fromLLtoPixel(range_left_top, 10)
    px1 = gprj.fromLLtoPixel(range_right_down, 10)


    #统计总任务数
    taskNum = 0
    min_x = int(px0[0] / 256.0)
    max_x = int(px1[0] / 256.0) + 1
    for x in range(min_x, max_x):
        str_x = "%s" % x

        min_y = int(px0[1] / 256.0)
        max_y = int(px1[1] / 256.0) + 1

        for y in range(min_y, max_y):
            p0 = gprj.fromPixelToLL((x * 256.0, (y + 1) * 256.0), 10)
            p1 = gprj.fromPixelToLL(((x + 1) * 256.0, y * 256.0), 10)
            taskNum += 1

    print "总任务数为 ： ", taskNum


    min_x = int(px0[0] / 256.0)
    max_x = int(px1[0] / 256.0) + 1
    for x in range(min_x, max_x):
        str_x = "%s" % x

        min_y = int(px0[1] / 256.0)
        max_y = int(px1[1] / 256.0) + 1

        for y in range(min_y, max_y):
            p0 = gprj.fromPixelToLL((x * 256.0, (y + 1) * 256.0), 10)
            p1 = gprj.fromPixelToLL(((x + 1) * 256.0, y * 256.0), 10)

            str_y = "%s" % y
            tile_uri = str_x + '_' + str_y + ".mbtiles"
            createTileSet(tile_uri, p0[0], p0[1], p1[0], p1[1], "produce.xml", 0, 14)


