"""Example grouping demo.

This module intentionally avoids importing pandas at module import time.
The stdlib uses a module called 'grp' which pathlib imports on some
platforms; having a top-level module named `grp` that imports pandas
can cause a circular import. To be safe, import pandas only inside
functions and run demos under a __main__ guard.

"""
"""
Grouping example: safe to import from other modules.

This module imports pandas only when executed directly to avoid
shadowing or side-effects during other imports.
"""


def demo():
    import pandas as pd

    data = {
        'Name': ['Ram', 'Mohan', 'Chovan', 'Thovan'],
        'Age': [28, 24, 35, 30],
        'Salary': [50000, 60000, 55000, 65000]
    }

    df = pd.DataFrame(data)
    print("Original DataFrame:", df, sep="\n")

    # Group by Age and sum Salary
    grouped = df.groupby('Age').sum()
    print("Grouped DataFrame:", grouped, sep="\n")


if __name__ == '__main__':
    demo()

"""

Output :- 

Original DataFrame:
     Name  Age  Salary
0     Ram   28   50000
1   Mohan   24   60000
2  Chovan   35   55000
3  Thovan   30   65000

Grouped DataFrame:
Age
24    60000
28    50000
30    65000
35    55000
Name: Salary, dtype: int64

"""