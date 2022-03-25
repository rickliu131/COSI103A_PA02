"""
test_transactions runs unit and integration tests on the transactions module
"""
import pytest
from transactions import Transaction, to_tran_dict_forTest
@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_trans.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db

@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    tran1 =  {'item':1, 'amount':100, 'category': 'any','date':'2001/03/30', 'description':'good1!'}
    tran2 = {'item':2, 'amount':1000, 'category': 'any','date':'2002/03/30', 'description':'good2!'}
    tran3 = {'item':3, 'amount':1000, 'category': 'any','date':'2003/03/30', 'description':'good3!'}
    id1=empty_db.add(tran1)
    id2=empty_db.add(tran2)
    id3=empty_db.add(tran3)
    yield empty_db
    empty_db.test_delete(id3)
    empty_db.test_delete(id2)
    empty_db.test_deletepyth(id1)

@pytest.mark.simple
def test_to_cat_dict():
    ''' teting the to_cat_dict function '''
    a = to_tran_dict_forTest((1,100,'any','2001/03/30','good123'))
    assert a['item']==1
    assert a['amount']==100
    assert a['category']=='any'
    assert a['date']=='2001/03/30'
    assert a['description']=='good123'
    assert len(a.keys())==5
    
@pytest.mark.add
def test_add(med_db):
    ''' add a category to db, the select it, then delete it'''

    tran0 = {'item':1, 'amount':100, 'category': 'any','date':'2001/03/30', 'description':'good1!'}
    trans0 = med_db.select_all()
    itemid = med_db.add(tran0)
    trans1 = med_db.select_all()
    assert len(trans1) == len(trans0) + 1
    med_db.test_delete(itemid)
    
    

@pytest.mark.select_by_category
def test_select_by_category():
    pass