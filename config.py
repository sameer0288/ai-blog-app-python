##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
