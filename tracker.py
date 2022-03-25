#! /opt/miniconda3/bin/python3
"""
tracker is an app that maintains a list of personal
financial transactions.

It uses Object Relational Mappings (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, Category, will map SQL rows with the schema
  (rowid, category, description)
to Python Dictionaries as follows:

(5,'rent','monthly rent payments') <-->

{rowid:5,
 category:'rent',
 description:'monthly rent payments'
 }

Likewise, the ORM, Transaction will mirror the database with
columns:
amount, category, date (yyyymmdd), description

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/tracker.db

Note the actual implementation of the ORM is hidden and so it
could be replaced with PostgreSQL or Pandas or straight python lists

"""
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# from transactions import Transaction
from category import Category
from transactions import Transaction


transactions = Transaction('tracker.db')
category = Category('tracker.db')

# here is the menu for the tracker app

MENU = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
12. delete category
'''


def process_choice(choice):
    if choice == '0':
        return
    if choice == '1':
        cats = category.select_all()
        print_categories(cats)
    elif choice == '2':
        name = input("category name: ")
        desc = input("category description: ")
        cat = {'name': name, 'desc': desc}
        category.add(cat)
    elif choice == '3':
        print("modifying category")
        rowid = int(input("rowid: "))
        name = input("new category name: ")
        desc = input("new category description: ")
        cat = {'name': name, 'desc': desc}
        category.update(rowid, cat)
    elif choice == '4':
    # Implemented by Yizhe
        print("showing transactions")
        trans = transactions.select_all()
        print_transactions(trans)
    elif choice == '5':
    # Implemented by Yizhe
        print("adding transaction")
        item = input("item #: ")
        amount = int(input("Amount: "))
        cat = input("Category: ")
        date = input("Date (yyyy/mm/dd): ")
        while len(date) != 10 or date[4] != '/' or date[7] != '/':
            print('wrong date format')
            date = input("Date (yyyy/mm/dd): ")
        desc = input("Description: ")
        tran = {'item': item, 'amount': amount, 'category': cat, 'date': date, 'description': desc}
        transactions.add(tran)
    elif choice == '6':
        # Implemented by Yuxuan
        # Delete transaction
        print("delete a transaction")
        item_id = input("item #: ")
        if transactions.select_by_id(item_id):
            # if found
            transactions.delete(item_id)
            print(f"Transaction #{item_id} was successfully deleted.")
        else:
            # not found
            print(f"Transaction #{item_id} not found. Cannot be deleted.")
    elif choice == '7':
        # Implemented by Yuxuan
        # Summarize transactions by date
        print("Summarize transactions by date...")
        pass
    #Implemented by Siyu
    elif choice == '9':
        print("Summarize transactions by year")
        trans = transactions.select_by_year()
        print_transactions(trans)
    elif choice == '10':
        #Implemented by Tianjun Cai
        print("Summarize transactions by category")
        trans = transactions.select_by_category()
        print_transactions(trans)
    elif choice == '11':
        #Implemented by Tianjun Cai
        print(MENU)
    elif choice == '12':
        #Implemented by Tianjun Cai
        print("Delete category")
        rowid = int(input("category row id: "))
        category.delete(rowid)
    else:
        print("choice", choice, "not yet implemented")

    choice = input("> ")
    return choice


def toplevel():
    """ handle the user's choice """

    #read the command args and process them
    print(MENU)
    choice = input("> ")
    while choice != '0':
        choice = process_choice(choice)
    print('bye')


#
# here are some helper functions
#




def print_category(cat):
    print("%-3d %-10s %-30s" % (cat['rowid'], cat['name'], cat['desc']))


def print_categories(cats):
    print("%-3s %-10s %-30s" % ("id", "name", "description"))
    print('-' * 45)
    for cat in cats:
        print_category(cat)


def print_transaction(tran):
    print("%-20s %-20s %-20s %-20s %-20s" % (
        tran['item'], tran['amount'], tran['category'], tran['date'], tran['description']))


def print_transactions(trans):
    
    print("%-20s %-20s %-20s %-20s %-20s" % ("item_#", "amount", "category", "date", "description"))
    print('-' * 100)
    for tran in trans:
        print_transaction(tran)


# here is the main call!

toplevel()
