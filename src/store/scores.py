import json
import os
from pathlib import Path


score_file = Path(r"data/scores.json")


def log_scores(user: str, score: dict) -> bool:
    if score_file.is_file() == False:
        create_scores_store()
    else:
        with open(score_file, "r") as jsonfile:
            data = json.load(jsonfile)

            if user not in data["data"]:
                create_user_in_store(user)
                input_user_scores(user, score)
            else:
                input_user_scores(user, score)


def create_scores_store() -> None:
    with open(score_file, "w") as jsonfile:
        data = {"data": {}}
        json.dump(data, jsonfile)
        jsonfile.close()
    create_user_in_store("test")


def create_user_in_store(user: str) -> None:
    user_data = {
        user: {"total_score": 0, "total_games": 0, "average": 0, "all_games": []}
    }
    with open(score_file, "r") as jsonfile:
        data = json.load(jsonfile)

    data["data"].update(user_data)

    with open(score_file, "w") as jsonfile:
        json.dump(data, jsonfile)


def input_user_scores(user: str, score: dict) -> None:
    with open(score_file, "r") as jsonfile:
        data = json.load(jsonfile)

    data["data"][user]["all_games"].append(score)
    data = calculate_totals(data, user)

    with open(score_file, "w") as jsonfile:
        json.dump(data, jsonfile)


def calculate_totals(data: dict, user: str) -> dict:
    all_games = data["data"][user]["all_games"]
    total_games: int = len(all_games)
    total_score: int = 0

    for item in all_games:
        total_score += item["tries"]

    average: float = total_score / total_games

    data["data"][user]["average"] = average
    data["data"][user]["all_games"] = all_games
    data["data"][user]["total_score"] = total_score
    data["data"][user]["total_games"] = total_games

    return data