# Trakr

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/vinay-dawani/trakr?label=version&style=for-the-badge)
[![wakatime](https://wakatime.com/badge/user/d02739e1-9da5-42ca-b1ff-1a3b3863a220/project/e2ef1360-c9b2-4d1d-afda-b0df3a4792ef.svg?style=for-the-badge)](https://wakatime.com/badge/user/d02739e1-9da5-42ca-b1ff-1a3b3863a220/project/e2ef1360-c9b2-4d1d-afda-b0df3a4792ef?style=for-the-badge)
[![Slack](https://img.shields.io/static/v1?label=made%20for&message=Slack&color=4A154B&style=for-the-badge&logo=slack)](https://img.shields.io/static/v1?label=made%20for&message=Slack&color=4A154B&style=for-the-badge&logo=slack)

Trakr is a minimal slack bot that is dedicated to tracking wordle scores in Data Solutions slack workspace.

## Packages

* slack_bolt
* pytest

## Installation

Spin up a virtual environment with venv/pyenv/whatever and install the readme:

```zsh
pip install -r requirements.txt
```

Start the slack bot with:

```zsh
python src/app.py
```

## Roadmap

* command ro return particular score for user
* command to give weekly average of all users
* command to throw some cool graphs?
* code refactoring (a lot of it)
* probably switch to a database?

## Contributing

Contributions are welcome!

## License

[GNU AGPL v3](./LICENSE)