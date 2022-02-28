try:
    from utils.bolt_init_helper import app
except ImportError:
    from bolt_init_helper import app


def get_channel_history(ch_id: str) -> list[dict]:
    """Get all past messages of the channel from

    Args:
        ch_id (str): id of the channel to retrieve

    Returns:
        list[dict]: a list of message dictionaries
    """
    data = app.client.conversations_history(
        channel=ch_id, oldest=1640995200, inclusive=True
    )
    scores: list[dict] = []
    scores += data["messages"]
    has_more = bool(data["has_more"])
    _cursor = data["response_metadata"]["next_cursor"] if has_more is True else ""

    while has_more:
        data = app.client.conversations_history(
            channel=ch_id, oldest=1640995200, inclusive=True, cursor=_cursor
        )
        scores += data["messages"]
        has_more = bool(data["has_more"])
        _cursor = data["response_metadata"]["next_cursor"] if has_more is True else ""

    return scores


def get_thread(ch_id: str, ts: int):
    """Get the thread from message timestamp

    Args:
        ch_id (str): Channel id
        ts (int): timestamp of the message

    Returns:
        list[dict]: list of msg objects
    """
    data = app.client.conversations_replies(channel=ch_id, ts=ts)
    return data["messages"]


def build_leaderboard_blocks(data: dict) -> dict:
    """formats game data in table

    Args:
        data (dict): expected format: {
            "user_id": {
                "avg_guess": Integer
                "total_games": Integer
            }
        }

    Returns:
        dict: blocks that can be appended in response message
    """
    score_str = "```##\t\tname                     average guess\t\ttotal games\n---------------------------------------------------------------------\n"
    data = dict(sorted(data.items(), key=lambda x: x[1]["avg_guess"]))

    for i, (k, v) in enumerate(data.items(), 1):
        i = "0" + str(i) if len(str(i)) == 1 else ...

        k = get_displayname_from_id(k)
        k = k + (" " * (25 - len(k)))

        _ = f"{i}\t\t{k}\t{v['avg_guess']:.3f}\t\t\t\t {v['total_games']}\n"
        score_str += _

    score_str += "```"

    blocks = {
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Top Scores of all Time:",
                    "emoji": True,
                },
            },
            {"type": "divider"},
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": score_str},
            },
        ]
    }

    return blocks


def get_displayname_from_id(user_id: str) -> str:
    data = app.client.users_profile_get(user=user_id)

    return data["profile"]["display_name"]
