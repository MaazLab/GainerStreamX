import pandas as pd


def remove_duplicates_keep_highest(df):
    """
    Removes duplicates based on the 'name' column, keeping the row with the highest 'change' value.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: A DataFrame with duplicates removed.
    """
    if 'name' not in df.columns or 'change' not in df.columns:
        raise ValueError("DataFrame must contain 'name' and 'change' columns.")
    
    # Get the index of the row with max 'change' for each 'name'
    idx = df.groupby('name')['change'].idxmax()
    deduped_df = df.loc[idx].reset_index(drop=True)
    
    return deduped_df


def get_top_k_df(df, top_k):
    """
    Returns the top_k rows of the DataFrame based on the 'change' column (descending order).

    Args:
        df (pd.DataFrame): The input DataFrame.
        top_k (int): The number of top rows to return.

    Returns:
        pd.DataFrame: A DataFrame with the top_k rows.
    """
    if 'change' not in df.columns:
        raise ValueError("DataFrame must contain a 'change' column.")
    
    return df.sort_values(by='change', ascending=False).head(top_k).reset_index(drop=True)



def merge_dataframes_on_key(df1, df2, df3, key):
    """
    Merges three DataFrames on the 'name' column using outer joins.

    Args:
        df1 (pd.DataFrame): First DataFrame.
        df2 (pd.DataFrame): Second DataFrame.
        df3 (pd.DataFrame): Third DataFrame.

    Returns:
        pd.DataFrame: A merged DataFrame containing all columns from the three inputs.
    """
    if key not in df1.columns or key not in df2.columns or key not in df3.columns:
        raise ValueError(f"All DataFrames must have a {key} column.")
    
    merged_df = pd.merge(df1, df2, on=key, how='outer')
    merged_df = pd.merge(merged_df, df3, on=key, how='outer')
    
    return merged_df