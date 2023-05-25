import pandas as pd
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--file", type=str, required=True)
args = parser.parse_args()

data = pd.read_csv(args.file, sep=",")
proc = (
    data
    .assign(File=lambda d: d["File"].str.strip(".json"))
    .groupby(["File"]).agg(
        {
            "VPE Correct": "mean",
            "NO VPE Correct": "mean",
            "Total": "max",
        }
    )
    .reset_index()
    .round(2)
)
print("ITERATIONS: ", data["Iteration"].max() + 1)
print("TOTAL EXAMPLES: ", data["Total"].sum())
print("TOTAL VPE CORRECT: ", data["VPE Correct"].sum())
print("TOTAL NO VPE CORRECT: ", data["NO VPE Correct"].sum())
print("TOTAL VPE ACCURACY: ", data["VPE Correct"].sum() / data["Total"].sum())
print("TOTAL NO VPE ACCURACY: ", data["NO VPE Correct"].sum() / data["Total"].sum())
print("TOTAL ACCURACY: ", (data["VPE Correct"].sum() + data["NO VPE Correct"].sum()) / (data["Total"].sum() * 2))
print(proc)
    
        
            


    
        

