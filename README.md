# Trakr

![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/vinay-dawani/trakr?label=version&)
[![wakatime](https://wakatime.com/badge/user/d02739e1-9da5-42ca-b1ff-1a3b3863a220/project/e2ef1360-c9b2-4d1d-afda-b0df3a4792ef.svg)](https://wakatime.com/badge/user/d02739e1-9da5-42ca-b1ff-1a3b3863a220/project/e2ef1360-c9b2-4d1d-afda-b0df3a4792ef?)
![Python](https://img.shields.io/badge/Made%20With-Python%203.9.5-blue.svg?logo=Python&color=0d7ebf)
![formatter](https://img.shields.io/badge/Code%20Style-Black-black)
![GitHub](https://img.shields.io/github/license/vinay-dawani/trakr?color=6e2d75)
[![Slack](https://img.shields.io/static/v1?label=made%20for&message=Slack&color=4A154B&&logo=slack)](https://img.shields.io/static/v1?label=made%20for&message=Slack&color=4A154B&logo=slack)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?color=107f67)](http://makeapullrequest.com)

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
* logger

## Contributing

Contributions are welcome!

## License

[GNU AGPL v3](./LICENSE)