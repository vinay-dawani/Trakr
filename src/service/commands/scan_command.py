import re

try:
    from utils.bolt_helpers import get_channel_history, get_thread
except ImportError:
    from ...utils.bolt_helpers import get_channel_history, get_thread


def get_historical_scores(channel_id: str) -> list[dict]:
    """retrieves, analyzes and logs historical scores

    Args:
        channel_id (str): channel id
    """
    data = get_channel_history(ch_id=channel_id)
    wordle_scores = get_only_wordle_scores(data, channel_id)

    # wordle_scores = sorted(wordle_scores, key=lambda x: x["ts"])
    thread_scores: list[dict] = []
    for score in wordle_scores:
        # print(score, end="\n\n\n")
        if "thread_ts" in score.keys():
            t_data = retrieve_and_collect_threads(channel_id, score)
            thread_scores.extend(t_data)

    wordle_scores.extend(
        thread_scores
    )  # collection of all wordle messages in channel history

    return wordle_scores


def retrieve_and_collect_threads(channel_id: str, msg: dict) -> list[dict]:
    ts = msg["thread_ts"]
    data = get_thread(channel_id, ts)

    wordle_scores = get_only_wordle_scores(data, channel_id)

    return wordle_scores


def get_only_wordle_scores(data: list[dict], channel_id: str) -> list[dict]:
    wordle_scores: list[dict] = []

    for msg in data:
        if "text" in msg.keys():
            match = re.search("(Wordle) \d+ [123456X]\/6\*?", msg["text"])

            if match:
                msg["channel"] = channel_id
                wordle_scores.append(msg)

    return wordle_scores
