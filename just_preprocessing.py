import pandas as pd

table: pd.DataFrame = pd.read_csv("tables/stratified_S2_points_wdate_filter.csv")

df_sorted = table.sort_values(
	by = ["id", "abs_days_diff", "cs_cdf"],
	ascending=[True, True, False]
)


df_selected = df_sorted.groupby("id") \
                   	.first() \
                   	.reset_index()


# Create a unique download ID for each row
df_selected["s2_download_id"] = [
    f"S2_{i:05d}" for i in range(len(df_selected))
]

df_selected.to_csv("tables/stratified_S2_points_wdate_filter_reduced.csv")

pass