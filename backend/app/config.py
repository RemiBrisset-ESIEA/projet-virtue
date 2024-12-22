class Config:
    # Configuration pour l'application Platinium
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@db/platinium'
    SQLALCHEMY_TRACK_MODIFICATIONS = False