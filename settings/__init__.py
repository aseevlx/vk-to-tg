import os
from .base_settings import *

if os.getenv('FLASK_SETTINGS') == 'prod':
    from .prod_settings import *
elif os.getenv('SETTINGS_MODULE') == 'dev':
    from .dev_settings import *