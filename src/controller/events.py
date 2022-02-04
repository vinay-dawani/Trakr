import re
import json

try:
    from utils.bolt_init_helper import app
    from service.events.messages import analyze_wordle_score
    from store.scores import log_scores
except ImportError:
    from ..utils.bolt_init_helper import app
    from ..service.events.messages import analyze_wordle_score
    from ..store.scores import log_scores


@app.message(re.compile("(Wordle) \d+ [123456]\/6\*?"))
def get_wordle_score_msg(message, say) -> None:
    score = analyze_wordle_score(message)
    user_info = message["user"]
    log_scores(user_info, score)
    say("your score has been logged")
