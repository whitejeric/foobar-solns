# foobar-solns
My solutions to googles old foobar challenges, lotta fun so far!

Reduced questions:
1. make a string of primes concatenated one after the other till it has length i+5 then return the last 5 digits of the string
2. take a list of positive and negative integers, find the maximum product of their entries
3. If a knight is on square x_ij, what's the minimum number of moves to get to y_kl
4. given a list of integers find all tuples (x,y,z) st. x|y|z and the indices of x and z are less than or greater than y's respectively
5. given an integer n (that we can: add 1 to, subtract 1 from, or divide by 2) what's the smallest number of operations needed to reach 1
6. what's the probability of eric remembering anything to do with markov chains 

Deglazed solutions:
1. start with a few primes (2 to 31 in this case) and greedy primality testing (max length of string was only 10,000)
2. sort em, find a midpoint between positive and negative entries, if theres an odd number of negative entries make the last occuring negative number '1' and return the product of the list
3. look at a chessboard for a bit, write a terrible solution then remember good ol' [dijkstra](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
4. for each y count how many divisors it has preceeding it in the list and how many multiples following it, then for each y add to the total the product of y's divisor and multiples count (that's math p|ab right there bb)
5. my fav! (love anything related to [collatz](https://en.wikipedia.org/wiki/Collatz_conjecture)) write down any 9 sequential integers and then their equivalence modulo 4 :) 
6. This one is _really fun_ if you're a cowboy:
* ignore the matrix structure of the input and try to create your own insane spaghetti solution (4 hours) 
* assume the Fraction lib pasta in python will not be as tasty as homemade (another 4 hours) 
* assume your very ugly bolognese code has rounding errors somewhere and scrap it all (repeat above 1.5 times or until pasta smells of burnt hair)
* realize you're stirring your pasta with an old toothbrush (leased common mistake), swap it out for a spoon (least common multiple) and enjoy the rich lasagna
