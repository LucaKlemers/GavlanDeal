Учебное приложение для работы с CRM, основанное на Bitrix24 API и написанное на Python/Django.

Функционал:
1. Получение данных о сделках и товарах
2. Добавление сделок
3. Создание зашифрованных Django Signer ссылок и QR-кодов на индивидуальные странички товаров вне и без взаимодействия с Bitrix
4. Получение информации о сотрудниках и их отделах, звонкахб и иерархии начальников
5. Отображение адресов компаний на карте через YMap API
6. Загрузка и скачивание массивов контактов в разных форматах (на данный момент .xlsx, .csv)

Использует integration_utils/bitrix24 для взаимодействия с Bitrix24 API через Python.
Также на случай обновления копия хранится в /bitrix24.

При запуске требуется изменение данных в settings.py и local_settings.py на актуальные.

---

A CRM training application based on the Bitrix24 API and written in Python/Django.

Functionality:
1. Retrieving data about deals and products
2. Adding deals
3. Creating Django Signer-encrypted links and QR codes for individual product pages outside and without interaction with Bitrix
4. Obtaining information about employees, their departments, calls, and supervisor hierarchy
5. Displaying company addresses on a map via YMap API
6. Uploading and downloading contact arrays in different formats (currently .xlsx, .csv)

Uses integration_utils/bitrix24 for interaction with Bitrix24 API via Python.
A copy is stored in /bitrix24 in case of updates.

When launching, updating data in settings.py and local_settings.py with current information is required.
