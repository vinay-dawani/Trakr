import pytest

from src.service.events.messages import (
    analyze_wordle_score,
    format_game_info,
    was_game_completed,
)

payload = {
    "client_msg_id": "df6a7c76-a001-490e-93d0-9180784b6477",
    "type": "message",
    "text": "Wordle 229 4/6*\n\n:black_large_square::large_yellow_square::large_green_square::black_large_square::black_large_square:\n:large_yellow_square::black_large_square::large_green_square::large_yellow_square::large_yellow_square:\n:large_green_square::black_large_square::large_green_square::large_green_square::large_green_square:\n:large_green_square::large_green_square::large_green_square::large_green_square::large_green_square:",
    "user": "U0313CRTPEK",
    "ts": "1643912870.945159",
    "team": "T031J1E2ZTL",
    "channel": "C031BBVHP6J",
    "event_ts": "1643912870.945159",
    "channel_type": "channel",
}


def test_analyze_wordle_score():
    res = analyze_wordle_score(payload)
    assert res == {
        "game_num": 229,
        "tries": 4,
        "hard_mode": True,
        "completed": True,
        "shared": ":black_large_square::large_yellow_square::large_green_square::black_large_square::black_large_square:\n:large_yellow_square::black_large_square::large_green_square::large_yellow_square::large_yellow_square:\n:large_green_square::black_large_square::large_green_square::large_green_square::large_green_square:\n:large_green_square::large_green_square::large_green_square::large_green_square::large_green_square:",
    }


@pytest.mark.xfail(raises=KeyError)
def test_analyze_wordle_score_empty_payload():
    res = analyze_wordle_score({})
    assert res == {}


def test_was_game_completed_won():
    test_str = ":black_large_square::large_yellow_square::large_green_square::black_large_square::black_large_square:\n:large_yellow_square::black_large_square::large_green_square::large_yellow_square::large_yellow_square:\n:large_green_square::black_large_square::large_green_square::large_green_square::large_green_square:\n:large_green_square::large_green_square::large_green_square::large_green_square::large_green_square:"
    res = was_game_completed(test_str.split("\n"))
    assert res is True


def test_was_game_completed_won_lost():
    test_str = ":black_large_square::large_yellow_square::large_green_square::black_large_square::black_large_square:\n:large_yellow_square::black_large_square::large_green_square::large_yellow_square::large_yellow_square:\n:large_green_square::black_large_square::large_green_square::large_green_square::large_green_square:\n:large_green_square::large_green_square::large_green_square::large_green_square::large_black_square:"
    res = was_game_completed(test_str.split("\n"))
    assert res is False
