from .utils import LinkNotFoundError
from .browser import Browser
from .form import Form, InvalidFormMethod
from .stateful_browser import StatefulBrowser, WebBrowser
#from .websuite import Google
from .__version__ import __version__


__all__ = ['StatefulBrowser', 'LinkNotFoundError', 'Browser', 'Form',
           'InvalidFormMethod', '__version__','WebBrowser', "Google"]
