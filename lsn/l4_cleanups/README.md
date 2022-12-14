Bird person asked rick to create a bird seed compensation calculation, rick is too lazy to fully implement it for all the universes in the central finite curve, but knows it might be useful down the road
so he just implemented a `get_universe` function that does not really do that much (for now)

he did implement some tests, however something seems to be breaking and he has a process of fixing things, it seems that tests work when individually run, but not when doing so together

he knows it is just a super easy fix but can't put a finger on where things go wrong

---
NOTES: please only edit the `UniverseDaysCountHasFallback` test under tests/test_a.py


---

if stuck there is a solution down here ↓

<details>
  <summary>Solution</summary>

  ```
  the way unittest lifecycle works mock.patch().start() can bleed over
  to other tests / files that are executed after until something stops
  the patch
  
  in this case the mocked_calendar_days is the offender
  patch.stopall() at the doCleanup is usually the most straightforward
  way of fixing this
  
  however depending on what initially patches the function / object
  it can also be done in tearDown, tearDownClass, or the function itself
  
  also note that context manager managed patching cleans itself up
  and patch().stop() is also always an option 
  (but also make sure to keep the original patch call for this (not the one that is returned after .start()))
  ```
</details>