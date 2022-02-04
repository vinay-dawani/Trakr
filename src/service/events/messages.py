def analyze_wordle_score(msg_payload: dict) -> dict:
    score_str = msg_payload["text"]
    score_arr = score_str.split("\n")
    game_info = score_arr[0]
    game_res = score_arr[2:]

    game_info = format_game_info(game_info, game_res)
    return game_info


def format_game_info(game_info: str, game_res_str: str) -> dict:
    info = game_info.split(" ")
    game_num = info[1]
    game_res = info[2][0]
    hard_mode = True if "*" in info[2] else False
    completed = was_game_completed(game_res_str)
    shared = "\n".join(game_res_str)

    return {
        "game_num": int(game_num),
        "tries": int(game_res),
        "hard_mode": bool(hard_mode),
        "completed": bool(completed),
        "shared": str(shared),
    }


def was_game_completed(game_res: str) -> bool:
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
