# DEFAULT DEV SETTINGS NOT FOR PROD

class Settings:
    # TODO MONGO SETTINGS
    # DB_NAME = 'temp_aio'
    # DB_USER = 'postgres'
    # DB_PASSWORD = Required(str)
    # DB_HOST = 'localhost'
    # DB_PORT = '5432'

    #FOR DEV ONLY. Generate prod with base64.urlsafe_b64encode(os.urandom(32))
    COOKIE_SECRET = b'0W_Cfh60HUnWjfIZE43a2SA_K4rR0LSMRiUoq4rGVWE='

    # TODO OVERRIDE THESE FROM ENVIRONMENT
