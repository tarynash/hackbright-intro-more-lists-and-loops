#Loops Exercises Part 1: Exploring Range
*Do the following exercises in the Python interpreter.*

## Explore `range`
*You do not need to type up answers to these.*

1. Type `range(5)` and press enter. What happens? 
2. Type `range(3.14)` and press enter. What happens? 
3. Type `range(-8)` and press enter. What happens? 
4. Type `range(0)` and press enter. What happens?
5. Type `range(1)` and press enter. What happens? 
6. Type `range(1,5)` and press enter. What happens?
  1. How is this different than `range(5)`?
7. Type ``range(5,1)`` and press enter. What happens?
8. Now type `range(5,1,-1)` and press enter. What happens?
  1. How is this different than `range(5,1)`?
9. Type `range(0,-5)` and press enter. What happens?
10. Type `range(-5,0)` and press enter. What happens?
  1. How is this different than `range(0,-5)`?
  2. How would you get the numbers from 0 down to -4? (Hint: look at #8)
11. Type `range(10)` and press enter. What happens?
12. Type `range(0,10)` and press enter. What happens?
13. Type `range(0,10,1)` and press enter. What happens?
14. Type `range(0,10,2)` and press enter. What happens?
15. Type `range(0,10,1+1)` and press enter. What happens?

## Describe how `range` works
*Please record your answers to these questions by using the edit button on GitHub.  
Make sure you have pushed your lists exercises before making any commits on GitHub, otherwise you will have to make a merge commit later.*

1. What does `range` do with a single argument?
  * Returns the indeces of the argument. For example, range(5) would return [0,1,2,3,4].
2. What do the arguments mean if there are 2?
  * Returns the indeces of the 2nd argument, beginning at the first (instead of beginning at the 0 index). For example, range(1:5) returns [1,2,3,4].
3. What does the third argument mean?
  * The third argument is the number you wish to count the indeces by. For example, range(2,12,2) returns [2,4,6,8,10].
