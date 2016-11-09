************
django CMS
************

Django CMS with standard configurations
including recommended addons and best practices. 

The setup process will automatically pull the `Explorer Theme
<https://github.com/divio/django-cms-explorer>`_ files into the project to
provide example templates and static files.

The following **essential addons** are available through this installation:

- `Aldryn Events <https://github.com/aldryn/aldryn-events>`_
- `Aldryn FAQ <https://github.com/aldryn/aldryn-faq>`_
- `Aldryn Jobs <https://github.com/aldryn/aldryn-jobs>`_
- `Aldryn News & Blog <https://github.com/aldryn/aldryn-newsblog>`_
- `Aldryn People <https://github.com/aldryn/aldryn-people>`_

There are also additional **recommended addons** available:

- `Aldryn Bootstrap 3 <https://github.com/aldryn/aldryn-bootstrap3>`_
- `Aldryn Forms <https://github.com/aldryn/aldryn-forms>`_
- `Aldryn Style <https://github.com/aldryn/aldryn-style>`_

Temp disabled
- `Aldryn Locations <https://github.com/aldryn/aldryn-locations>`_


************
Installation
************



Docker
------

For development setup, run the following:

1.First time setup: create env by  
`docker-machine create --driver virtualbox homepage`
1.`eval $(docker-machine env homepage)`
1.`docker-compose build`
1.`docker-compose up -d`
1.`docker-compose run web python manage.py migrate --noinput --no-initial-data`
1.`docker-compose run web python manage.py migrate --noinput`



Make
------

- run ``make docker`` which sets the docker image up and runs it in the background

For additional information checkout the ``Makefile``.


*****
Login
*****

You can login to the cms by appending ``/?edit`` to the url. The credentials are:

- Username: **admin**
- Password: **admin**
