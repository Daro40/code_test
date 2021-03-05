# Skills Challenge/Code Test:

* I chose Python to solve the challenge number 4.
* For this challenge i think that it's appropiate to make a Unit Testing.
* I used [virtual_enviroment](https://docs.python.org/3/library/venv.html)

## I did this challenge with a Test-Driven-Development(TDD) methodology:

1. First I code the testing function, taking an array as an example and doing the task manually very carefull to get the expected result.
1. Then run the test to compare both arrays and got it passed, so i proceed to make a function which failed at first, but then:
1. Coded the zeros_to_end function which does the task
1. When i got a positive result i proceed to parametrize the input and expected arrays of the test in order to have different datasets verified
1. Run the test again and passed all of them
1. If the zeros_to_end function is modified it will be easy to test with many datasets if it's working right


**Obs 1** I used Pycharm as a test runner 
> pytest main_test.py
got ===== 3 passed in 0.12s =====

**Obs 2** venv can be used to load all the libraries ( numpy and pytest)

-----
## Datasets:
input | expected
------------ | -------------
arr0 = [0,1,0,0] | expected0 = [1,0,0,0]
arr = [0, 3, 4, 6, 21, 0, 3, 0, 0, 2, 4, 1, 5, 7, 8, 0, 3234, 2534, 0, 524, 65, 42, 1, 6, 0, 788, 65, 7, 7] | expected = [3, 4, 6, 21, 3, 2, 4, 1, 5, 7, 8, 3234, 2534, 524, 65, 42, 1, 6, 788, 65, 7, 7, 0, 0, 0, 0, 0, 0, 0]
arr2 = [0, 3, 4, 6, 21, 0, 3, 2, 4, 1, 5, 7, 8, 0, 0, 524, 65, 42, 1, 6, 0, 788, 65, 7, 7] | expected2 = [3, 4, 6, 21, 3, 2, 4, 1, 5, 7, 8, 524, 65, 42, 1, 6, 788, 65, 7, 7, 0, 0, 0, 0, 0]
