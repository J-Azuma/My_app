from sqlalchemy import Column, ForeignKey, String
from app.configration.database.initdb import Base
from app.password.password import Password
from app.user.valueobject.userid import UserId

class PasswordDto(Base):
    __tablename__ = "passwords"
    user_id = Column(String, ForeignKey('users.id' , ondelete='CASCADE'), primary_key=True, unique=True)
    value = Column(String, nullable=False)
    
    
    def to_entity(self) -> Password:
        return Password(
            UserId(self.user_id),
            self.value
        )
    
    @staticmethod
    def from_entity(password: Password) -> 'PasswordDto':
        return PasswordDto(
            user_id = password.user_id.value,
            value = password.value
        )