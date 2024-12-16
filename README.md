# Unclosed File Bug in Python

This repository demonstrates a common but easily overlooked error in Python: forgetting to close files after opening them.  This can lead to resource leaks and in extreme cases, data corruption.

The `bug.py` file contains the buggy code. The `bugSolution.py` file presents a solution. Always ensure to close files using a `finally` block or context manager for reliable resource management.