import os

class Config:

    BOT_TOKEN = os.environ.get(
        "BOT_TOKEN", " "
    )

    SESSION_NAME = os.environ.get("SESSION_NAME", "")

    API_ID = int(os.environ.get("API_ID", ""))

    API_HASH = os.environ.get("API_HASH", "")

    CLIENT_ID = os.environ.get(
        "CLIENT_ID",
        "",
    )

    CLIENT_SECRET = os.environ.get(
        "CLIENT_SECRET", ""
    )

    # Owner is allowed to use /addauth, /rmauth, /users, /broadcast, /broadusers
    OWNER_ID = int(os.environ.get("OWNER_ID", "8909902924"))

    _AUTH_USERS_DEFAULT = (
        "8845596819,7988815969,8680968748,8429278856,8723278238,8313091010,8902042822,8480660521,8971045439,"
        "8838086114"
    )
    AUTH_USERS = [
        int(uid)
        for uid in os.environ.get("AUTH_USERS", _AUTH_USERS_DEFAULT).split(",")
        if uid.strip()
    ]
    if OWNER_ID not in AUTH_USERS:
        AUTH_USERS.append(OWNER_ID)

    VIDEO_DESCRIPTION = os.environ.get(
        "VIDEO_DESCRIPTION",
        "Uploaded By Smarty Brother. Only For Education Purpose!",
    )

    VIDEO_CATEGORY = os.environ.get("VIDEO_CATEGORY", "")

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "—MS Bro")

    DEBUG = bool(os.environ.get("DEBUG", ""))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE", "unlisted")

    CRED_FILE = os.environ.get("CRED_FILE", "auth_token.txt")
