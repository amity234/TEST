from SARKARMUSIC.core.bot import Sar
from SARKARMUSIC.core.dir import dirr
from SARKARMUSIC.core.git import git
from SARKARMUSIC.core.userbot import Userbot
from SARKARMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Sar()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
