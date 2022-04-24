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
## To see the full report of pylint in the file, run:
``` bash
pylint fileName.py
```
Here is an example with tracker.py with command 
``` bash
pylint tracker.py
```
in shell:

<img width="532" alt="Screen Shot 2022-04-24 at 1 45 46 PM" src="https://user-images.githubusercontent.com/62511665/164989453-db70785e-51d0-47d7-be64-89668a9e353e.png">

## To run pytest and see the result once we are in the correct directory, run:
``` bash
pytest
```
and see results as below:

<img width="565" alt="Screen Shot 2022-04-24 at 1 40 17 PM" src="https://user-images.githubusercontent.com/62511665/164989267-6003b112-0b71-408b-8e6c-e4b3dce7a87e.png">

## To interact with our tracker app, use the command
``` bash
python tracker.py
```
in shell:

<img width="502" alt="Screen Shot 2022-04-24 at 1 47 30 PM" src="https://user-images.githubusercontent.com/62511665/164989510-230d6d2e-f470-4f8b-b00d-1aee75d73742.png">
### for example, to add a category, you can simply call :
``` bash
2
``` 
and start to add the corresponding category name and description:

<img width="451" alt="Screen Shot 2022-04-24 at 1 51 35 PM" src="https://user-images.githubusercontent.com/62511665/164989677-a8edacb0-62a5-4c29-aacb-898590101be8.png">

### to see the category we just added, call
``` bash
1
``` 
and the category will display as below: 

<img width="402" alt="Screen Shot 2022-04-24 at 1 52 47 PM" src="https://user-images.githubusercontent.com/62511665/164989709-36c011fd-3906-4550-ae60-9ebfd85183d1.png">

Adding and displaying transactions are similar to that of category. Once a transaction is added, we can see the transaction by calling 
``` bash
4
``` 
and we can also summarize our transation by variousn factors. At the end, once all the operations are done, call 
``` bash
0
``` 
to quit.

Thanks for visiting and using our app! 
