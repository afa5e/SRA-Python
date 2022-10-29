# Week 2 — Relational Databases

Relational databases allow us to access data in a table, similarly to 
spreadsheets, but with commands such as "SELECT * from DATA". 

## First task

Create SQL queries to solve the problems in the tasks folder.

## Extension task: Store inventory and ordering database

Your task for this week is to design a database system that can record
the current inventory in a store and implement a system which the user 
can use to search for products, and add them to their cart and calculate
the total price.

### Stage 1: Welcome message

Your code after finishing this stage should print out the following 
welcome message:

```
Welcome to the Python Store.

To search for an item, use the command "s" followed by the name of the item.
To add an item to your cart, use the "a" command followed by the name and the quantity.
To remove an item, use "r" followed by the name and quantity.
To view you cart, use "v"
To calculate the total price, use "c"
To exit, use CTRL+D
```


### Stage 2: View products

#### 2.1: Show all products

##### Command:
> browse

##### Overview:
The browse command should print out all products, and their details.

##### Example:

```
    product_id  product_name   price          aisle  quantity
0            0         apple    1.99  fresh-produce        10
1            1        banana    2.49  fresh-produce        10
2            2          pear    3.49  fresh-produce        10
3            3        orange    5.99  fresh-produce        10
4            4         peach    5.99  fresh-produce        10
5            5        cherry    6.99  fresh-produce        10
6            6        tomato    9.99  fresh-produce        10
7            7     starfruit   24.99  fresh-produce        10
8            8          lime    4.49  fresh-produce        10
9            9  potato-chips    2.99         snacks        10
10          10      cola can    5.00         drinks        10
11          11       cheddar   30.00           deli        10
12          12    proscuitto  110.00           deli        10
13          13  lolly snakes    5.00         snacks        10
```

#### 2.2: Search

##### Command:
> s Item-name

##### Overview:
The user can use the command s followed by the name of the item to 
search for item names that matches the search term. If a product is 
found, print out the name, price and available quantity.

If multiple items in the database contains the search term, print 
them all out in a list with their prices and quantities.

##### Example:

###### One matching item:
```
s apple
apple: 10 in stock
```

###### No matches:
```
s mango
"mango" not found
```

#### 2.5: Viewing cart

##### Command
> v

##### Overview
The view command should list out the contents of the cart with the corresponding 
quantity and total price.

##### Example:

###### Empty cart:
```
v
Your cart is empty!
```

###### Cart with items:
```
v
Your cart:
apple | 10 | $19.90
banana | 5 | $12.45
```

### Stage 3: Purchasing

#### 3.1: Add to cart

##### Command:

> a Item-name quantity

##### Overview:
The user can try to add items to their cart with this command. If the 
item is in the store, and in stock, subtract the customer's order from 
the store and add them into the cart. If the order exceeds the available 
stock, add all that is in stock into their cart. If the item is not in 
stock, display an error message.

##### Example:

###### Adding one item
```
a apple 1
1 "apple" added to cart
```

###### Adding an item that does not exist
```
a mango 10
"mango" not found
```

###### Adding more items than what is in stock
```
a apple 100
You cannot order 100 of apple as there are only 10 in stock.
```

###### Adding an invalid amount to the cart
```
a apple -1
Invalid quantity
```

#### 3.2: Removing items from cart

##### Command:
> r Item-name quantity

##### Overview:

The user can remove items from their cart with this command. If they try to remove too many items, or an item that is not in the cart send an error message.

##### Examples:

###### Removing one item
```
r apple 10
10 "apple" removed from cart
```

###### Removing too many items
```
r apple 100
Not enough "apple" in cart
```

###### Removing an invalid amount of items
```
r apple banana
Invalid input
```