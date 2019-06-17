from web.setting import setting
from web.setting.models import Driver, Device, Avatars
from flask import render_template, request, jsonify, current_app
from werkzeug.utils import secure_filename
from web import db
from sqlalchemy import exc
import ReturnMsg, json, logging, socket, os

@setting.route("/")
def index():
    return render_template("setting.html")

@setting.route("/driver/addone", methods=['POST'])
def addDriver():
    if request.method != 'POST':
        return jsonify(status = 1, msg = '无效请求')
    driverName = request.form['name']
    telephone = request.form['telephone']
    age = request.form['age']
    if(not driverName or not telephone):
        return jsonify(status = 1, msg = '请上传合理数据')

        try:
            driver = Driver(driverName, telephone, age)
            db.session.add(driver)
            db.session.add(avatar)
            db.session.commit()
        except exc.IntegrityError:
            return jsonify(status=1,msg="电话已被占用")
        return jsonify(status=0,msg="录入成功")
    else:
        return jsonify(status=1,msg="录入失败")

@setting.route("/driver/addavatar", methods=['POST'])
def addAvatar():
    telephone = request.form['telephone']
    avatar = request.files['avatars']
    avatarType = request.form['type']
    if not telephone or not avatar or not avatarType:
        return jsonify(status = 1, msg = '数据不完整')
    filePath = 'D:\\AsdaSystem\\zc\\'+secure_filename(avatar.filename)
    avatar.save(filePath)
    resutl = sendSocketMsg(filePath,telephone)
    current_app.logger.info(resutl)
    if resutl.RecordStatus == 'success':
        avatar = Avatars(telephone,filePath,avatarType)
        db.session.add(avatar)
        db.session.commit()
        return jsonify(status=0,msg="添加成功")
    else:
        os.remove(filePath)
        return jsonify(status=1,msg="添加失败")

@setting.route("/device/arguments", methods=['POST'])
def setDevice():
    data = request.get_json()
    current_app.logger.info(data)
    if 'telephone' not in data:
        return jsonify(status=1,msg= '无法查找该用户')
    args = db.session.query(Driver.id).all()
    current_app.logger.info(args[0][0])
    sql = 'replace into arguments ('
    if 'resolution' in data:
        sql += 'resolution,'
    if 'codeRate' in data:
        sql += 'codeRate,'
    if 'bitRate' in data:
        sql += 'bitRate,'
    if 'quality' in data:
        sql += 'quality,'
    if 'frame' in data:
        sql += 'frame ,'
    if 'ip' in data:
        sql += 'ip,'
    if 'port' in data:
        sql += 'port,'
    if 'gataway' in data:
        sql += 'gataway ,'
    sql += 'id) value('
    if 'resolution' in data:
        sql += data.resolution +','
    if 'codeRate' in data:
        sql += data.codeRate +','
    if 'bitRate' in data:
        sql += data.bitRate+','
    if 'quality' in data:
        sql += data.quality + ','
    if 'frame' in data:
        sql += data.frame +','
    if 'ip' in data:
        sql += data.ip+','
    if 'port' in data:
        sql += data.port +','
    if 'gataway' in data:
        sql += data.gataway + ','
    sql += 'id='+str(args[0][0])+')'
    db.session.execute(sql)
    current_app.logger.info(sql)
    return sql

# @setting.route("/sendsocket",methods=(['GET']))
def sendSocketMsg(filePath="testpath",telephone=""):
    address = ('127.0.0.1',2333)
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect(address)
    sc.send(str.encode({"ImagePath":filePath,"telephone":telephone}))
    data = sc.recv(512)
    result = bytes.decode(data)
    current_app.logger.info(result)
    sc.close()
    return json.loads(result)