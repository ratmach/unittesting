Rick started writting some tests for bootleg JerryBoree he is trying to copy
project is in early stages of development, but he's heard good things about [TDD](https://www.guru99.com/test-driven-development.html)
so he's trying to follow best practices

---
NOTES: while doing test exercise it is advised not to touch anything outside the `test_script`

every test run has a lifecycle, for this segment let's simplify and state the order:
```python
@classmethod
def setUpClass(cls):
    pass

def setUp(self):
    pass

def test(self):
    pass

def tearDown(self):
    pass

@classmethod
def tearDownClass(cls):
    pass
```
in order to follow the DRY principle, it is usually a good idea to move some of the data / mock initialization to setUp / setUpClass, difference being setUpClass only executes once for the test instance, while setUp executes once per test
some testing frameworks take advantage of this giving developers ability to do data initialization once, greatly cutting down on execution time
good example for this would be [setUpTestData](https://docs.djangoproject.com/en/4.1/topics/testing/tools/#django.test.TestCase.setUpTestData)
