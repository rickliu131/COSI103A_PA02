# PA02
Our app can perform following function for users:<br /> 
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

The script to test our file:<br />
#!/bin/sh <br />
pylint transactions.py <br />
pylint tracker.py <br />
pytest -v test_transactions.py<br />

OR type<br />
sh transcript.sh

To run pytest and see the result once we are in the correct directory, call:
``` bash
pytest
```
and see results as below:

<img width="565" alt="Screen Shot 2022-04-24 at 1 40 17 PM" src="https://user-images.githubusercontent.com/62511665/164989267-6003b112-0b71-408b-8e6c-e4b3dce7a87e.png">


