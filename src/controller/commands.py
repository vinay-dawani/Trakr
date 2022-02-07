try:
    from utils.bolt_init_helper import app
    from service.events.messages import analyze_wordle_score
    from store.scores import (
        log_scores,
        check_game_exists_user,
        check_user_exists,
        create_user_in_store,
    )
except ImportError:
    from ..utils.bolt_init_helper import app
    from ..service.events.messages import analyze_wordle_score
    from ..store.scores import (
        log_scores,
        check_game_exists_user,
        check_user_exists,
        create_user_in_store,
    )


@app.command("/scan")
def scan_build_history(ack, body):
    ack(f"hey")
    x = app.client.conversations_history(channel=body["channel_id"])
    print(x)
