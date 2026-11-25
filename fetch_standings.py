import pandas as pd

pd.set_option('display.max_columns', None)

url = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv"
games = pd.read_csv(url)
games = games[games["season"] == 2026]

teams = games['away_team'].unique().tolist()

games = games.dropna(subset=["away_score","home_score"])

team_divisions = {
    "NE":"AFCE",
    "NYJ":"AFCE",
    "MIA":"AFCE",
    "BUF":"AFCE",
    "IND":"AFCS",
    "HOU":"AFCS",
    "JAX":"AFCS",
    "TEN":"AFCS",
    "PIT":"AFCN",
    "BAL":"AFCN",
    "CLE":"AFCN",
    "CIN":"AFCN",
    "KC":"AFCW",
    "LV":"AFCW",
    "DEN":"AFCW",
    "LAC":"AFCW",
    "DAL":"NFCE",
    "WAS":"NFCE",
    "PHI":"NFCE",
    "NYG":"NFCE",
    "NO":"NFCS",
    "ATL":"NFCS",
    "CAR":"NFCS",
    "TB":"NFCS",
    "GB":"NFCN",
    "CHI":"NFCN",
    "DET":"NFCN",
    "MIN":"NFCN",
    "SF":"NFCW",
    "LA":"NFCW",
    "ARI":"NFCW",
    "SEA":"NFCW"}

teams = games['away_team'].unique().tolist()
divisions = set(team_divisions.values())
print(divisions)

standings = pd.DataFrame({"team": teams,"w": 0,"l": 0,"t": 0}).set_index("team")
standings["div"] = standings.index.map(team_divisions)

standings = standings

games = games[["away_team","home_team","away_score","home_score"]]


#add W/L columns
for _,row in games.iterrows():
    away,home = row["away_team"],row["home_team"]
    if row['away_score'] > row['home_score']:
        standings.loc[away,"w"] += 1
        standings.loc[home,"l"] += 1
    elif row['home_score'] > row['away_score']:
        standings.loc[away,"l"] += 1
        standings.loc[home,"w"] += 1
    elif row['home_score'] == row['away_score']:
        standings.loc[away,"t"] += 1
        standings.loc[home,"t"] += 1
    else:
        raise TypeError('Could not evaluate the scores of the game.')

standings = standings.sort_values(["w","t"],ascending=False)
print(standings)

for division in divisions:
    pass