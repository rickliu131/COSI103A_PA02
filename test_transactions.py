"""
test_transactions runs unit and integration tests on the transactions module
"""
import pytest
from transactions import Transaction, to_tran_dict
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
    # Implemented by Yizhe
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
    empty_db.test_delete(id1)

@pytest.fixture
def med_db(small_db):
    # Implemented by Yizhe
    """ create a database with 10 more elements than small_db"""
    itemids = []
    # add 10 categories
    for i in range(10):
        s = str(i)
        tran = {'item': i,
               'amount': i,
               'category': 'any'+str(i),
               'date': '2001/03/3'+str(i),
               'description': 'good'+str(i),
               }
        itemid = small_db.add(tran)
        itemids.append(itemid)

    yield small_db
    # remove those 10 categories
    for j in range(10):
        small_db.test_delete(itemids[j])

@pytest.mark.simple
def test_to_trans_dict():
    # Implemented by Yizhe
    ''' teting the to_cat_dict function '''
    a = to_tran_dict((1,100,'any','2001/03/30','good123'))
    assert a['item']==1
    assert a['amount']==100
    assert a['category']=='any'
    assert a['date']=='2001/03/30'
    assert a['description']=='good123'
    assert len(a.keys())==5
    
@pytest.mark.add
def test_add(med_db):
    # Implemented by Yizhe
    ''' add a category to db, the select it, then delete it'''

    tran0 = {'item':1, 'amount':100, 'category': 'any','date':'2001/03/30', 'description':'good1!'}
    trans0 = med_db.select_all()
    itemid = med_db.add(tran0)
    trans1 = med_db.select_all()
    assert len(trans1) == len(trans0) + 1
    med_db.test_delete(itemid)

@pytest.mark.select_by_id
def test_select_by_id(med_db):
    # Implemented by Yuxuan
    assert med_db.select_by_id(1)['item'] == '1'
    assert med_db.select_by_id(3)['item'] == '3'
    assert med_db.select_by_id(9999) is None

@pytest.mark.select_by_year
def test_select_by_year(med_db):
    # Implemented by Siyu
    tran1 = {'item':1, 'amount':100, 'category': 'any','date':'2001/03/30', 'description':'good1!'}
    tran2 = {'item':2, 'amount':100, 'category': 'any','date':'2003/03/30', 'description':'good2!'}
    tran3 = {'item':3, 'amount':100, 'category': 'any','date':'2005/03/30', 'description':'good3!'}
    id1=med_db.add(tran1)
    id2=med_db.add(tran2)
    id3=med_db.add(tran3)
    dicts = med_db.select_by_year()
    for index,tran in enumerate(dicts):
        if index+1 < len(dicts):
            next = dicts[index+1]
            assert int(tran['date'][0:4])>=int(next['date'][0:4])
    med_db.test_delete(id1)
    med_db.test_delete(id2)
    med_db.test_delete(id3)
    
@pytest.mark.select_byMonth
def test_select_byMonth(empty_db):
    '''implemented by Emma'''
    '''tests if transactions program can select all items with a specified month'''
    tran0 = {'item':1, 'amount':100, 'category': 'any','date':'2001/03/10', 'description':'null'}
    tran1 = {'item':2, 'amount':200, 'category': 'any','date':'2001/02/10', 'description':'null'}
    tran2 = {'item':3, 'amount':300, 'category': 'any','date':'2001/01/10', 'description':'null'}
    empty_db.add(tran0)
    empty_db.add(tran1)
    empty_db.add(tran2)
    trans = empty_db.select_byMonth('02')
    for tran in trans:
         assert tran['date'] == '2001/02/10'

@pytest.mark.select_by_date
def test_select_by_date(empty_db):
    # Implemented by Yuxuan
    tran1 = {'item': 1, 'amount': 10, 'category': 'cat1', 'date': '2021/12/31', 'description': 'A'}
    tran2 = {'item': 2, 'amount': 20, 'category': 'cat1', 'date': '2022/01/01', 'description': 'B'}
    tran3 = {'item': 3, 'amount': 15, 'category': 'cat2', 'date': '2020/02/14', 'description': 'C'}
    empty_db.add(tran1)
    empty_db.add(tran2)
    empty_db.add(tran3)
    assert empty_db.order_by_date()[0]['date'] == '2022/01/01'
    assert empty_db.order_by_date()[1]['date'] == '2021/12/31'
    assert empty_db.order_by_date()[2]['date'] == '2020/02/14'

@pytest.mark.select_by_category
def test_select_by_category():
    pass