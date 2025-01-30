[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tqM-lrvp)
# CMPS 2200  Recitation 01

**Name (Team Member 1):**___Zoe Murphy___  
**Name (Team Member 2):**______

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`. All tests are in `test_main.py`.

## Install Python Dependency

We need Python library of "tabulate" to visualize the results in a good shape. Please install it by running 'pip install tabulate' or 'pip install -r requirements.txt' in Shell Tab of Repl.  

## Running and testing your code

- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest test_main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 

**For linear search, the function goes through a list one by one until it finds a match for the key. Therefore,
the worst case input value for the key would be the value at the very end of the given list. This would require the function
to check each and every value in the list. If it was a really long list, this could take a bit of time.**

**For binary search, it basically splits the given list in half and searches each half (and it will keep splitting in half
over and over until there are no numbers left). So, the worst case scenario for the key would actually be a value
that isn't even in the list. This is because the binary search function would have to split over and over again until
there are no numbers left, which would be the most time consuming.**

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 

**I already explained how the linear search works in the question above. The best case value for the key would be
whatever value is positioned first in the list. If the first value matches the key, the function is done running 
right then and there.**

**For the binary search function (also explained how it works in the question above), the best case key value would be 
 equal to the middle value in the list. In my code, the middle values is defined as "middle = (left + right) // 2," so 
 the best input key would be equal to that equation.**

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest test_main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

**To run "print_results(compare_search()), from the command line, I had to run "python3" so that it could take in 
python commands. Then, I ran "from main import compare_search()" and "from main import print_results()."
Then, I could run the command above and it gave me this:**

|        n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.006 |    0.007 |
|      100 |    0.005 |    0.002 |
|     1000 |    0.044 |    0.002 |
|    10000 |    0.410 |    0.003 |
|   100000 |    4.145 |    0.005 |
|  1000000 |   41.669 |    0.010 |
| 10000000 |  483.751 |    0.016 |


- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

**So just knowing how the run times work, O(n) is slower/less efficient than O(log_2(n)). This makes sense looking
at that table above, as the binary search times (O(log_2(n)) are overall much faster than the linear search times (O(n)). So yes, 
these theoretical running times match the empirical results.**

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search?
      + **As mentioned above, the worst-case scenario run time for linear search is O(n). So, if we're
          searching a list of n elements k times, the run time would just be O(kn). You just need to
          multiply k times and n elements together for the run time.**
  + For binary search?
      + **Also mentioned above, the worst run time for binary search is O(log_2(n)). However,
          now we have to take into account the sorting of the list, which is n^2. So, together the
          sorting time of binary search in this scenario would be O(log_2(n) + n^2). But, we search the
          list k times (we don't sort it k times, just search it), so my final answer is O(k log_2(n) + n^2)**
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting?
    **So to find an answer to this, set up an inequality between the two run times we just found.
    So, we have n^2 + k log_2(n) < kn. k log_2(n) is pretty small compared to n^2, so we can just say n^2 < kn.
    Then, it becomes n < k. So, if n < k, binary search + sorting is more efficient. If n > k, use the linear search**
