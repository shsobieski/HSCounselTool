def split_scale(df):
    """
    Splits dataframe into test and training sets. Then scales the sets using the StandardScaler()  
    
    """
    (X_train, X_test, 
     y_train, y_test) = train_test_split(df, target, 
                                         test_size= .2, 
                                         random_state = 24)
    scaler = StandardScaler()
    df = pd.DataFrame(scaler.fit_transform(df))
    X_train = pd.DataFrame(scaler.fit_transform(X_train))
    X_test = pd.DataFrame(scaler.fit_transform(X_test))
    return X_train, X_test, y_train, y_test