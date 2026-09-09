import os

def mongo_uri() -> str:
    return os.environ.get("MEDIA_RIGHTS_MONGO_URI", "mongodb://localhost:27017/media_rights")
