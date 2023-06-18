BitLinker
=====

BitLinker - консольная утилита для сокращения длинных ссылок, через онлайн-сервис Bitly. 
Создана в рамках задания третьего урока из курса `API веб-сервисов` на сайте https://dvmn.org.  


Установка
----------

Для установки и обновления зависимостей используйте `pip`_:

.. code-block:: text

    $ pip install -r requirements.txt



Примеры использлвания
----------------

.. code-block:: text

    $ python main.py https://mozilla.org
      * Битлинк -- https://mzl.la/3C9aju6

    $ python main.py https://mzl.la/3C9aju6
      * Количество переходов по битлинку -- 8

Ссылки
-----

-   Ссылка на урок: https://dvmn.org/modules/web-api/