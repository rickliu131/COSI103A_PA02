import sqlite3
import csv
class Transaction():
    '''
    Transaction class that will store financial transactions with the fields
    '''
    def __init__(self,dbfile):
        ''' courses is a tuple of the courses being offered '''
        self.dbfile = dbfile
        self.drop_data_table()
        self.create_data_table()



    def create_data_table(self):
        ''' create a table to store the Brandeis course data'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions (
                                item text, 
                                amount int,
                                category text,
                                date text, 
                                description text)''')
        con.commit()
        con.close()

    def drop_data_table(self):
        ''' remove the table and all of its data from the database'''
        con = sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DROP TABLE IF EXISTS transactions''')
        con.commit()
        con.close()





if __name__ == '__main__':
    trans = Transaction('tracker.db')
    print('1')