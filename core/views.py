from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .services import *
import datetime

# Create your views here.
class transactionViewSet(APIView):
    def get(self,request,transaction_id):
        transation_instances = get_transations()
        product_ref_instances = get_product_ref()
        filter_data = {}
        for i in transation_instances:
            if i["transactionId"] == int(transaction_id):
                filter_data = i
        product_name = ""
        for h in product_ref_instances:
            product_name = get_product_name(h["productId"])
        del filter_data["productId"]
        filter_data["productName"] = product_name
        return JsonResponse(filter_data, safe=False)

class transactionSummaryByProductsViewSet(APIView):
    def get(self,request,last_n_days):
        trans_data = get_filtered_data(last_n_days)
        summery_data,city =get_summery_data()
        for j in summery_data:
            for k in trans_data:
                if j["productId"] == k["productId"]:
                    j["transactionAmount"].append(int(k["transactionAmount"]))
            j["totalAmount"] = int(sum((j["transactionAmount"])))
            del j["productId"]
            del j["cityName"]
            del j["transactionAmount"]
        filter_data = { "summary": summery_data}
        return JsonResponse(filter_data, safe=False)

class transactionSummaryByManufacturingCityViewSet(APIView):
    def get(self,request,last_n_days):
        trans_data = get_filtered_data(last_n_days)
        summery_data,city =get_summery_data()
        
        for j in summery_data:
            for k in trans_data:
                if j["productId"] == k["productId"]:
                    j["transactionAmount"].append(int(k["transactionAmount"]))
            j["totalAmount"] = int(sum((j["transactionAmount"]))) 
            for l in city:
                if l["cityName"] == j["cityName"]:
                    l["prod_wise_total"].append(j["totalAmount"])
                l["TotalAmount"] = sum(l["prod_wise_total"])
            del j["productId"]
            del j["transactionAmount"]
        for l in city:
            del l["prod_wise_total"]
        filter_data = { "summary": city}
         
        return JsonResponse(filter_data, safe=False)
    