# Technology

This project is written in Python
For the programming language, I use "UV" as me Packet-manager.
I use pytest with uv for testing.

## Reasons

- easy deveoment: you habe many komplex and strong libaries (like pandas, numpy, cv2, matplotlib)
- easy deployment: you can run the code everywhere, if you have there a python interpreter

# Usage

you only have to put each lenth of the triangle in the func

```python
from circumference import circumference
a = 10
b = 10
c = 10
u = circumference(a,b,c)
```

# Testing

you need to import pytest:

```python
import pytest
```

your file should be in the folder tests/
your file should start with "test_"
your func name should start with "test_"
