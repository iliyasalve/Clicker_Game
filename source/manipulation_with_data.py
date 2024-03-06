def save_result(data_path: str, score: int, multipliers: int, multipliers_cost: int, best_score: int):
    '''
    Writing current values to a file
    '''

    dict = {
          "score": score,
          "multipliers": multipliers,
          "multipliers_cost": multipliers_cost,
          "best_score": best_score
    }
    
    with open(data_path, "w") as file:
        for key, value in dict.items():
            file.write(f'{key} {value}\n')


def load_result(data_path: str) -> tuple[int, int, int, int]:
    '''
    Returns the values written in the file
    '''

    dict = {}

    with open(data_path) as file:
        for line in file:
            key, *value = line.split()
            dict[key] = value
    
    return int(dict["score"][0]), int(dict["multipliers"][0]), int(dict["multipliers_cost"][0]), int(dict["best_score"][0])

    