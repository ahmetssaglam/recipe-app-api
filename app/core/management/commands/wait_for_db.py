"""
Django command to wait for the database to be available
"""
from time import sleep
import sys

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as PsOperationalError


class Command(BaseCommand):
    """
    Django command to wait for database
    """

    def add_arguments(self, parser):
        parser.add_argument("--poll_seconds", type=float, default=2)
        parser.add_argument("--max_retries", type=int, default=5)

    def handle(self, *args, **options):
        """
        Entrypoint for command
        :param args:
        :param options:
        :return:
        """

        max_retries = options["max_retries"]
        poll_seconds = options["poll_seconds"]

        self.stdout.write("Waiting for database...")
        db_up = None
        retry = 0
        while not db_up and retry < max_retries:
            try:
                self.check(databases=["default"])
                db_up = True
            except(PsOperationalError, OperationalError) as err:
                self.stdout.write(
                    "Database unavailable on attempt {attempt}/{max_retries}, waiting..."
                    .format(attempt=retry + 1, max_retries=max_retries))
                sleep(poll_seconds)
                retry += 1

        if db_up is None:
            self.stdout.write(self.style.ERROR("Database unavailable!"))
            sys.exit(1)
        else:
            self.stdout.write(self.style.SUCCESS("Database available!"))
