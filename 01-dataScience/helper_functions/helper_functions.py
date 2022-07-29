
# print question text function

def print_question_text(col_name: str) -> None:
    '''Print question text for specified column name from schema dataframe

    Args:
    col_name: str. Name of column in schema dataframe

    Returns: None'''

    try:
        question_text = schema.loc[schema.Column==col_name,'QuestionText'].values[0]
        print(f'{col_name}: {question_text}\n')
    except:
        print('Column name does not exist.\n')


# replace values in string function
# https://stackoverflow.com/questions/14156473/can-you-write-a-str-replace-using-dictionary-values-in-python

def replace_values_in_string(text, args_dict):
    '''replace values in string using a dictionary

    Args: text, args_dict
    Returns: new dictonary key-value'''

    for key in args_dict.keys():
        text = text.replace(key, str(args_dict[key]))
    return text


# correlation matrix plot
# https://stackoverflow.com/questions/48139899/correlation-matrix-plot-with-coefficients-on-one-side-scatterplots-on-another

def corrdot(*args, **kwargs):
    '''create correlation matrix with coefficients, etc.

    Args: dataframe numerical values
    Returns: corr plot'''
    corr_r = args[0].corr(args[1], 'pearson')
    corr_text = f"{corr_r:2.2f}".replace("0.", ".")
    ax = plt.gca()
    ax.set_axis_off()
    marker_size = abs(corr_r) * 10000
    ax.scatter([.5], [.5], marker_size, [corr_r], alpha=0.6, cmap="coolwarm",
               vmin=-1, vmax=1, transform=ax.transAxes)
    font_size = abs(corr_r) * 40 + 5
    ax.annotate(corr_text, [.5, .5,],  xycoords="axes fraction",
                ha='center', va='center', fontsize=font_size)
