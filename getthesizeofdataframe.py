import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)

    data = {
        "player_id": [1,2,3],
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 22],
        "position": ["Forward", "Goalkeeper", "Defender"],
        "team": ["A-Team", "B-Team", "C-Team"]
    }

    players = pd.DataFrame(data)

    print(getDataframeSize)
    