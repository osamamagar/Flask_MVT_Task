class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.sqlite"


class ProductionConfig(Config):
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = "postgresql://magar:3799@localhost:5432/flask_iti"
    # postgresql://username:password@localhost:port_number/dbname


projectConfig={
    "dev": DevelopmentConfig,
    'prd': ProductionConfig
}