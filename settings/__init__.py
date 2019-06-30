import os

if os.getenv('FLASK_SETTINGS') == 'production':
    from .prod_settings import *
elif os.getenv('FLASK_SETTINGS') == 'development':
    from .dev_settings import *