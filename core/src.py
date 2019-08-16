# -*- coding:utf-8 -*-
# Author: Jaylen
# date: 2019/8/15
from lib import common

user_info = {
    'name':None,
    'account':0
}
user_logger = common.get_logger('user')


def login():
    print("登录")
    if user_info['name']:
        print('您已经登录')
        return
    count = 0
    user_dic = common.reads()
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        password = input('请输入密码：').strip()

        if name in user_dic:
            if password == user_dic[name] and user_dic['locked'] == False:
                user_info['name'] = name
                print('登录成功！')
                user_logger.info('%s 登录成功' % name)
        else:
            count += 1
            print('输入错误或者已被锁定！')
            if count == 3:
                user_dic['locked'] = True
                common.save(user_dic)
                print('尝试过多，锁定')
                user_logger.info('%s 已被锁定' % name)
                break


def register():
    print('注册')
    if user_info['name']:
        print('您已经登陆')
        return
    user_dic = common.reads()
    while True:
        name = input('请输入名字:').strip()
        if name == 'q':
            break
        if name in user_dic:
            print('该用户名已存在！')
            break
        password = input('请输入密码').strip()
        conf_password = input('请确认密码').strip()
        if password == conf_password:
            account = input('请输入余额').strip()
            user_dic = {'name': name,
                        'password': password,
                        'account': account,
                        'locked': False,
                        'shoppingcart': {}}
            common.save(user_dic)

            user_logger.info('%s 注册成功' % name)


        else:
            print('两次密码不一致')


@common.login_auth
def shopping():
    print('购物')
    prod_list = [
        ['coffee', 10],
        ['chicken', 20],
        ['iphone', 8000],
        ['macPro', 15000],
        ['car', 100000]
    ]
    shoppingcart = {}
    cost = 0
    user_dic = common.reads()
    account = user_dic['account']
    while True:
        for i, prod in enumerate(prod_list):
            print('%s : %s ' % (i, prod))
        choice = input('请输入要购买的商品：').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= len(prod_list):
                continue
            prod_name = prod_list[choice][0]
            prod_price = prod_list[choice][1]
            if account >= prod_price:
                if prod_name in shoppingcart:
                    shoppingcart[prod_name]['count'] += 1
                else:
                    shoppingcart[prod_name] = {'price': prod_price, 'count': 1}
                account -= prod_price
                cost += prod_price
            else:
                print('余额不足')
        elif choice == 'q':
            if cost == 0:
                break
            print(shoppingcart)
            buy = input('确认购买吗？（y/n）').strip()
            if buy == 'y':
                user_dic['account'] = account,
                user_dic['shoppingcart'] = shoppingcart
                common.save(user_dic)

            else:
                print('您没买东西')
                break
        else:
            print('输入非法')


@common.login_auth
def repay():
    print('还款')


@common.login_auth
def withdraw():
    print('提现')

func_dic = {
    '1': login,
    '2': register,
    '3':repay,
    '4': withdraw,
    '5': shopping
}


def run():
    while True:
        print('''
        1、登录
        2、注册
        3、提现
        4、购物
        ''')
        choice = input('请选择:').strip()
        if choice in func_dic:
            func_dic[choice]()