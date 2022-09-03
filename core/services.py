import pandas as pd
import os
import datetime

# Create your tests here.

def get_transations():
    res = []

    dir_path = r'transactions/'

    transaction_file_list = os.listdir(dir_path)
    print(transaction_file_list)
    data = []
    for file in transaction_file_list:
        df = pd.read_csv('transactions/{}'.format(file))
        for d in range(len(df)):
            transaction_date = datetime.datetime.strptime(df.loc[d]["transactionDatetime"],"%d/%m/%Y %H:%M")
            dic = {
                "transactionId":int(df.loc[d]["transactionId"]),
                "productId":int(df.loc[d]["productId"]),
                "transactionAmount":int(df.loc[d]["transactionAmount"]),
                "transactionDatetime":transaction_date
            }
            data.append(dic)
    return data

def get_product_ref():
    df = pd.read_csv('ProductRef/ProductReference.csv')
    data = []
    for d in range(len(df)):
        dic = {
            "productId":df.loc[d]["productId"],
            "productName":df.loc[d]["productName"],
            "productManufacturingCity":df.loc[d]["productManufacturingCity"],
        }
        data.append(dic)
    return data


def get_product_name(productId):
    product_ref_instances = get_product_ref()
    for h in product_ref_instances:
        if h["productId"] == productId:
            return str(h["productName"])
        else:
            return ""

def get_filtered_data(last_n_days):
    trans_data = []
    transation_instances = get_transations()
    filter_date = datetime.datetime.now() - datetime.timedelta(int(last_n_days))
    for i in transation_instances:
            if filter_date <= i["transactionDatetime"]:
                trans_data.append(i)
    return trans_data

def get_summery_data():
    product_ref_instances = get_product_ref()
    city = []
    summery_data = []
    for h in product_ref_instances:
        data = {
            "productId":h["productId"],
            "productName":h["productName"],
            "cityName":h["productManufacturingCity"],
            "transactionAmount":[],
            "totalAmount":"",
        }
        summery_data.append(data)
        city.append({"cityName":h["productManufacturingCity"],"TotalAmount":"","prod_wise_total":[]})
    city = [i for n, i in enumerate(city) if i not in city[n + 1:]]
    return summery_data,city