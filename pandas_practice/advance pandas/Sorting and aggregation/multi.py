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
    grouped = df.groupby('Age')['Salary'].sum()
    print("Grouped DataFrame:", grouped, sep="\n")


if __name__ == '__main__':
    demo()