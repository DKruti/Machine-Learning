#Preparing the Data and Launching the Fine Tuning

import pandas as pd

n = 2000

#df = pd.read_excel('/Users/aaliyahsalia/Desktop/SFBU/6thTrimester/CS589/Week10_HW2/Medicine_description.xlsx', sheet_name='Sheet1', header=0, nrows=n)
df = pd.read_excel('Medicine_description.xlsx', sheet_name='Sheet1', header=0, nrows=n)
reasons = df["Reason"].unique()

reasons_dict = {reason: i for i, reason in enumerate(reasons)}

df["Drug_Name"] = "Drug: " + df["Drug_Name"] + "\n" + "Malady:"

df["Reason"] = " " + df["Reason"].apply(lambda x: "" + str(reasons_dict[x]))

df.drop(["Description"], axis=1, inplace=True)

df.rename(columns={"Drug_Name": "prompt", "Reason": "completion"}, inplace=True)

jsonl = df.to_json(orient="records", indent=0, lines=True)

with open("drug_malady_data.jsonl", "w") as f:
    f.write(jsonl)
