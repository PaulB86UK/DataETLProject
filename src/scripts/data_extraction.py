import pandas as pd
import time


def extract_from_source(PATH):
    """
    Inputs: (PATH)
    Functionality: Extracts the data from https://www.football-data.co.uk and saves it as a csv file in the path specified.
    Returns: None
    """

    COLNAMES = [
        "Date",
        "Referee",
        "HomeTeam",
        "AwayTeam",
        "FTR",
        "HTR",
        "FTHG",
        "HTHG",
        "HS",
        "HST",
        "HC",
        "HF",
        "HY",
        "HR",
        "FTAG",
        "HTAG",
        "AS",
        "AST",
        "AC",
        "AF",
        "AY",
        "AR",
    ]

    for year in range(1617, 2023, 101):
        print(f"Obtaining Data from the English Premmier League, year:{year}")
        epl = pd.read_csv(
            f"https://www.football-data.co.uk/mmz4281/{year}/E0.csv", usecols=COLNAMES
        )
        epl = epl.reindex(columns=COLNAMES)
        epl.to_csv(rf"{PATH}\epl_data_{year}.csv", index=False)
        time.sleep(5)
