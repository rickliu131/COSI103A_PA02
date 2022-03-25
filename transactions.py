# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import sqlite3

# Implemented by Yizhe
def to_tran_dict(tran_tuple):
    tran = {'item': tran_tuple[0], 'amount': tran_tuple[1], 'category':
            tran_tuple[2], 'date': tran_tuple[3],
                'description': tran_tuple[4]}
    return tran
# Implemented by Yizhe
def to_tran_dict_list(tran_tuples):
    return [to_tran_dict(tran) for tran in tran_tuples]

class Transaction:
    """
    Transaction class that will store financial transactions with the fields
    """
    # Implemented by Siyu
    def __init__(self, dbfile):
        """ courses is a tuple of the courses being offered """
        self.dbfile = dbfile
        self.drop_data_table()
        self.create_data_table()
    # Implemented by Yizhe
    def create_data_table(self):
        """ create a table to store the Brandeis course data"""
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions (
                                item text, 
                                amount integer,
                                category text,
                                date text, 
                                description text)''')
        con.commit()
        con.close()

    # Implemented by Yizhe
    def drop_data_table(self):
        """ remove the table and all of its data from the database"""
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DROP TABLE IF EXISTS transactions''')
        con.commit()
        con.close()
    #Implemented by Siyu
    def select_by_year(self):
        """ Summarize by year in descending order """
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * FROM transactions ORDER BY date DESC")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list(tuples)

    def select_by_category(self):
        """ Summarize by category in alphabetic order; Implemented by Tianjun Cai"""
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * FROM transactions ORDER BY category")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list(tuples)

    # Implemented by Yizhe
    def select_all(self):
        """ return all of the categories as a list of dicts."""
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * FROM transactions")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list(tuples)

    # Implemented by Yizhe
    def add(self, tran):
        """ add a category to the categories table.
            this returns the rowid of the inserted element
        """
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?)", (tran['item'], tran['amount'], tran['category'],
                                                                   tran['date'], tran['description']))
        con.commit()
        con.close()
        return tran['item']
    # Implemented by Yizhe
    def test_delete(self, itemid):
        """
        add a category to the categories table.
        this returns the rowid of the inserted element
        """
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE item=(?);
        ''', (itemid,))
        con.commit()
        con.close()

    def select_by_id(self, item_id):
        # Implemented by Yuxuan
        # Select a transaction by its id
        # Return None if not found
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT * FROM transactions WHERE item=(?);''', (item_id,))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        if tuples:
            return to_tran_dict(tuples[0])
        return None

    def delete(self, item_id):
        # Implemented by Yuxuan
        # Delete a transaction, given its id
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions WHERE item=(?);''', (item_id,))
        con.commit()
        con.close()

    def order_by_date(self):
        # Implemented by Yuxuan
        # Sort transactions by date
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("SELECT * FROM transactions ORDER BY date DESC")
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list(tuples)

    #implemnted by Emma Xu
    def select_by_month(self, month):
        "lists all items with a specificed month, eg. enter 02, it will prints out all items of Feburary"
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        month = '%' + "/" + month + "/"+ '%'
        cur.execute("select * from transactions where date like (?)", ([month]))
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_tran_dict_list(tuples)


if __name__ == '__main__':
    trans = Transaction('tracker.db')
    print('1')
