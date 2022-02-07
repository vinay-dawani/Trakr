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
