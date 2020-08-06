def count(df):
    """
    Prints value counts for every column in a DataFrame
    
    """
    for col in df.columns:
        print('Values of {}'.format(col))
        print(data[col].value_counts(dropna = False)) 
        print('\n')