import json

from pathlib import Path


score_file = Path(r"data/scores.json")


def log_scores(user: str, score: dict):
    """Logs the score to JSON datastore

    Args:
        user (str): user who sent the message
        score (dict): formatted dictionary of score info
    """
    if not score_file.is_file():
        create_scores_store()  # Creates the store if doesn't exist
    else:
        with open(score_file, "r", encoding="utf-8") as jsonfile:
            data = json.load(jsonfile)

            # checks if user exists and populates the database
            if user not in data["data"]:
                create_user_in_store(user)
                input_user_scores(user, score)
            else:
                input_user_scores(user, score)


def create_scores_store() -> None:
    """makes a json file with an empty object"""
    with open(score_file, "w", encoding="utf-8") as jsonfile:
        data = {"data": {}}
        json.dump(data, jsonfile)
        jsonfile.close()
    create_user_in_store("test")  # creates a test user


def create_user_in_store(user: str) -> None:
    """Creates a user in the datastore using

    Args:
        user (str): Name of the user to initialize entry into
    """
    user_data = {
        user: {"total_score": 0, "total_games": 0, "average": 0, "all_games": []}
    }
    with open(score_file, "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)

    data["data"].update(user_data)

    with open(score_file, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)


def input_user_scores(user: str, score: dict) -> None:
    """Insert the scores of user in database

    Args:
        user (str): id of the user to insert
        score (dict): Score of the user
    """
    with open(score_file, "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)

    data["data"][user]["all_games"].append(score)
    data = calculate_totals(data, user)

    with open(score_file, "w", encoding="utf-8") as jsonfile:
        json.dump(data, jsonfile)


def calculate_totals(data: dict, user: str) -> dict:
    """Caclulates total values like total games

    Args:
        data (dict): Data of the JSON file with
        user (str): id of the user who

    Returns:
        dict: returns updated data
    """
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
    """Returns all games of the user

    Args:
        user (str): Id of the user to quesry

    Returns:
        list[dict]: a list of all the games of the user
    """
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


def check_user_exists(user: str) -> bool:
    """Checks if user exists in datastore and

    Args:
        user (str): ID if the user is already

    Returns:
        bool: if user exists or not
    """
    with open(score_file, "r", encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)

        if user in data["data"]:
            return True
        else:
            return False
