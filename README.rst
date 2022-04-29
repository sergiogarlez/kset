Configure Access to Multiple Clusters
=====================================

This script allows access to multiple K8s clusters through the use of
configuration files. After your clusters, users, and contexts are
defined in one or more configuration files, you can quickly switch
between clusters by using the ``kset`` command.

Usage
-----

1- Place ``kset/`` wherever you prefer

2- Install requirements:

::

   $ pip3 install -r requirements.txt

Optional: install and enable `Powerline
fonts <https://github.com/powerline/fonts>`__ to render icons

3- Mark the script as executable:

::

   $ chmod +x kset/kset.py

4- Add this alias (or similar) to your ~/.bashrc.user (and
``source ~/.bashrc.user``)

.. code:: bash

   alias kset="<PATH_TO_kset>/kset/kset.py && source /tmp/.${USER}_aux"

4- Place your ``.conf`` files under ``kset/configs/``. ``.conf`` file
names are not taken into account since information about clusters is
retrieved automatically.

5- Invoke the tool and follow instructions. Example:

::

   $ kset

                                Available environments
   ┏━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
   ┃ # ┃ Cluster name   ┃ URL                                     ┃
   ┡━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
   │ 1 │ docker-desktop │ https://kubernetes.docker.internal:6443 │
   │ 2 │ cluster03      │ https://kubernetes.cluster:6443         │
   │ 3 │ cluster05      │ https://other.kubernetes.cluster:6443   │
   └───┴────────────────┴─────────────────────────────────────────┘

   Choose one (or press Enter for local) > 3

   👌 Loading  <PATH_TO_kset>/kset/configs/cluster05.conf

