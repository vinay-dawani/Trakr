from cgitb import text


try:
    from utils.bolt_init_helper import app
    from service.commands.scan_command import get_historical_scores
    from service.events.messages import analyze_wordle_score
    from store.scores import (
        log_scores,
        check_game_exists_user,
        check_user_exists,
        create_user_in_store,
    )
except ImportError:
    from ..utils.bolt_init_helper import app
    from ..service.commands.scan_command import get_historical_scores
    from ..service.events.messages import analyze_wordle_score
    from ..store.scores import (
        log_scores,
        check_game_exists_user,
        check_user_exists,
        create_user_in_store,
    )


@app.command("/scan")
def scan_build_history(ack, body) -> None:
    """Get history of slack channel and put in datastore

    Args:
        ack ([type]): [description]
        body ([type]): message payload
    """
    ack(f"starting the scan :wink:")

    channel_id = body["channel_id"]
    wordle_scores = get_historical_scores(channel_id)

    logged: int = 0

    for msg in wordle_scores:
        score_fmtted = analyze_wordle_score(msg)
        user_id: str = msg["user"]

        game_exists = False

        if check_user_exists(user_id):
            game_exists = check_game_exists_user(user_id, score_fmtted)
        else:
            create_user_in_store(user_id)

        if not game_exists:
            try:
                log_scores(user_id, score_fmtted)
                logged += 1
            except Exception:
                pass

    app.client.chat_postEphemeral(
        channel=channel_id,
        text=f"Scores logged!! Succesfully logged {logged} scores out of {len(wordle_scores)}",
        user=body["user_id"],
    )
