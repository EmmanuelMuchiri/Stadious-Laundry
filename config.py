class Config:
    pass
class ProdConfig(Config):
    pass
class TestConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
config_options ={"production":ProdConfig,"development":DevConfig,"testing":TestConfig}