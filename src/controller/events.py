import re

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


@app.message(re.compile("[\w*\s*\d*!\.,@#$%^&\*]*(Wordle) \d+ [123456X]\/6\*?"))
def get_wordle_score_msg(message) -> None:
    """Grab the event where message is a wordle score and analyze item

    Args:
        message ([type]): message payload
    """
    score = analyze_wordle_score(message)
    user_info: str = message["user"]

    if score is None:
        app.client.chat_postEphemeral(
            channel=message["channel"],
            text="Are you trying to send a wordle score? Looks like it's missing some stuff :eyes:",
            user=user_info,
        )
        return

    game_exists: bool = False

    if check_user_exists(user_info):
        game_exists = check_game_exists_user(user_info, score)
    else:
        create_user_in_store(user_info)

    if game_exists:
        app.client.chat_postEphemeral(
            channel=message["channel"],
            text="Uh-ho! Looks like this game already exists in your profile",
            user=user_info,
        )
    else:
        try:
            log_scores(user_info, score)
            app.client.chat_postEphemeral(
                channel=message["channel"],
                text="Your score has been logged!",
                user=user_info,
            )
        except Exception:
            app.client.chat_postEphemeral(
                channel=message["channel"],
                text="Uh-ho! Looks like there were some trouble logging your scores. Please try again later.",
                user=user_info,
            )
