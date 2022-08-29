"""
Django command to wait for db to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('waiting for db...')
        db_up = False
        MAX_TRY = 300
        tried = 0
        while db_up is False and tried < MAX_TRY:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('DB not available, waiting for 1 sec...')
                time.sleep(1)
                tried += 1

        if db_up is False:
            self.stdout.write('Exhausted attempts. DB is not available')
            raise OperationalError
        else:
            self.stdout.write('DB successfully started.')
