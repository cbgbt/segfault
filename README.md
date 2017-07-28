segfault
========
Sometimes you need errors and even BaseException just isn't enough! For those
times when you need something truly awful, try segfault!

Errortown
=========

```python
import segfault

# Segfaults as a function call,
segfault.segfault()

# Segfaults as an exception!
raise segfault.Segfault("They came from... behind")

# It's that easy!
```
