Overall Guidelines
------------------

Bug reports, feature suggestions and pull requests welcome (on
GitHub). Security issues should be reported by email to the core
developers (emails available in the "Author" field of commits in the
Git history).

When editing please don't reformat code—this makes diffs and pull
requests hard to read.

Code should be flake8-clean and the test coverage is and should remain
100%. Add new tests whenever you add new features.

Hints on Development
--------------------

|Build Status| |Coverage Status|
|Requirements Status| |Documentation Status|
|CII Best Practices|

Installing dependencies and running tests can be done with:

::

    python setup.py test

The documentation can be generated and viewed with:

::

    pip install sphinx
    python setup.py build_sphinx
    firefox docs/_build/html/index.html

The documentation is generated from docstrings within ``*.py`` files,
and ``*.rst`` documentation files in the ``docs/`` directory.

You can develop against multiple versions of Python using
`virtualenv <https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments>`__:

::

    python3 -m venv .virtual-py3 && source .virtual-py3/bin/activate
    pip install -r requirements.txt -r tests/requirements.txt

and

::

    virtualenv -p python2 --no-site-packages .virtual-py2 && source .virtual-py2/bin/activate
    pip install -r requirements.txt -r tests/requirements.txt

After making changes, run pytest in all virtualenvs:

::

    source .virtual-py3/bin/activate
    pytest

    source .virtual-py2/bin/activate
    pytest

Installation should be as simple as:

::

    python setup.py install

Release Checklist
-----------------

Releases can be done only by people with sufficient priviledges on
GitHub and PyPI. Things to do are:

At each release:

- Make sure all changes are documented in ``docs/ChangeLog.rst``
- Update the version number to $v in
  ``vsoup/__version__.py``
- Remove the ``(in development)`` mention in ``docs/ChangeLog.rst``.
- git commit -m "Release $v"
- git tag v$ver
- git push origin master v$v
- Visit the `release page on GitHub
  <https://github.com/vaderyang/VSoup/releases>`__, copy
  the relevant section from ``docs/ChangeLog.rst`` to the release
  page.
- ``python setup.py sdist upload -r pypi`` or ``twine upload``. This
  requires a ``~/.pypirc`` with::

    [distutils]
    index-servers =
        pypi
    
    [pypi]
    username:<user>
    password:<password>

Right after the release:

- Update the version number to a ``x.y.z-dev`` number in
  ``vsoup/__version__.py``
- Create the ``(in development)`` section in ``docs/ChangeLog.rst``.
- ``git commit -m "Prepare for next release" && git push``
