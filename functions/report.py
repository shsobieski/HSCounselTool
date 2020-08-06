def report(model):
    """
    Prints confusion matrix and classification report for the classification model
    
    """
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print('Confusion Matrix\n')
    print(confusion_matrix(y_test, y_pred))
    print('\nClassification Report\n')
    print(classification_report(y_test, y_pred))  
    return y_pred