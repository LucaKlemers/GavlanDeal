from django.shortcuts import render
from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth

from django.conf import settings

@main_auth(on_start=True, set_cookie=True)
def index(request):
    app_settings = settings.APP_SETTINGS
    user = request.bitrix_user
    user_name = user.first_name
    context = {"app_settings": app_settings, "user_name": user_name,}
    return render(request, 'GavlanDealApp/index.html', context)

