import time
import pandas as pd
import fireducks.pandas as fd
import matplotlib.pyplot as plt

operations = ["load_data", "countna", "dropna", "query_1", "query_2", "query_3", "query_4"]

def load_data(module, filename):
    return module.read_csv(filename, index_col=0)

def countna(df):
    return df.isnull().sum()

def dropna(df):
    return df.dropna()

# Calculate average points by country
def q1(df):
    return df.groupby('country')['points'].mean().sort_values(ascending=False).head(10)

# Find the most expensive wine
def q2(df):
    return df[df['price'] == df['price'].max()]

# Calculate the number of reviews by variety
def q3(df):
    return df['variety'].value_counts().head(10)

# Find average price for each point value
def q4(df):
    return df.groupby('points')['price'].mean().sort_index()

# to enforce the instructions associated with "df" instance
# to be executed, when using FireDucks to measure execution time
# correctly
def evaluate(df):
    try:
        df._evaluate()
    except: # pandas result doesn't need to be evaluated
        pass

def run_analysis(module, filename):
    times = []

    start = time.time()
    df = module.read_csv(filename)
    evaluate(df)
    times.append(time.time() - start)
    #print(df.shape)

    for q in [countna, dropna, q1, q2, q3, q4]:
        start = time.time()
        res = q(df)
        evaluate(res)
        times.append(time.time() - start)

    return times