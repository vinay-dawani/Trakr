try:
    from store.scores import get_all_scores
except ImportError:
    from ...store.scores import get_all_scores


def get_top_leaderboard_data() -> dict:
    data = get_all_scores()
    top_scores: dict = {}

    for k, v in zip(data.keys(), data.values()):
        top_scores[k] = {"total_games": v["total_games"], "avg_guess": v["average"]}

    return top_scores
