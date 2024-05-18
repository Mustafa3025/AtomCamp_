"""" 
def evaluate_models_classification(X_train, X_test, y_train, y_test):
    models = {
        'Logistic Regression': LogisticRegression(max_iter=1000),
        'Decision Tree': DecisionTreeClassifier(),
        'Random Forest': RandomForestClassifier(),
        'Support Vector Machines': SVC(),
        'K-NearestNeighbor': KNeighborsClassifier(),
        'Gradient Boosting': GradientBoostingClassifier(),
        'Multi-Layer Percepton': MLPClassifier(max_iter=1000),
    }   
    
    for model_name, model in models.items():
        try:
            model.fit(X_train, y_train)
            train_score = model.score(X_train, y_train)
            test_score = model.score(X_test, y_test)
            print(f'{model_name} Training Score : {train_score:.4f}')
            print(f'{model_name} Test Score     : {test_score:.4f}')
        except Exception as e:
            print(f'Error evaluating {model_name} : {e}')
        print()
        

print('Evaluating the score of each algorithm : ')
evaluate_models_classification(X_train, X_test, y_train, y_test)
"""