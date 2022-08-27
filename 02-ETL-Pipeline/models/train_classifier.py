import nltk
nltk.download(['punkt', 'wordnet', 'averaged_perceptron_tagger'])

import sys
import re
import numpy as np
import pandas as pd
import pickle

from sqlalchemy import create_engine
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics import classification_report
from sklearn.multioutput import MultiOutputClassifier

url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'


class StartingVerbExtractor(BaseEstimator, TransformerMixin):

    def starting_verb(self, text):
        sentence_list = nltk.sent_tokenize(text)
        for sentence in sentence_list:
            pos_tags = nltk.pos_tag(tokenize(sentence))
            first_word, first_tag = pos_tags[0]
            if first_tag in ['VB', 'VBP'] or first_word == 'RT':
                return True
        return False

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        X_tagged = pd.Series(X).apply(self.starting_verb)
        return pd.DataFrame(X_tagged)


def load_data(database_filepath):
    '''Reads messages from database

    Args:
        database_filepath (str): Filepath to SQLite database.
    Returns:
        dataframe containing (X) features and (y) labels
    '''

    #database_filepath = "../data/DisasterResponse.db"
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql_table('DisasterResponse_table', engine)

    df = df.drop(['child_alone'], axis=1)

    # load data from database
    X = df['message']
    y = df.iloc[:,4:]
    category_names = list(y.columns.values)
    return X, y, category_names


def tokenize(text):
    '''Tokenize the text function

    Args:
        text: Text message which needs to be tokenized
    Returns:
        clean_tokens: List of tokens extracted from the provided text
    '''

    url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

    # Extract urls from text & Replace url with a url placeholder string
    detected_urls = re.findall(url_regex, text)
    for url in detected_urls:
        text = text.replace(url, "urlplaceholder")

    tokens = nltk.word_tokenize(text)
    lemmatizer = nltk.WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    '''Build machine learning pipeline

    Args:
        None
    Returns:
        cv: gridsearch object that transforms data, creates model object, and
        finds optimal model parameters.
    '''

    pipeline = Pipeline([
        ('features', FeatureUnion([

            ('text_pipeline', Pipeline([
                ('count_vectorizer', CountVectorizer(tokenizer=tokenize)),
                ('tfidf_transformer', TfidfTransformer())
            ]))

        ])),

        ('classifier', MultiOutputClassifier(AdaBoostClassifier()))
    ])

    parameters = {
        'classifier__estimator__learning_rate': [0.01, 0.02, 0.05],
        'classifier__estimator__n_estimators': [10, 20, 40]
    }

    cv = GridSearchCV(pipeline, param_grid = parameters)
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    '''Model evaluation function that returns test accuracy, precision, recall
        and F1 score for fitted model.

    Args:
        model: Fitted model object.
        X_test: Dataframe containing test features dataset.
        Y_test: Dataframe containing test labels dataset.
        category_names: list of strings. List containing category names.
    Returns:
        None (printed evaluation results)
    '''

    Y_pred_test = model.predict(X_test)
    print(classification_report(Y_test.values, Y_pred_test, target_names=category_names))


def save_model(model, model_filepath):
    '''Fitted model saved as pickle file

    Args:
        model: model object. Fitted model object.
        model_filepath: string. Filepath for where fitted model should be saved
    Returns:
        None
    '''

    with open(model_filepath, 'wb') as f:
        pickle.dump(model, f)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

        print('Building model...')
        model = build_model()

        print('Training model...')
        model.fit(X_train, Y_train)

        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
