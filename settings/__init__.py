from .base_settings import *  # noqa
import os

if os.getenv("FLASK_SETTINGS") == "prod":
    from .prod_settings import *  # noqa
elif os.getenv("SETTINGS_MODULE") == "dev":
    from .dev_settings import *  # noqa
