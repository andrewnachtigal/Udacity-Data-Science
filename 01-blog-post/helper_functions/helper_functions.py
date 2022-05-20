# print survey questions from schema

def print_question_text(col_name: str) -> None:
    '''Print question text for specified column name from schema dataframe

    Args:
    col_name: str. Name of column in schema dataframe

    Returns:
    None
    '''
    try:
        question_text = schema.loc[schema.Column==col_name,'QuestionText'].values[0]
        print(f'{col_name}: {question_text}\n')
    except:
        print('Column name does not exist.\n')


# replace values in string function
# https://stackoverflow.com/questions/14156473/can-you-write-a-str-replace-using-dictionary-values-in-python

def replace_values_in_string(text, args_dict):
        '''Does something

        Args:

        Returns:
        
        '''
    for key in args_dict.keys():
        text = text.replace(key, str(args_dict[key]))
    return text
