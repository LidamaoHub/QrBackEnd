# -*- coding: utf-8 -*-
# @Author: leeperfect
# @Date:   2017-04-30 19:58:02
# @Last Modified by:   leeperfect
# @Last Modified time: 2017-04-30 20:02:37
#coding=utf-8
from flask import Flask,request,render_template,Session,Response
from werkzeug import secure_filename
import os,json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)


@app.route("/aa",methods=["get"])
def index():
    result_json = json.dumps({"s":1})
    # Response
    resp = Response(result_json)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp






if __name__ == "__main__":
    app.run(debug=True)
