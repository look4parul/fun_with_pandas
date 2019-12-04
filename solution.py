import pandas as pd

df = pd.read_csv("election_data.csv")
print(df)

total_num_votes = df["Voter ID"].shape[0]
print(total_num_votes)

count_df = df.groupby("Candidate").count()[["Voter ID"]].assign(proportion =lambda df: df["Voter ID"]/total_num_votes) 
print(count_df)