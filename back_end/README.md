=================
django-bootstrap
=================

-----------------
Development setup
-----------------

Install required system packages:

.. code-block:: bash

    $ sudo apt-get install python3-pip
    $ sudo apt-get install python3.6-dev
    
Create www directory where project sites and environment dir

.. code-block:: bash

    $ mkdir /var/www && mkdir /var/envs && mkdir /var/envs/bin
    
Install virtualenvwrapper

.. code-block:: bash

    $ sudo pip3 install virtualenvwrapper
    $ sudo pip3 install --upgrade virtualenv
    
Add these to your bashrc virutualenvwrapper work

.. code-block:: bash

    export WORKON_HOME=/var/envs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6
    export PROJECT_HOME=/var/www
    export VIRTUALENVWRAPPER_HOOK_DIR=/var/envs/bin
    source /usr/local/bin/virtualenvwrapper.sh
    
Create virtualenv

.. code-block:: bash

    $ cd /var/envs && mkvirtualenv django_bootstrap --python=/usr/local/bin/python3.6
    
Install requirements for a project.

.. code-block:: bash

    $ cd /var/www/django_bootstrap && pip install -r requirements/local.txt
    
Migrate

.. code-block:: bash

    $ python manage.py migrate
    
Run tests

.. code-block:: bash

    $ python manage.py test
    
Run on local machine, swagger docs are available -  http://127.0.0.1:8000/api/v0/swagger/

.. code-block:: bash

    $ python manage.py runserver