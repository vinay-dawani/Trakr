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
    data = app.client.conversations_history(channel=ch_id, oldest=1640995200)
    return data["messages"]


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
    score_str = "#\t\tname\t\t\t\t\taverage guess\t\ttotal games\n----------------------------------------------------------------\n"
    data = dict(sorted(data.items(), key=lambda x: x[1]["avg_guess"]))

    # * The leaderboard message right now mentions the user but since 'respond' API is used,
    # * the message is sent as ephermal and notif are not pushed.
    # TIP: A valid workaround can be to get used profile from id and use 'display_name' property
    # * Also table comes out a bit weird right now because of spacing isuues but when above is
    # * implemented, then an ascii table can be made or an image that is then attached.
    for i, (k, v) in enumerate(data.items(), 1):
        xyz = (
            f"{i}\t\t<@{k}>\t\t\t\t{v['avg_guess']:.3f}\t\t\t\t\t\t{v['total_games']}\n"
        )
        score_str += xyz

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
