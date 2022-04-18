CODECipher
----------

☯️ **codecipher** is package for cipher utilities.

Developed in 🐍 `python <https://www.python.org/>`_ code.

|codecov| |circleci|

.. |codecov| image:: https://codecov.io/gh/electux/codecipher/branch/dev/graph/badge.svg
   :target: https://codecov.io/gh/electux/codecipher

.. |circleci| image:: https://circleci.com/gh/electux/codecipher/tree/main.svg
   :target: https://circleci.com/gh/electux/codecipher/tree/main

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|codecipher python checker| |codecipher python package|

|codecipher github issues| |codecipher documentation status|

|codecipher github contributors|

.. |codecipher python checker| image:: https://img.shields.io/github/workflow/status/electux/codecipher/codecipher_python_checker?style=flat&label=codecipher%20python%20checker
   :target: https://github.com/electux/codecipher/actions/workflows/codecipher_python_checker.yml

.. |codecipher python package| image:: https://img.shields.io/github/workflow/status/electux/codecipher/codecipher_package_checker?style=flat&label=codecipher%20package%20checker
   :target: https://github.com/electux/codecipher/actions/workflows/codecipher_package_checker.yml

.. |codecipher github issues| image:: https://img.shields.io/github/issues/electux/codecipher.svg
   :target: https://github.com/electux/codecipher/issues

.. |codecipher github contributors| image:: https://img.shields.io/github/contributors/electux/codecipher.svg
   :target: https://github.com/electux/codecipher/graphs/contributors

.. |codecipher documentation status| image:: https://readthedocs.org/projects/codecipher/badge/?version=latest
   :target: https://codecipher.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

Used next development environment

|ubuntu linux os|

.. |ubuntu linux os| image:: https://raw.githubusercontent.com/electux/ats_utilities/dev/docs/ubuntuxis.png

|ats_utilities python3 build|

.. |ats_utilities python3 build| image:: https://img.shields.io/github/workflow/status/electux/ats_utilities/ats_utilities_python3_build?style=flat&label=ats_utilities%20python3%20build
   :target: https://github.com/electux/ats_utilities/actions/workflows/ats_utilities_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/electux/codecipher/releases

To install **codecipher** 📦 type the following

.. code-block:: bash

    tar xvzf codecipher-x.y.z.tar.gz
    cd codecipher-x.y.z/
    # pyton3
    pip3 install -r requirements.txt
    python3 -m build -s --no-isolation --wheel
    pip3 install codecipher-x.y.z-py3-none-any.whl

or old fashioned way

.. code-block:: bash

    tar xvzf codecipher-x.y.z.tar.gz
    cd codecipher-x.y.z/
    # pyton3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info

You can use Docker to create image/container, or You can use pip to install 📦

.. code-block:: bash

    # python3
    pip3 install codecipher

|github docker checker|

.. |github docker checker| image:: https://img.shields.io/github/workflow/status/electux/codecipher/codecipher_python3_build?style=flat&label=codecipher%20python3%20build
   :target: https://github.com/electux/codecipher/actions/workflows/codecipher_python3_build.yml

Dependencies
-------------

**codecipher** requires next modules and libraries

* None

Package structure
------------------

**codecipher** is based on OOP.

🧰 Package structure

.. code-block:: bash

    codecipher/
    ├── a1z52n62/
    │   ├── decode.py
    │   ├── encode.py
    │   └── __init__.py
    ├── atbs/
    │   ├── decode.py
    │   ├── encode.py
    │   ├── __init__.py
    │   └── lookup_table.py
    ├── b64/
    │   ├── decode.py
    │   ├── encode.py
    │   └── __init__.py
    ├── caesar/
    │   ├── decode.py
    │   ├── encode.py
    │   └── __init__.py
    ├── __init__.py
    ├── vernam/
    │   ├── decode.py
    │   ├── encode.py
    │   └── __init__.py
    └── vigenere/
        ├── decode.py
        ├── encode.py
        ├── __init__.py
        ├── key_generator.py
        └── lookup_table.py

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2021 by `electux.github.io/codecipher <https://electux.github.io/codecipher>`_

**codecipher** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/electux/codecipher/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
