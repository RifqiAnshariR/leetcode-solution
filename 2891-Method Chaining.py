import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # sorted_animals = animals.sort_values(by='weight', ascending=False)  
    # return sorted_animals[sorted_animals["weight"] > 100][["name"]]

    return animals[animals["weight"] > 100].sort_values(by="weight", ascending=False)[["name"]]
