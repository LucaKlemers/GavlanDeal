DEBUG = True
ALLOWED_HOSTS = ['*']

from integration_utils.bitrix24.local_settings_class import LocalSettingsClass


APP_SETTINGS = LocalSettingsClass(
    portal_domain='b24-klxrii.bitrix24.ru',
    app_domain='127.0.0.1:8003',
    app_name='GavlanDeal',
    salt='wefiewofioiI(IF(Eufrew8fju8ewfjhwkefjlewfjlJFKjewubhybfwybgybHBGYBGF',
    secret_key='wefewfkji4834gudrj.kjh237tgofhfjekewf.kjewkfjeiwfjeiwjfijewf',
    application_bitrix_client_id='local.686fbec780ab95.71091991',
    application_bitrix_client_secret='dj6ItKtwfMrrZA98dDwtFK9Zte3gb1GuMqSS1juI6VWa5GIVpD',
    application_index_path='/',
)

DOMAIN = "localhost:8003"
