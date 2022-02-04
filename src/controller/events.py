import re

try:
    from utils.bolt_init_helper import app
    from service.events.messages import analyze_wordle_score
    from store.scores import log_scores, check_game_exists_user
except ImportError:
    from ..utils.bolt_init_helper import app
    from ..service.events.messages import analyze_wordle_score
    from ..store.scores import log_scores, check_game_exists_user


@app.message(re.compile("(Wordle) \d+ [123456]\/6\*?"))
def get_wordle_score_msg(message) -> None:
    score = analyze_wordle_score(message)
    user_info: str = message["user"]

    game_exists = check_game_exists_user(user_info, score)

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
