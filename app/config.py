# Placeholder for env

class Config(object):
    DEBUG = False
    TESTING = False

class Production(Config):
    pass

class Development(Config):
    DEBUG = True
    
class Testing(Config):
    TESTING = True
    