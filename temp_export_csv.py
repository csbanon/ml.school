import pandas as pd


def split_csv():
    """
    Splits a CSV file into two halves and saves them as separate files.
    """
    df = pd.read_csv("data/penguins.csv")
    num_rows = df.shape[0]

    df_1 = df.iloc[:num_rows // 2]
    df_2 = df.iloc[num_rows // 2 :]

    df_1.to_csv("data/penguins_1.csv", index=False)
    df_2.to_csv("data/penguins_2.csv", index=False)


if __name__ == "__main__":
    split_csv()