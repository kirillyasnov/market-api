from pydantic import BaseSettings

class Settings(BaseSettings):
    
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int
    
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'