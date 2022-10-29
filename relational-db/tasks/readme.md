# Relational DB tasks

## Task 1 - Select everything

Create a python script that can open ```data.csv``` and print out the contents

### Correct output:
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

## Task 2 - Select one column

Print out the list of product names from ```data.csv```

### Correct output:
```
    product_name
0          apple
1         banana
2           pear
3         orange
4          peach
5         cherry
6         tomato
7      starfruit
8           lime
9   potato-chips
10      cola can
11       cheddar
12    proscuitto
13  lolly snakes
```

## Task 3 - Select products under a price

Ask the user for a price, and then display a list of products, and their prices, that cost less than that.

### Correct output:
```
Price: 10.00
    product_name  price
0          apple   1.99
1         banana   2.49
2           pear   3.49
3         orange   5.99
4          peach   5.99
5         cherry   6.99
6         tomato   9.99
7           lime   4.49
8   potato-chips   2.99
9       cola can   5.00
10  lolly snakes   5.00
```

```Price: 3.00
   product_name  price
0         apple   1.99
1        banana   2.49
2  potato-chips   2.99
```

## Task 4 - Sorting

Show all products, their prices and quantity and sort by price and name in that order.

### Correct output:
```
    product_name   price  quantity
0          apple    1.99        10
1         banana    2.49        10
2   potato-chips    2.99        10
3           pear    3.49        10
4           lime    4.49        10
5       cola can    5.00        10
6   lolly snakes    5.00        10
7         orange    5.99        10
8          peach    5.99        10
9         cherry    6.99        10
10        tomato    9.99        10
11     starfruit   24.99        10
12       cheddar   30.00        10
13    proscuitto  110.00        10
```

## Task 5 - Averages

Find the average cost of all products with their prices below a user defined cost.

### Correct output:
```
Price: 10
   AVG(price)
0    4.946364
```

```
Price: 3
   AVG(price)
0        2.49
```

## Task 6 - Count