def create_pie_chart(df,cols,group_col,title,flip=False,normalize=True):
    '''
    Create pie charts for the given dataframe and columns.
    :param df: DataFrame containing the data to plot
    :param cols: List of columns to plot
    :param group_col: Column to group by
    :param title: Title of the plot
    :param flip: If True, flip the dataframe (transpose it -> rows become columns and vice versa)
    :param normalize: If True, normalize the data to percentages (Default), else show absolute values
    '''
    import matplotlib.pyplot as plt
    
    if isinstance(cols, str):
        cols = [cols]
    if flip:
        df_t = df.transpose()
        df_t.columns = df_t.iloc[0]
        graph_count = len(df_t.columns)
        df_t.drop(df_t.index[0:(len(df.columns) - len(cols))], inplace=True)
        df_t.reset_index(inplace=True)
        df_t.rename(columns={'index': group_col}, inplace=True)
        cols = list(df_t.columns[1:])
        df = df_t
    else:
        graph_count = len(cols)
    title = title[0].upper() + title[1:]
    # set up a subplot for the age categories in leeftijd, create piecharts for each
    if graph_count == 1:
        plt.figure(figsize=(6, 4))
        if normalize:
            plt.pie(df[cols[0]], labels=df[group_col], autopct='%1.1f%%', startangle=90)
        else:
            total = df[cols[0]].sum()
            plt.pie(df[cols[0]], labels=df[group_col], autopct=lambda p: '{:.0f}'.format(p * total / 100), startangle=90)
        plt.title(title, fontsize=16)
        return
    if graph_count% 3 == 0:
        fig, axs = plt.subplots(graph_count//3, 3, figsize=(13-2*(graph_count//3), 4), tight_layout=True)
    elif graph_count % 2 == 0:
        fig, axs = plt.subplots(graph_count//2, 2, figsize=(10, 7), tight_layout=True)
    else:
        fig, axs = plt.subplots(graph_count, 1, figsize=(10, 7))
    axs = axs.flatten()
    # create pie charts for each age category
    # total title
    fig.suptitle(title, fontsize=16)
    for i, col in enumerate(cols, start=0):
        # create pie chart for each age category
        # ignore Na values in the pie chart
        df_used = df.copy()
        df_used = df_used[df_used[col].isna() == False]
        if normalize:
            axs[i].pie(df_used[col], labels=df_used[group_col], autopct='%1.1f%%', startangle=90, colors=plt.cm.tab10.colors)
        else:
            total = df_used[col].sum()
            axs[i].pie(df_used[col], labels=df_used[group_col], autopct=lambda p: '{:.0f}'.format(p * total / 100), startangle=90, colors=plt.cm.tab10.colors)
        axs[i].set_title(col,fontsize=12-graph_count//3)
        for label in axs[i].texts:
            label.set_fontsize(9-graph_count//3)

# normalize the columns in summ_df between 0 and 1
def normalize(df, cols, axis):
    '''
    Normalize the columns in the dataframe between 0 and 1.
    :param df: DataFrame containing the data to normalize
    :param cols: List of columns to normalize
    :param axis: Axis to normalize along (0 for columns, 1 for rows)
    :return: Normalized DataFrame
    '''
    import pandas as pd
    df_norm = df.copy()
    if axis == 0:
        for col in cols:
            col_sum = df[col].sum()
            df_norm[col] = df[col] / col_sum
    elif axis == 1:
        new_cols = {}
        for wijk in df.index.unique():
            wijk_df = df[df.index == wijk]
            wijk_df = wijk_df.fillna(0)
            wijk_sum = wijk_df[cols].sum(axis=1).values[0]

            new_cols[wijk] = {}
            for col in cols:
                new_cols[wijk][col] = wijk_df[col].values[0] / wijk_sum
        df_norm.loc[:, cols] = pd.DataFrame(new_cols).transpose().values
    return df_norm

def remove_whitespace(df, rem_nr=False):
    '''
    Remove whitespace from the column names of the dataframe.
    :param df: DataFrame containing the data to remove whitespace from
    :param rem_nr: If True, remove numbers from the column names i.e. VraagOverHuis_1 becomes VraagOverHuis
    :return: DataFrame with whitespace removed from the column names
    '''
    columns = []
    for colname in df.columns:
        indices = []
        for j in range(1, len(colname)):
            if (colname[j].isupper() and colname[j-1] != ' ' and colname[j-1].isupper() == False) or (colname[j].isnumeric() and colname[j-1].isalpha()):
                indices.append(j)
        indices.append(None)
        columns.append((' ').join([colname[:indices[0]]]+[colname[indices[i]:indices[i+1]] for i in range(len(indices)-1)]))

    if rem_nr:
        columns = [col.split('_')[0] for col in columns]
    df.columns = columns