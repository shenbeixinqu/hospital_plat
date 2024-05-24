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
