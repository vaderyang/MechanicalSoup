VSoup
==============

Home page
---------
Based on Mechnicalsoup

https://mechanicalsoup.readthedocs.io/

Overview
--------

A Python library for automating interaction with websites.
MechanicalSoup automatically stores and sends cookies, follows
redirects, and can follow links and submit forms. It doesn't do
JavaScript.

Based on Mechnicalsoup, I added more simple facilities for my own use.

Installation
------------

|Latest Version| |Supported Versions|

PyPy and PyPy3 are also supported (and tested against).


Download and install the development version from `GitHub <https://github.com/MechanicalSoup/MechanicalSoup>`__::

  pip install git+https://github.com/vaderyang/Vsoup

Installing from source (installs the version in the current working directory)::

  python setup.py install

(In all cases, add ``--user`` to the ``install`` command to
install in the current user's home directory.)


Documentation
-------------

The basic usage documentation is the same as mechnicalsoup which can be found at
https://mechanicalsoup.readthedocs.io/. You may want to jump directly to
the `automatically generated API
documentation <https://mechanicalsoup.readthedocs.io/en/latest/mechanicalsoup.html>`__.

Example
-------

From `<examples/expl_duck_duck_go.py>`__, code to get the results from
a DuckDuckGo search:

.. code:: python

    """Example usage of Vsoup to get the results from
    DuckDuckGo."""

    import vsoup

    # Connect to duckduckgo
    browser = vsoup.StatefulBrowser()
    browser.open("https://duckduckgo.com/")

    # Fill-in the search form
    browser.select_form('#search_form_homepage')
    browser["q"] = "MechanicalSoup"
    browser.submit_selected()

    # Display the results
    for link in browser.get_current_page().select('a.result__a'):
        print(link.text, '->', link.attrs['href'])

More examples are available in `<examples/>`__.

For an example with a more complex form (checkboxes, radio buttons and
textareas), read `<tests/test_browser.py>`__
and `<tests/test_form.py>`__.

Development
-----------

|Build Status| |Coverage Status|
|Requirements Status| |Documentation Status|
|CII Best Practices|

Instructions for building, testing and contributing to VSoup:
see `<CONTRIBUTING.rst>`__.
