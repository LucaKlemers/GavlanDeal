from django.shortcuts import render
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth
from integration_utils.bitrix24.functions.call_list_method import call_list_method
from integration_utils.bitrix24.functions.api_call import api_call
from django.conf import settings
from operator import itemgetter
from django.core.signing import Signer
from django.utils.crypto import get_random_string
import qrcode
from .models import Product #, ProductID
import requests
from PIL import Image
import io
import base64

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
        token.call_api_method('crm.deal.add', {"fields": request.POST.dict()})
    return render(request, 'GavlanDealApp/add_deal.html')

@main_auth(on_cookies=True)
def generate_qr(request):
    token = request.bitrix_user_token
    if request.method == "POST":
        id = int(request.POST.dict()['id'])
        product = token.call_api_method('crm.product.get', params={"id": id})['result']

        name = product['NAME']
        descritpion = product['DESCRIPTION']
        image_url = "https://b24-klxrii.bitrix24.ru" + str(product['PROPERTY_44'][0]['value']['downloadUrl'])
        response = requests.get(image_url, stream=True)
        image = Image.open(io.BytesIO(response.content))
        image_path = f"GavlanDealApp\product_images\{id}.webp"
        image.save(f"GavlanDealApp\static\GavlanDealApp\product_images\{id}.webp")

        product_db, _ = Product.objects.get_or_create(product_id=id, defaults = {'product_name': name, 'product_description': descritpion, 'product_image': image_path})
        product_db.save()

        s = get_random_string(16)
        signer = Signer(salt=s)
        signed_id = signer.sign_object(id)
        qr_link = f"localhost:8003/product?id={signed_id}&s={s}"

        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(qr_link)
        qr.make(fit=True)
        qr_code_image = qr.make_image(fill_color="black", back_color="white")

        buffer = io.BytesIO()
        qr_code_image.save(buffer, format="PNG")
        qr_base64 = base64.b64encode(buffer.getvalue()).decode()

        context = {"qr_link": qr_link, "qr_code": f"data:image/png;base64,{qr_base64}" }

        return render(request, 'GavlanDealApp/generate_qr.html', context)
    return render(request, 'GavlanDealApp/generate_qr.html')

def product(request):
    signer = Signer(salt=request.GET.get('s'))
    id = int(signer.unsign_object(request.GET.get('id')))
    product = Product.objects.get(product_id=id)
    objects = Product.objects.all()
    for object in objects:
        print(object.product_image, object.product_name, object.product_id)
    name = product.product_name
    description = product.product_description
    image = product.product_image
    context = {"name": name, "description": description, "image": image}
    return render(request, 'GavlanDealApp/product.html', context)


@main_auth(on_cookies=True)
def product_list(request):
    token = request.bitrix_user_token
    fields = ["ID", "Наименование"]
    product_types = ["ID", "TITLE"]
    full_products = sorted(token.call_api_method("crm.product.list")['result'], key=itemgetter('ID'), reverse=True)
    products = []
    for product in full_products:
        values = []
        id = product["ID"]
        name = product["NAME"]
        values.append(id)
        values.append(name)
        products.append(values)
    context = {"fields": fields, "products": products,}
    return render(request, 'GavlanDealApp/product_list.html', context)

@main_auth(on_cookies=True)
def employees(request):
    token = request.bitrix_user_token
    users = token.call_api_method("im.department.colleagues.list")['result']
    print(users)
    employees = []
    context = {"employees": employees}
    return render(request, 'GavlanDealApp/employees.html', context)
