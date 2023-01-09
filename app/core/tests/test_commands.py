"""
Test custom Django management commands
"""
from unittest.mock import patch

from psycopg2 import OperationalError as PsOperationalError

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch("core.management.commands.wait_for_db.Command.check")
# @patch("django.db.backends.base.base.BaseDatabaseWrapper.ensure_connection")
class CommandTests(SimpleTestCase):
    """
    Test commands
    """

    def test_wait_for_db_ready(self, patched_check):
        """
        Test waiting for database if database ready
        :param patched_check:
        :return:
        """
        patched_check.return_value = True
        call_command("wait_for_db")
        patched_check.assert_called_once_with(databases=["default"])

    @patch("time.sleep")
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """
        Test waiting for database when getting OperationalError
        :param patched_sleep:
        :param patched_check:
        :return:
        """
        patched_check.side_effect = [PsOperationalError] * 2 + [OperationalError] * 2 + [True]

        call_command("wait_for_db")

        self.assertEqual(patched_check.call_count, 5)
        patched_check.assert_called_with(databases=["default"])

