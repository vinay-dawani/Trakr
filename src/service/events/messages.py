import re


def analyze_wordle_score(msg_payload: dict) -> dict:
    """Gets info from raw slack response

    Args:
        msg_payload (dict): event notification from slack response

    Returns:
        dict: a dictionary of formatted data about user and the game
    """
    score_str = msg_payload["text"]
    # score_arr = score_str.split("\n")
    game_info = re.search("(Wordle) \d+ [123456X]\/6\*?", score_str).group()
    game_res = re.search("((:\w+:(\\n)?)+)", score_str).group()

    print(game_res, game_info)

    game_info = format_game_info(game_info, game_res)
    return game_info


def format_game_info(game_info: str, game_res_str: str) -> dict:
    """Formats the info for ame in a dictionary

    Args:
        game_info (str): first line of the result as array of
        game_res_str (str): emoji part of the result

    Returns:
        dict: Formatted dictionary
    """
    info = game_info.split(" ")
    game_num = info[1]
    game_res = info[2][0]
    if game_res == "X":
        game_res = 0
    hard_mode = True if "*" in info[2] else False
    completed = was_game_completed(game_res_str)
    shared = game_res_str

    return {
        "game_num": int(game_num),
        "tries": int(game_res),
        "hard_mode": bool(hard_mode),
        "completed": bool(completed),
        "shared": str(shared),
    }


def was_game_completed(game_res: str) -> bool:
    """Checks if the game was completed and returns bool

    Args:
        game_res (str): emoji part of the result string

    Returns:
        bool: if the game was completed
    """
    game_res = game_res.split("\n")

    if len(game_res) <= 6:
        if (
            game_res[-1]
            == ":large_green_square::large_green_square::large_green_square::large_green_square::large_green_square:"
        ):
            return True
        else:
            return False
    else:
        return False
