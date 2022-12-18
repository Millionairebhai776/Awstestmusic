import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5834794506:AAEgMU5gd-G5_VgL6Y5hQeJZLOEAsEfgQy8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzsBu4wyr2YrD5AQQCu_qsDZSF6DCJCL-AIKHtb3S8M7iR6attC4-ZYWZswAHuYZvx5AjXNinfqB5v5rEPaIsFm0Q1BY8KDYsg_y6b_6PWJ8RAtFhwwjE2XLDNsw84ARjgBxizd5hrGQZEMgynnNOCFpQvSzFUS5jcnJpoqGrp6MYxTmu330k6J_7aI0bDwIWQBwpmnlTDiSxl9rYasMX9h89RA4ZTrZZm8bRZCJdDhQQCwhPdSZWSo1XbOv8v-5Zp2yKWdMJK0HqbWCE8Fn_mDRf4J49iEsnTzj9pbjsRa5GeJlqQki_MwgRaPvHksddq2BwWHSns-CrTf0hh72jJsiw7U=") 
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@FwMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "FILMWORLDOFFICIA")
    CHANNEL = os.environ.get("CHANNEL", "FILMWORLDOFFICIA")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", 5295973607)) # required
