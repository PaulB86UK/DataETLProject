import pandas as pd
import os


def create_main_file(PATH):
    COUNTER = 0
    for filename in os.listdir(PATH):
        if filename.startswith("epl_data_") & (filename.endswith(".csv")):
            print(f"Currently Processing {filename}")
            if COUNTER != 0:
                temp_data = pd.read_csv(Rf"{PATH}\{filename}")
                temp_data["Season"] = f"Season 20{filename[9:11]}/20{filename[11:13]}"
                epl_data = pd.concat([epl_data, temp_data])

            else:
                epl_data = pd.read_csv(Rf"{PATH}\{filename}")
                epl_data["Season"] = f"Season 20{filename[9:11]}/20{filename[11:13]}"

        else:
            pass

        COUNTER += 1

    return epl_data


def rename(epl_data):

    epl_data.columns = [
        "Date",
        "Referee",
        "HomeTeam",
        "AwayTeam",
        "FullTime",
        "Halftime",
        "HomeGoals",
        "HomeGoalsHalftime",
        "HomeShots",
        "HomeShotsOnTarget",
        "HomeCorners",
        "HomeFouls",
        "HomeYellowCards",
        "HomeRedCards",
        "AwayGoals",
        "AwayGoalsHalftime",
        "AwayShots",
        "AwayShotsOnTarget",
        "AwayCorners",
        "AwayFouls",
        "AwayYellowCards",
        "AwayRedCards",
        "Season",
    ]

    return epl_data


def query():
    sql_query = """
    SELECT  CASE    WHEN LENGTH(Date) = 8 THEN  20||SUBSTR(Date,7,2)||"-"||SUBSTR(Date,4,2)||"-"||SUBSTR(Date,'/',3)
                    WHEN LENGTH(Date) = 10 THEN  SUBSTR(Date,7,2)||"-"||SUBSTR(Date,4,2)||"-"||SUBSTR(Date,'/',3)
            END AS 'Date'
            ,   Season
            ,   Referee
            ,   HomeTeam
            ,   AwayTeam
            ,   FullTime
            ,   Halftime
            ,   HomeGoals
            ,   HomeGoalsHalftime
            ,   HomeShots
            ,   HomeShotsOnTarget
            ,   HomeCorners
            ,   HomeFouls
            ,   HomeYellowCards
            ,   HomeRedCards
            ,   AwayGoals
            ,   AwayGoalsHalftime
            ,   AwayShots
            ,   AwayShotsOnTarget
            ,   AwayCorners
            ,   AwayFouls
            ,   AwayYellowCards
            ,   AwayRedCards
        FROM epl_data_renamed
    """
    return sql_query
