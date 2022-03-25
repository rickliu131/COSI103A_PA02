# PA02
Our app can perform following function for users:\n 
0. quit
1. show categories
2. add category
3. modify category
4. show transactions: show all the transactions stored in the database
5. add transaction: add one new transaction into the database
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

The script to test our file:
#!/bin/sh
pylint transactions.py
pylint tracker.py
pytest -v test_transactions.py

OR type
sh transcript.sh
