from passlib.context import CryptContext


pwd_cxt = CryptContext(schemes='bcrypt', deprecated='auto')

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
    
    def verify(plaintext_password: str, hashed_password: str):
        return pwd_cxt.verify(plaintext_password, hashed_password)