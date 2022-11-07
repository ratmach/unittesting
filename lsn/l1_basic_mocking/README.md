In case Space cruiser brakes down, rick needs a way to debug it he wrote a `debug_space_cruiser` function which needs
some unit tests

while we're at it might as well test how the universe hashing algorithm `get_universe_hash` behaves 🤷‍♂️


---
NOTES: while doing test exercise it is advised not to touch anything outside the `test_*` files

there are two script files to test, one of them is procedural other one is OOP

useful resources:

- [mock.patch](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch)
- [mock.patch.object](https://docs.python.org/3/library/unittest.mock.html#patch-object)

Unit testing is important, it helps us keep code quality high and features working.
In most cases unit testing is used for isolating parts of the code in order to give developers 
a more manageable scope to focus on. Which gives teams ability to scale in size, there are many tricks approaches and nuances to unit testing,

we'll start with two of the most basic ones:

A) testing a function for an input
this is the most basic form of the testing, you're taking a function, giving it an input and waiting for it to return a specific number,
this approach may work in certain scenarios but is usually heavily dependent on the actual size of the input set

B) mocking a function

mocking a function is a term which involves us replacing an actual function call with a fake one,
fake function resembles an actual one, with obvious differences in return value and actual execution

(both of this can be changed by setting a return_value and side_effects)

another difference is in the lifecycle, mocked function "lives" from the .start() up till .stop()

(note: mock.patch is context manager friendly (so it can be used with `with patch() as f`))

or until the test does a cleanup (more on this in the test lifecycles)

