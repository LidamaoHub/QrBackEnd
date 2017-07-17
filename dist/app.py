# -*- coding: utf-8 -*-
# @Author: leeperfect
# @Date:   2017-04-30 22:03:00
# @Last Modified by:   leeperfect
# @Last Modified time: 2017-06-04 19:04:13
#coding=utf-8
from flask import Flask,request,render_template,session,Response,redirect
from werkzeug import secure_filename
from datetime import timedelta
import leancloud, json, time, pymongo,redis,os,requests
from bson.json_util import dumps
from bson.objectid import ObjectId
from pymongo import MongoClient
from StringIO import StringIO
import cStringIO, urllib2
from PIL import Image, ImageDraw, ImageFont
from config import conf
from bson import json_util
from bs4 import BeautifulSoup
from leancloud import Query, Object, User, LeanCloudError, File

redis_db = redis.StrictRedis(host=conf["redis"]['host'], port=conf['redis']['port'])
client = MongoClient(conf['mongo']['host'],conf['mongo']['port'])

loc_db = client.qr.locs
topic_db = client.qr.topics
rel_db = client.qr.rels
user_db = client.qr.users
reward_db = client.qr.rewards
mall_db = client.qr.malls
group_db = client.qr.groups
notice_db = client.qr.notices
block_db = client.qr.blocks

p_db = client.mall.products
o_db = client.mall.orders


app = Flask(__name__)
# CORS(app)
app.secret_key = 'F12Zr47j\3yX R~X@H!jLwf/T'
app.permanent_session_lifetime = timedelta(minutes=20)
SESSION_TYPE = 'filesystem'
# SESSION_COOKIE_HTTPONLY = False
s = session



bad_resp = Response(json.dumps({"err":True,"reason":"unexcept session"}))
bad_resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:8081'


leancloud.init(conf["leancloud"]["app_id"], master_key=conf["leancloud"]["master_key"])

# 小程序

def re(j):
    j["err"] = False
    result = json.dumps(j)
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:8081'
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    return resp
def re_err(j):
    j["err"] = True
    result = json.dumps(j)
    resp = Response(result)
    resp.headers['Access-Control-Allow-Origin'] = 'http://localhost:8081'
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    return resp
def insert_cover(db_name, dic):
    if not redis_db.exists(db_name + "_number"):
        redis_db.set(db_name + "_number", 0)
    up_no = int(redis_db.get(db_name + "_number")) + 1
    redis_db.set(db_name + "_number", up_no)
    timestamp = int(time.time())
    dic["id"] = up_no
    dic["create_time"] = timestamp
    dic["update_time"] = timestamp
    return dic
def get_list(r,need=[]):
    r = [x for x in r]
    if len(r):
        re = []
        if need:
            ret_list = [item for item in set(r[0]) if item in set(need)]
        else:
            ret_list = r[0].keys()
        # 取交集
        for x in r:
            z = {}
            for i in ret_list:
                if i == "_id":
                    z["_id"] = str(x["_id"])
                else:
                    z[i] = x[i]
            re.append(z)
        return re
    else:
        return []
def get_dict(r,need=[]):
    if r:
        if need:
            ret_list = [item for item in set(r.keys()) if item in set(need)]
        else:
            ret_list = r.keys()
        z = {}
        for i in ret_list:
            if i == "_id":
                print i

                z["_id"] = str(r["_id"])
                print z["_id"],type(z["_id"])
            else:
                z[i] = r[i]
        print z
        return z
    else:
        return None


# 装饰器

def check_session(func):
    def wrapper(*args, **kw):
        if "username" not in s:
            return re_err({})
        else:
            return func(*args, **kw)
    wrapper.func_name = func.func_name
    return wrapper


@app.route("/",methods=["GET","POST"])
def index():
    # if "username" not in s:
    return render_template("index.html")
    
@app.route("/check",methods=["GET","POST"])
@check_session
def check():
    return re({})

@app.route("/login",methods=["GET","POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    # 大型偷懒写法
    try:
        g_info = group_db.find({"username":username,"password":password})
        useful_key = ["username","id","open_id"]

        if g_info.count():
            for x in useful_key:
                if x in g_info[0]:
                    s[x] = g_info[0][x]
            s["_id"] = str(g_info[0]["_id"])

            return re({"err":False})
        else:
            return re({"err":True,"reason":"错误的账号密码"})
    except:
        return bad_resp
@app.route("/regist",methods=["POST"])
def regist():
    username = request.form["username"]
    password = request.form["password"]
    a = {"aa":1}
    client.a.locs.insert(a)

    try:
        user_info = group_db.find({"username":username,"password":password})
        if user_info.count():
            s["username"] = username
            s["_id"] = str(user_info[0]["_id"])

            # content = [x for x in user_info][0]
            return re({"reason":"已注册"})
        else:
            u = insert_cover("users",{
            "username":username,
            "password":password,
            "loc_list":[],
            "open_id":"",
            "loc_amount":conf["amount"]
            })
            g_id = str(group_db.insert(u))
            s["username"] = username
            s["_id"] = g_id
            return re({})
    except Exception,e:
        print e
        return re_err({"reason":str(e)})

@app.route("/add_loc",methods=["POST"])
@check_session
def add_loc():
    info = {
        "loc_name":"新建地点",
        "creator" : s["_id"],
        "column" : ["time_line","reward","mall"],
        "content":"示例介绍",
        "img_list":[],
        "reward_content":"感谢你的赞赏",
        "cover":{},
        "reward_type":0,
        "gift_list":[],
        "loc_list":["time_line","reward","mall"],
        "state":0
    }
    loc_id = str(loc_db.insert(insert_cover("locs",info)))
    notice_db.insert(insert_cover("notices",{"content":"","loc_id":loc_id}))
    return re({"loc_id":loc_id})

@app.route("/get_loc",methods=["GET","POST"])
@check_session
def get_loc():
    loc_id = request.form["loc_id"]
    
    loc = get_dict(loc_db.find_one(ObjectId(loc_id)))
    if loc:
        return re({"loc_info":loc})
    else:
        return re_err({})
@app.route("/get_locs",methods=["GET","POST"])
@check_session
def get_locs():
    group_id = s["_id"]
    loc_list = get_list(loc_db.find({"creator":group_id}))
    return re({"locs":loc_list})

@app.route("/get_topics",methods=["GET","POST"])
@check_session
def get_topics():
    group_id = s["_id"]
    loc_id = request.form["loc_id"]
    loc = loc_db.find({"_id":ObjectId(loc_id),"creator":group_id})
    if loc.count():
        try:
            group_loc_id = str(loc[0]["id"])
            topic_list = get_list(topic_db.find({"loc_id":group_loc_id,"state":0}))
            return re({"topics":topic_list})
        except Exception,e:
            print e
            return re_err({})
    else:
        return re_err({})

   
      

@app.route("/update_loc",methods=["POST"])
@check_session
def update_loc():
    loc_update = json.loads(request.form["loc_info"])
    loc_id = request.form["loc_id"]
    loc = loc_db.find_one({"_id":ObjectId(loc_id),"creator":session["_id"]})
    if not loc:
        return re_err({})
    loc_safe = {}
    for x in ["loc_name","column","content","img_list","reward_content","reward_type","gift_list","cover","loc_list"]:
        if x in loc_update:
            loc_safe[x] = loc_update[x]

    loc_db.update({"_id":ObjectId(loc_id)},{"$set":loc_safe})

    return re({})

@app.route("/upload_img",methods=["POST"])
@check_session
def upload_img():
    upload_file = request.files["files"]
    f = leancloud.File(upload_file.filename, data=upload_file.stream)
    f.save()
    url_little = f.url+"?imageView2/2/w/100"
    file = urllib2.urlopen(url_little)
    tmpIm = cStringIO.StringIO(file.read())
    im = Image.open(tmpIm)

    w,h = im.size
    rel_w = conf['image']['max_width']
    rel_h = rel_w/100*h
    
    
    re_dic = {"url":f.url,"src": f.url,"w":rel_w,"h":rel_h}

    return re(re_dic)

@app.route("/get_qr",methods=["GET","POST"])
@check_session
def get_qr():
    loc_id = str(request.form["loc_id"])
    url = "http://cli.im/api/qrcode/code?text=//%s/loc/%s&mhid=shbPWlvvmckhMHcsKdVcPKs" %(conf["server"]["server_name"],loc_id)
    h = "http:"+BeautifulSoup(requests.get(url).content).select(".qrcode_plugins_box_body img")[0].attrs["src"]
    return re({"url":h})

@app.route("/get_qr_url",methods=["GET","POST"])
def get_qr_url():
    url = request.form["redirect_url"][5:]
    url = "http://cli.im/api/qrcode/code?text=%s&mhid=shbPWlvvmckhMHcsKdVcPKs" %url
    h = "http:"+BeautifulSoup(requests.get(url).content).select(".qrcode_plugins_box_body img")[0].attrs["src"]
    return re({"url":h})
    

    
@app.route("/del_topic",methods=["POST"])
@check_session
def del_topic():
    # 检查是否是creator
    group_id = s["_id"]
    topic_id = request.form["obj_id"]
    topic = topic_db.find_one(ObjectId(topic_id))
    if topic:
        topic_loc_id  = topic["loc_id"]
        topic_info = loc_db.find_one({"creator":group_id,"id":topic_loc_id})
        if topic_info:
            topic_db.update({"_id":ObjectId(topic_id)},{"$set":{"state":2}})
            return re({})
    return re_err({})
@app.route("/del_user",methods=["GET","POST"])
@check_session
def del_user():
    user_id = int(request.form["user_id"])
    loc_id = request.form["loc_id"]
    location_id = str(loc_db.find_one(ObjectId(loc_id))["id"])
    block_db.insert(insert_cover("users",{"user_id":user_id,"loc_id":loc_id,"state":0}))
    topic_db.update({"user_id":user_id,"loc_id":location_id},{"$set":{"state":1}},multi=True)
    return re({})
@app.route("/get_block_user",methods=["GET","POST"])
def get_block_user():
    loc_id = request.form["loc_id"]
    block_list = get_list(block_db.find({"loc_id":loc_id}))
    for x in block_list:
        user_info = get_dict(user_db.find_one({"id":x['user_id'],"state":0}))
        x["user_info"] = user_info
    print block_list
    return re({"block_list":block_list})
@app.route("/unblock_user",methods=["GET","POST"])
def unblock_user():
    user_id = int(request.form["user_id"])
    loc_id = request.form["loc_id"]
    location_id = str(loc_db.find_one(ObjectId(loc_id))["id"])
    block_db.update({"user_id":user_id},{"$set":{"state":1}})

    topic_db.update({"user_id":user_id,"loc_id":location_id,"state":1},{"$set":{"state":0}},multi=True)
    return re({})
    

  
    




@app.route("/get_notice",methods=["GET","POST"])
def get_notice():
    loc_id = request.form["loc_id"]
    print loc_id
    try:
        notice = notice_db.find_one({"loc_id":loc_id})
        content = notice["content"]
    except:
        notice_db.insert(insert_cover("notices",{"content":"","loc_id":loc_id}))
        content = ""
    return re({"content":content})
    
@app.route("/update_notice",methods=["GET","POST"])
def update_notice():
    loc_id = request.form["loc_id"]
    content = request.form["content"]
    print content
    notice_db.update({"loc_id":loc_id},{"$set":{"content":content}})
    

    return re({})
@app.route("/get_group_info",methods=["GET","POST"])
@check_session
def get_group_info():
    z = {}
    for x in s:
        z[x] = s[x]
    return re({"s":z})
    


@app.route("/get_author_open_id/<group_id>",methods=["GET","POST"])
@check_session
def get_author_open_id(group_id):
    group_id = int(group_id)
    try:
        code = request.args['code']
        open_id = request.args['open_id']
        group_db.update({"id":group_id},{"$set":{"open_id":open_id}})
        s["open_id"] = open_id
        return re({"message":"绑定成功"})

    except Exception,e:
        print e
        return re_err({})
    
@app.route("/change_online_type",methods=["GET","POST"])
@check_session
def change_online_type():
    state = int(request.form["state"])
    loc_id = int(request.form["loc_id"])
    print "xxx",group_db.find_one(ObjectId(s["_id"]))
    loc_amount = int(group_db.find_one(ObjectId(s["_id"]))["loc_amount"])
    loc_amount1 = loc_db.find({"creator":s["_id"],"state":1}).count()
    if state==1 and loc_amount1>=loc_amount:
        return re_err({"reason":"你的上线次数达到限额","type":1})
    else:
        c = loc_db.update({"id":loc_id,"creator":s["_id"]},{"$set":{"state":state}})
        if c["updatedExisting"]:
            return re({})
        else:
            return re_err({"reason":"发生程序错误","type":0})
    
# mall

@app.route("/create_p",methods=["GET","POST"])
@check_session
def create_p():
    loc_id = request.form["loc_id"]
    loc_i = loc_db.find_one(ObjectId(loc_id))['id']
    default_p = {
    "p_name": "未命名商品",
    "p_intro": "未填写介绍",
    "loc_obj_id":loc_id,
    "loc_id":loc_i,
    "p_cover": {
    "url":"",
    "name":"封面"
    },
    "state":0,
    "p_type": [
    {
        "name": "默认分类",
        "charge": 0
    }]
    }
    i = str(p_db.insert(insert_cover("product",default_p)))
    return re({"_id":i})






@app.route("/update_p",methods=["GET","POST"])
@check_session
def update_p():
    safe_list = ["p_name","p_intro","p_cover","state","p_type","state","id","create_time","update_time","loc_obj_id","loc_id"]
    update_info = json.loads(request.form["info"])
    print update_info
    p_id = request.form["_id"]
    safe_dic = {}
    for x in safe_list:
        if x in update_info:
            safe_dic[x] = update_info[x]
    p_db.update({"_id":ObjectId(p_id)},safe_dic)
    return re({})

@app.route("/get_p_list",methods=["GET","POST"])
@check_session
def get_p_list():
    obj_id = request.form["obj_id"]
    l = get_list(p_db.find({"state":0,"loc_obj_id":obj_id}))
    return re({"p_list":l})
@app.route("/get_p",methods=["GET","POST"])
def get_p():
    p_id = request.form["_id"]
    p = get_dict(p_db.find_one(ObjectId(p_id)))

    return re({"p":p})
    

        
@app.route("/get_order_list",methods=["GET","POST"])
@check_session
def get_order_list():
    obj_id = request.form["obj_id"]
    o_l = get_list(o_db.find({"state":0,"loc_obj_id":obj_id}))

    return re({"order_list":o_l})

@app.route("/del_order",methods=["GET","POST"])
def del_order():
    order_id = request.form["order_id"]
    o_db.update({"_id":ObjectId(order_id)},{"$set":{"state":1}})
    return re({})
# end mall

if __name__ == "__main__":
    app.run(debug=True,port=3333)
