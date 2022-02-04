import json

from pathlib import Path


score_file = Path(r"data/scores.json")


def log_scores(user: str, score: dict) -> bool:
    if not score_file.is_file():
        create_scores_store()
    else:
        with open(score_file, "r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)

            if user not in data["data"]:
                create_user_in_store(user)
                input_user_scores(user, score)
            else:
                input_user_scores(user, score)


def create_scores_store() -> None:
    with open(score_file, "w", encoding="utf-8") as jsonfile:
        data = {"data": {}}
        json.dump(data, jsonfile)
        jsonfile.close()
    create_user_in_store("test")


def create_user_in_store(user: str) -> None:
    user_data = {
        user: {"total_score": 0, "total_games": 0, "average": 0, "all_games": []}
    }
    with open(score_file, "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)

    data["data"].update(user_data)

    with open(score_file, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)


def input_user_scores(user: str, score: dict) -> None:
    with open(score_file, "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)

    data["data"][user]["all_games"].append(score)
    data = calculate_totals(data, user)

    with open(score_file, "w", encoding="utf-8") as jsonfile:
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


# TODO: make DAO/DTO
def get_all_games_user(user: str) -> list[dict]:
    data: dict
    with open(score_file, "r", encoding="utf-8") as jsonfile:
        # ? Store in a sorted linked list or stack
        data = json.load(jsonfile)

    return data["data"][user]["all_games"]


def check_game_exists_user(user: str, score: dict) -> bool:
    all_games = get_all_games_user(user)

    for game in all_games:
        if game["game_num"] == score["game_num"]:
            return True

    return False
