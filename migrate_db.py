"""
Migration example
"""

from playhouse.migrate import *

from tg.models import db

migrator = SqliteMigrator(db)

migrate(migrator.add_column("tgpost", "reposted_pictures", CharField(default="")))
