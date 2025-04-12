import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    dimension = players.shape
    return list(dimension)
