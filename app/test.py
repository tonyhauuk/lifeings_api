from pymongo import MongoClient
from flask import jsonify
from flask import Flask
import json
import random
import uuid
from app.util.connect import Conn
import time
import datetime
import json
import urllib
import urllib.request as req
from app.util.models import Process

c = Conn()
p = Process()
app = Flask(__name__)

def checkExistUser1():
    db = c.connect()
    user = db.User
    n = int('13261593150')
    isExist = user.find_one({'mobile': n})

    s = getCol('City').find_one()
    print(s)

    #print(isExist)


    if isExist is None:
        result = 0
    else:
        result = 1

    c.close()

    return result

def getCol1(collection = None):
    if collection == None:
        return 2
    else:
        db = c.connect()
        name = db.get_collection(collection)
        c.close()
        return name



def insert1():
    c.connect()
    ss = "{'userName': 'wangxiao','userID':1,'email': 'wangxiao@estarinfo.net','mobile': '13261593150','password': '800915'," \
         "'birthday': '','city': 'Beijing', 'token': 'q938479r8uasfijda8shd9f8a9sdfha','expire': 1505121083000}"
    sql = json.dumps(ss)
    coll =  p.getCol('User')
    r = coll.insert(sql)
    print('ret status:  ' + r)
    c.close()

def ran():
    #r = random.randint(1000, 10000)
    r = uuid.uuid1()
    print(r)



def send():
    data = {}
    data['mobile'] = '13261593150'
    data['verify'] = str(random.randint(1000, 10000))
    #data['uuid'] = uuid.uuid1()

    params = urllib.parse.urlencode(data)
    url = 'http://www.estar360.com/lifeings/send_sms/sendsms.php?' + params
    ret = req.urlopen(url).read()
    result = ret.decode('utf-8')

    print(result)


def querySms(mobile):
    data = {}
    data['mobile'] = mobile

    params = urllib.parse.urlencode(data)
    url = 'http://www.estar360.com/lifeings/send_sms/sendsms.php?' + params
    ret = req.urlopen(url).read()
    result = ret.decode('utf-8')

    print(result)

def time2str():
    time1 = "2017-09-18 14:52:21"
    st = time.strptime(time1, "%Y-%m-%d %H:%M:%S")
    timeStamp1 = int(time.mktime(st))

    time2 = "2017-09-18 14:57:21"
    st1 = time.strptime(time2, "%Y-%m-%d %H:%M:%S")
    timeStamp2 = int(time.mktime(st1))

    timeStamp = timeStamp2 - timeStamp1

    print(timeStamp)


def getType():
    with app.app_context():
        validate = '8800'
        phone = '132615965465'
        obj = {'verification': validate, 'mobile': phone}
        data = jsonify(obj)

        print(type(obj))

def findfind():
    name = p.getCol('User')
    phone = '13261593150'
    dates = {'mobile': phone}
    condition =  {'verification': 1, '_id': 0}
    value = p.findByCondition(dates, condition, 'User')
    print(value['verification'])

def findStrIndex():
    m = '13811300140'
    n = m.find('1')
    print(n)

if __name__ == '__main__':
    findfind()
    #findStrIndex()
    #getType()
    #time2str()
    #send()

    #querySms(13261593150)

    #
    # if not name:
    #     print('not null')
    # else:
    #     print('is null')
    #time = datetime.datetime.now().strftime('%Y%m%d')
    #print(time)

    #send()
    #a = c.connect().City.find_one()
   # print(a)
    #ran()
   #insert()

    #connect()
    #r = checkExistUser()
   # print(r)






