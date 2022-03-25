"""
test_transactions runs unit and integration tests on the transactions module
"""

import pytest
from transactions import Transaction


@pytest.fixture
def dbfile(tmpdir):
    """ create a database file in a temporary file system """
    return tmpdir.join('test_tracker.db')


@pytest.fixture
def empty_db(dbfile):
    """ create an empty database """
    db = Transaction(dbfile)
    yield db


@pytest.mark.select_by_category
def test_select_by_category():
    pass