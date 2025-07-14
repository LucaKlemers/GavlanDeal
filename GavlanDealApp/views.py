from django.shortcuts import render
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from integration_utils.bitrix24.functions.call_list_method import call_list_method
from integration_utils.bitrix24.functions.api_call import api_call
from django.conf import settings
from operator import itemgetter
import requests

@main_auth(on_start=True, set_cookie=True)
def index(request):
    app_settings = settings.APP_SETTINGS
    user = request.bitrix_user
    user_name = user.first_name
    context = {"app_settings": app_settings, "user_name": user_name,}
    return render(request, 'GavlanDealApp/index.html', context)


@main_auth(on_cookies=True)
def last_deals(request):
    token = request.bitrix_user_token
    # full_deals = sorted(call_list_method(token, 'crm.deal.list', ['select => ["ID", "TITLE", "OPPORTUNITY", "TAX_VALUE", "BEGINDATE", "CLOSEDATE", "UF_CRM_1752242366887"]']), key=itemgetter('LAST_ACTIVITY_TIME'), reverse=True)[:10]
    fields = ["ID", "Наименование", "Валюта", "Сумма", "Налог",
             # "Клиент",
              "Начало", "Конец",  "Скидка(%)"]
    deal_types = ["ID", "TITLE", "CURRENCY_ID", "OPPORTUNITY", "TAX_VALUE", "BEGINDATE", "CLOSEDATE", "UF_CRM_1752242366887"]
    full_deals = sorted(token.call_api_method("crm.deal.list")['result'], key=itemgetter('LAST_ACTIVITY_TIME'), reverse=True)[:10]
    deals = []
    for deal in full_deals:
        id= {'ID': deal["ID"]}
        real_deal = token.call_api_method('crm.deal.get', params=id)['result']
        values = []
        for value in real_deal:
            if value in deal_types:
                values.append(real_deal[value])
            #elif value == "CONTACT_ID":
            #    values.append(call_list_method(token, "crm.contact.get", fields=[int(deal[value])])[1]['NAME'])
        deals.append(values)
    context = {"fields": fields, "deals": deals,}
    return render(request, 'GavlanDealApp/last_deals.html', context)

@main_auth(on_cookies=True)
def add_deal(request):
    token = request.bitrix_user_token
    if request.method == "POST":
        print(request.POST.dict())
        token.call_api_method('crm.deal.add', {"fields": request.POST.dict()})
    return render(request, 'GavlanDealApp/add_deal.html')