#!/usr/bin/env python
# -*- coding: utf-8 -*-


db_url='sqlite:///db.sqlite'

ref_pay_perc_1lvl=0 #столько получит от 1 уровная рефералов за оплату
ref_pay_perc_2lvl=0 #столько получит от 2 уровная рефералов за оплату
ref_view_pay_1lvl=0.80 #столько получит от 1 уровная рефералов за подписку
ref_view_pay_2lvl=0 #столько получит от 2 уровная рефералов за подписку
user_view_perc=0.40 #столько получит пользователь за вступление(проценты от стоимости установленной заказчиком)
min_out_pay=10 #минимальная сумма для вывода
min_post_cost=0.25 #минимальная стоимость 1 подписчика

number=998915066072
qiwi_token='1439b7d8043a1b8fdd85fd78ca61e1f4'

ya_number=410015879712650
ya_token='F852FB6DC5923691F1043FEBB52BF9E280571BF1569594A0D1EA32E6F28AF885' # 'F852FB6DC5923691F1043FEBB52BF9E280571BF1569594A0D1EA32E6F28AF885'

telegram_token='658374451:AAGhl6rcfaC8tlTOISWwiHrvLlT4JpILkio'


uah_to_rub=2.39
usd_to_rub=68.07
eur_to_rub=79.11

admins = [616352062,329892918]

tutorial_url = 'http://telegra.ph/'





WEBHOOK_HOST = '52.212.233.171'
WEBHOOK_PORT = 443
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_SSL_CERT = './webhook_cert.pem'
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'

WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)

WEBHOOK_URL_PATH = "/{}/".format(telegram_token)
