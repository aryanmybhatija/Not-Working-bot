import os

class Config(object):
    # Telegram Bot Token (from environment variable)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    
    # Telegram API ID & Hash (from environment variables)
    API_ID = int(os.environ.get("API_ID", ))
    API_HASH = os.environ.get("API_HASH", "")
    
    # Admin IDs (comma-separated in env, converted to list of integers)
    ADMIN_ID = [int(admin_id) for admin_id in os.environ.get("ADMIN_ID", "").split(",")]
    
    # MongoDB URL (from environment variable)
    DB_URL = os.environ.get("DB_URL", "")
    
    # Database Name (from environment variable)
    DB_NAME = os.environ.get("DB_NAME", "MY_BOT_DB")
    
    # Log Channel IDs (from environment variables)
    TXT_LOG = int(os.environ.get("TXT_LOG", -1002267020380))
    AUTH_LOG = int(os.environ.get("AUTH_LOG", -1002206934353))
    HIT_LOG = int(os.environ.get("HIT_LOG", -1002250811863))
    DRM_DUMP = int(os.environ.get("DRM_DUMP", -1002460920533))
    
    # Main Channel ID (from environment variable)
    CHANNEL = int(os.environ.get("CHANNEL", -1002644382988))
    
    # Channel URL (from environment variable)
    CH_URL = os.environ.get("CH_URL", "https://t.me/II_Way_to_Success_II")
    
    # Bot Owner Link (from environment variable)
    OWNER = os.environ.get("OWNER", "6947378236")
    
    # Thumbnail URL (from environment variable)
    THUMB_URL = os.environ.get("THUMB_URL", "https://i.postimg.cc/dVmpK7NP/IMG-20250603-180212-401.jpg")
