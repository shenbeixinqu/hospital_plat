import json
from flask import Blueprint, request, jsonify
from .modules import CMSHouse
from utils.return_methods import success_return, error_return
from exts import db
from auth import generate_auth_token


bp = Blueprint('back', __name__, url_prefix='/back')


# 登录
@bp.route('/login', methods=['POST'])
def login():
    username = request.values.get('username')
    password = request.args.get('password')
    token_byte = generate_auth_token(username)
    token_str = token_byte.decode('utf-8')
    print('token_str', token_str)
    data = {
        "code": 200,
        "msg": "success",
        "data": {
            "token": token_str
        }
    }
    return jsonify(data)


# 退出
@bp.route('/logout', methods=['POST'])
def logout():
    data = {
        "code": 200,
        "msg": "success",
    }
    return jsonify(data)


# 获取用户信息
@bp.route("/userInfo")
def user_info():
    token_name = request.args.get("token_value")
    data = {"code": 200, "msg": "success"}

    if token_name == "editor-token":
        data["data"] = {
            "roles": ["editor"],
            "ability": ["READ", "WRITE"],
            "username": "editor",
            "avatar": "https://i.gtimg.cn/club/item/face/img/2/16022_100.gif"
        }
    else:
        data["data"] = {
            "roles": ["admin"],
            "ability": ["READ", "WRITE", "DELETE"],
            "username": "admin",
            "avatar": "https://i.gtimg.cn/club/item/face/img/2/16022_100.gif"
        }
    return jsonify(data)


@bp.route('/thing_manage')
def thing_manage():
    pn = int(request.values.get("pn", 1))
    limit = int(request.values.get("limit", 10))
    key_word = request.values.get("k_word")
    query_all = CMSHouse.query.filter(CMSHouse.name.contains(key_word)).offset((pn - 1) * limit).limit(limit).all()
    total = CMSHouse.query.count()
    data = []
    for q in query_all:
        record = {
            "id": q.id,
            "name": q.name,
            "price": q.price,
            "deposit": q.deposit,
            "community": q.community,
            "address": q.address,
            "way": q.way,
            "towards": q.towards,
            "floor": q.floor,
            "area": q.area,
            "desc": q.desc,
            "mobile": q.mobile,
            "status": q.status,
        }
        data.append(record)
    return success_return(**{"data": data, "total": total})


@bp.route('/thing_edit', methods=['GET', 'POST'])
def thing_edit():
    data = request.get_data()
    data = json.loads(data)
    print('data', data)

    name = data['name']
    price = data['price']
    deposit = data['deposit']
    address = data['address']
    way = data['way']
    towards = data['towards']
    floor = data['floor']
    area = data['area']
    status = data['status']
    try:
        community = data['community']
    except:
        community = ""
    try:
        desc = data['desc']
    except:
        desc = ""
    try:
        mobile = data['mobile']
    except:
        mobile = ""
    if data['id']:
        h_id = data['id']
        house = CMSHouse.query.get(h_id)
        house.name = name
        house.price = price,
        house.deposit = deposit,
        house.community = community,
        house.address = address,
        house.way = way,
        house.towards = towards,
        house.floor = floor,
        house.area = area,
        house.desc = desc,
        house.mobile = mobile,
        house.status = status
    else:
        house = CMSHouse(
            name=name,
            price=price,
            deposit=deposit,
            community=community,
            address=address,
            way=way,
            towards=towards,
            floor=floor,
            area=area,
            desc=desc,
            mobile=mobile,
            status=status
        )
        db.session.add(house)
    db.session.commit()
    return success_return()


@bp.route('/thing_del', methods=['GET', 'POST'])
def thing_del():
    get_data = json.loads(request.get_data())
    print('11111', get_data)
    ids = get_data['ids']
    for h_id in ids:
        house = CMSHouse.query.get(h_id)
        db.session.delete(house)
    db.session.commit()
    return success_return()


@bp.route('/daily', methods=['GET'])
def daily():
    pn = int(request.values.get("pn", 1))
    limit = int(request.values.get("limit", 10))
    key_word = request.values.get("seleteVal")
    if key_word == "1":
        total = 17
        data = [
            {"time": "2024-04-30", "fk_count": 285, "ip_count": 268},
            {"time": "2024-04-30", "fk_count": 286, "ip_count": 284},
            {"time": "2024-04-30", "fk_count": 220, "ip_count": 215},
            {"time": "2024-04-30", "fk_count": 184, "ip_count": 173},
        ]
    else:
        total = 12
        data = [
            {"time": "2024-04-30", "fk_count": 2851, "ip_count": 2681},
            {"time": "2024-04-30", "fk_count": 2861, "ip_count": 2841},
            {"time": "2024-04-30", "fk_count": 2201, "ip_count": 2151},
            {"time": "2024-04-30", "fk_count": 1841, "ip_count": 1731},
        ]
    return success_return(**{"data": data, "total": total})


@bp.route('/header_data', methods=['POST'])
def header_data():
    data = {
        "registered_count": 42,
        "return_count": 40,
        "admission_count": 6
    }
    return jsonify({"datas": data})


@bp.route('/statistics_data', methods=['POST'])
def statistics_data():
    data = request.get_data()
    data = json.loads(data)
    type_val = data['type']
    if type_val == 'my':
        data = {
        "month_repeat_count": 19,
        "month_repeat_count_same": "12.3",
        "month_repeat_count_ring": "-10.5",
        "year_repeat_count": 4,
        "year_repeat_count_same": "15",
        "month_accept_count": 23,
        "month_accept_count_same": "-9.5",
        "month_accept_count_ring": "-15.2",
        "year_accept_count": 97,
        "year_accept_count_same": "24",
        "month_drug_income": "15426.65",
        "month_drug_income_same": "11",
        "month_drug_income_ring": "-2.5",
        "year_drug_income": "316712",
        "year_drug_income_same": "10.09"
    }
    elif type_val == 'room':
        data = {
            "month_repeat_count": 16,
            "month_repeat_count_same": "11.3",
            "month_repeat_count_ring": "-17.5",
            "year_repeat_count": 3,
            "year_repeat_count_same": "15",
            "month_accept_count": 17,
            "month_accept_count_same": "-9.5",
            "month_accept_count_ring": "-15.2",
            "year_accept_count": 82,
            "year_accept_count_same": "21",
            "month_drug_income": "15425.65",
            "month_drug_income_same": "12",
            "month_drug_income_ring": "-2.5",
            "year_drug_income": "217112",
            "year_drug_income_same": "10.09"
        }
    elif type_val == 'all':
        data = {
            "month_repeat_count": 31,
            "month_repeat_count_same": "12.3",
            "month_repeat_count_ring": "-10.5",
            "year_repeat_count": 6,
            "year_repeat_count_same": "15",
            "month_accept_count": 16,
            "month_accept_count_same": "-7.2",
            "month_accept_count_ring": "-11.4",
            "year_accept_count": 126,
            "year_accept_count_same": "52",
            "month_drug_income": "52426.65",
            "month_drug_income_same": "11",
            "month_drug_income_ring": "-2.5",
            "year_drug_income": "627712",
            "year_drug_income_same": "10.09"
        }
    return jsonify({"datas": data})


@bp.route('/rank_data', methods=['GET'])
def rank_data():
    data = [
        {"name": "张医生", "count": 1987},
        {"name": "赵医生", "count": 1815},
        {"name": "王医生", "count": 1726},
        {"name": "孙医生", "count": 1667},
        {"name": "李医生", "count": 1292},
        {"name": "陈医生", "count": 926},
        {"name": "章医生", "count": 871},
    ]
    return jsonify({"datas": data})


@bp.route('/distributed_data', methods=['GET'])
def distributed_data():
    data = {
        "consultation_count": 9,
        "disease_count": 10,
        "department_max_count": 7,
        "department_min_count": 6
    }
    return jsonify({"datas": data, "code": 200, "msg": "success"})


@bp.route('/distributed_apply', methods=['POST'])
def distributed_apply():
    return jsonify({"code": 201, "msg": "success"})


@bp.route('/warning_data', methods=['GET'])
def warning_data():
    data = {
        "admission_count": 110,
        "retreat_count": 110,
        "department_max_count": 7
    }
    return jsonify({"datas": data, "code": 200, "msg": "success"})


@bp.route('/warning_apply', methods=['POST'])
def warning_apply():
    return jsonify({"code": 200, "msg": "success"})


@bp.route('/stop_lock_data', methods=['GET'])
def stop_lock_data():
    data = {
        "if_switch": True,
        "error_one": 5,
        "lock_minute": 30,
        "error_two": 10,
        "not_login_day": 90
    }
    return jsonify({"datas": data, "code": 200, "msg": "success"})


@bp.route('/stop_lock_apply', methods=['POST'])
def stop_lock_apply():
    return jsonify({"code": 200, "msg": "success"})


@bp.route('/auto_logout_data', methods=['GET'])
def auto_logout_data():
    data = {
        "if_switch": True,
        "not_operate_minute": 10
    }
    return jsonify({"datas": data, "code": 200, "msg": "success"})


@bp.route('/auto_logout_apply', methods=['POST'])
def auto_logout_apply():
    return jsonify({"code": 200, "msg": "success"})


@bp.route('/month_report_data', methods=['GET'])
def month_report_data():
    data = {
        "if_switch": True,
        "person_report_date": 15,
        "department_report_date": 16,
        "all_report_date": 9
    }
    return jsonify({"datas": data, "code": 200, "msg": "success"})


@bp.route('/month_report_apply', methods=['POST'])
def month_report_apply():
    return jsonify({"code": 200, "msg": "success"})


@bp.route('/year_report_data', methods=['GET'])
def year_report_data():
    data = {
        "if_switch": True,
        "person_report_month": 4,
        "person_report_day": 21,
        "department_report_month": 3,
        "department_report_day": 30,
        "all_report_month": 8,
        "all_report_day": 16
    }
    return jsonify({"datas": data, "code": 200, "msg": "success"})


@bp.route('/year_report_apply', methods=['POST'])
def year_report_apply():
    return jsonify({"code": 200, "msg": "success"})


@bp.route('/chart_left_top_one', methods=['GET'])
def chart_left_top_one():
    data = [
        {"name": "脑科", "count": 2019},
        {"name": "神经内科", "count": 1987},
        {"name": "运动医学科", "count": 1815},
        {"name": "运动医学科", "count": 1726},
        {"name": "运动医学科", "count": 1667},
        {"name": "运动医学科", "count": 1292},
        {"name": "运动医学科", "count": 926},
        {"name": "运动医学科", "count": 912},
    ]
    return jsonify({"code": 200, "datas": data, "msg": "success"})


@bp.route('/chart_left_top_two', methods=['GET'])
def chart_left_top_two():
    data = [
        {"name": "张医生", "count": 2019},
        {"name": "王医生", "count": 1987},
        {"name": "李医生", "count": 1815},
        {"name": "赵医生", "count": 1726},
        {"name": "孙医生", "count": 1667},
        {"name": "陈医生", "count": 1292},
        {"name": "杜医生", "count": 926},
        {"name": "钱医生", "count": 912},
    ]
    return jsonify({"code": 200, "datas": data, "msg": "success"})


@bp.route('/chart_left_top_three', methods=['GET'])
def chart_left_top_three():
    data = [
        {"name": "张医生", "radio": "97.0"},
        {"name": "王医生", "radio": "96.4"},
        {"name": "李医生", "radio": "92.1"},
        {"name": "赵医生", "radio": "89.5"},
        {"name": "孙医生", "radio": "87.8"},
        {"name": "陈医生", "radio": "82.3"},
        # {"name": "杜医生", "radio": "80.9"},
        # {"name": "钱医生", "radio": "81.1"},
    ]
    return jsonify({"code": 200, "datas": data, "msg": "success"})


@bp.route('/chart_center_top', methods=['GET'])
def chart_center_top():
    data = [
        {"name": "辽宁省", "value": 90, "lineData": [80, 72, 68, 79, 73, 84, 89, 87, 90, 83, 78, 81]},
        {"name": "吉林省", "value": 60, "lineData": [20, 12, 38, 59, 43, 84, 19, 27, 40, 33, 18, 21]},
        {"name": "黑龙江省", "value": 15, "lineData": [40, 52, 68, 79, 23, 34, 39, 27, 10, 63, 78, 51]},
        {"name": "陕西省", 'value': 10, "lineData": [24, 42, 28, 89, 13, 24, 39, 47, 70, 53, 73, 71]},
        {"name": "山西省", "value": 12, "lineData": [80, 72, 68, 79, 73, 84, 89, 87, 90, 83, 78, 81]},
        {"name": "山东省", "value": 9, "lineData": [80, 72, 68, 79, 73, 84, 89, 87, 90, 83, 78, 81]},
        {"name": "河南省", "value": 35, "lineData": [80, 72, 68, 79, 73, 84, 89, 87, 90, 83, 78, 81]},
        {"name": "河北省", "value": 19, "lineData": [80, 72, 68, 79, 73, 84, 89, 87, 90, 83, 78, 81]},
        {"name": "广东省", "value": 4, "lineData": [80, 72, 68, 79, 73, 84, 89, 87, 90, 83, 78, 81]},
        {"name": "广西省", "value": 39, "lineData": [80, 72, 68, 79, 73, 84, 89, 87, 90, 83, 78, 81]},
    ]
    return jsonify({"code": 200, "datas": data, "msg": "success"})


@bp.route('/chart_right_top_one', methods=['GET'])
def chart_right_top_one():
    data = {
        "data_one": 1589,
        "data_two": 256,
        "data_three": 356,
        "data_four": 3652,
        "data_five": 29856,
    }
    return jsonify({"code": 200, "datas": data, "msg": "success"})


@bp.route('/chart_right_top_two', methods=['GET'])
def chart_right_top_two():
    data = {
        "disease_name": ["呼吸道感染", "高血压", "糖尿病", "支气管炎", "急性肠炎", "风湿"],
        "disease_count": [933, 850, 723, 680, 500, 300],
    }
    return jsonify({"code": 200, "datas": data, "msg": "success"})


@bp.route('/chart_left_bottom', methods=['GET'])
def chart_left_bottom():
    data = {
        # 配送量
        "deliveryData": [4.8, 7.1, 6.3, 6.8, 7.2, 8.1, 6.4, 6.6, 5.9, 9.1, 6.3, 6.0],
        # 化验量
        "assayData": [4.0, 4.3, 2.9, 3.1, 3.7, 4.0, 3.8, 4.6, 5.2, 4.7, 4.1, 2.9],
        # 检查项
        "examineData": [4.2, 5.8, 5.2, 6.1, 5.7, 4.1, 4.8, 5.8, 4.6, 4.2, 3.8, 4.7],
        # 治疗量
        "treatData": [1.7, 3.1, 1.9, 3.7, 3.5, 1.6, 2.2, 3.0, 1.7, 0.9, 2.6, 2.2],
        "deliveryValue": 18756,
        "assayValue": 14237,
        "examineValue": 12657,
        "treatValue": 16316,
    }
    return jsonify({"code": 200, "datas": data, "msg": "success"})


@bp.route('/chart_center_bottom', methods=['GET'])
def chart_center_bottom():
    data = {
        # 复诊
        "visit_data": ["8.2", "7.1", "8.4", "8.0", "5.9", "4.2", "8.1", "3.0", "7.0", "8.0", "8.1", "9.0"],
        # 接诊
        "admission_data": ["6.2", "8.1", "5.4", "6.0", "4.1", "2.6", "8.8", "4.7", "7.2", "6.4", "7.1", "9.6"],
    }
    return jsonify({"code": 200, "datas": data, "msg": "success"})


@bp.route('/chart_right_bottom', methods=['GET'])
def chart_right_bottom():
    data = [
        {"name": "网上复诊挂号", "value": 13},
        {"name": "网上治疗", "value": 7},
        {"name": "网上开具化验", "value": 20},
        {"name": "网上开具药品", "value": 33},
        {"name": "网上开具检查", "value": 27},
    ]

    return jsonify({"code": 200, "datas": data, "msg": "success"})
