import pandas as pd

def main(fileName):
    fileName = str(fileName)
    df = pd.read_csv(fileName)
    print("rows: " + str(len(df.axes[0])))
    print("cols: " + str(len(df.axes[1])))

main("./text.csv")
