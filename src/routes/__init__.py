from flask import Blueprint
from pathlib import Path

router = Blueprint('router', __name__)

baseLocation = Path(__file__).absolute().parent.parent #src

quizzesFileLocation = baseLocation / "data" / "quizzes-file.json"
questionFileLocation = baseLocation / "data" / "question-file.json"
gamesFileLocation = baseLocation / "data" / "games-file.json"
usersFileLocation = baseLocation / "data" / "users-file.json"


from .usersRoutes import *
from .quizzesRoutes import *
from .questionsRoutes import *
from .gamesRoutes import *
