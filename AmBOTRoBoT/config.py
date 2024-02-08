class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 12227067 
    API_HASH = "b463bedd791aa733ae2297e6520302fe"

    CASH_API_KEY = "PNNU99H3W9KDLKVM"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://gqamawel:d3iqDuHfZQONokPCLclcMJc9Qdvm0Xpj@heffalump.db.elephantsql.com/gqamawel"  # A sql database url from elephantsql.com

    EVENT_LOGS = ("-1002024151357")  # Event logs channel to note down important bot level events
    GBAN_LOGS = ()
    MONGO_DB_URI = "mongodb+srv://AMBOT:AMBOT@ambot.uecutzy.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://graph.org/file/297a88997afb4a4a5013a.jpg"

    SUPPORT_CHAT = "dard_e_dil_ded"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6359320563:AAHpB5PCtX1XkJ7om2KEVeV_oL0xusRNEC8"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "9HK7J0H25AKQ"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5360305806  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
