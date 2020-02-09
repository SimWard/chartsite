import os


class Config:
    # generated with secrets.token_hex(16) (should be env var for production)
    SECRET_KEY = '54a4fb91181f930961e26797a6314e43'

    # definitely use env var if any more complicated than sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
