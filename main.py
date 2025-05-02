from scraping import get_details_stocktitan, get_price_volume_stockanalysis, scrape_stockanalysis, scrape_stocktitan
from utils import get_top_k_df, merge_dataframes_on_key, remove_duplicates_keep_highest
from concurrent.futures import ThreadPoolExecutor
import pandas as pd



with ThreadPoolExecutor() as executor:
    future1 = executor.submit(scrape_stocktitan)
    future2 = executor.submit(scrape_stockanalysis)

    df1 = future1.result()
    df2 = future2.result()

# Combine both results
combined_df = pd.concat([df1, df2], ignore_index=True)

# print("\nCombined Results:")
# print(combined_df)


deduped_df = remove_duplicates_keep_highest(combined_df)
# print("\nAfter Removing Duplicates:")
# print(deduped_df)

# Sort the combined dataframe by 'change' in descending order
combined_sorted_df = deduped_df.sort_values(by='change', ascending=False).reset_index(drop=True)
# print("\nSorted Results:")
# print(combined_sorted_df)


top_k_stocks_df = get_top_k_df(combined_sorted_df ,top_k =5)

print("\ntop_k Stocks")
print(top_k_stocks_df)

# with ThreadPoolExecutor() as executor:
#     future1 = executor.submit(scrape_stocktitan)
#     future2 = executor.submit(scrape_stockanalysis)

#     df1 = future1.result()
#     df2 = future2.result()

price_details_df = get_price_volume_stockanalysis(top_k_stocks_df['name'].to_list())

details_df = get_details_stocktitan(top_k_stocks_df['name'].to_list())

print("price_details_df")
print(price_details_df)


print('details_df')
print(details_df)

merged_df = merge_dataframes_on_key(top_k_stocks_df, price_details_df, details_df, key='name')
merged_df.to_csv('merged_df.csv')