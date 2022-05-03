from sqlalchemy import Boolean, Column, String
from app.configration.database.initdb import Base
from app.user.user import User
from app.user.valueobject.userid import UserId
from app.user.valueobject.email import  Email

class UserDto(Base):
    """Userエンティティの変換先

    Args:
        Base (_type_): DB接続設定

    Returns:
        _type_: _DTO
    """    
    __tablename__: str = "users"
    __table_args__ = {'extend_existing': True}
    id = Column(String, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    is_active = Column(Boolean, nullable=False, default=False)
    is_deleted = Column(Boolean, nullable=False, default=False)
    
    
    def to_entity(self) -> User:
        """DTOをエンティティに変換

        Returns:
            User: Userエンティティ
        """        
        return User(
            UserId(self.id),
            Email(self.email),
            self.is_active,
            self.is_deleted
        )
    
    @staticmethod
    def from_entity(user: User) -> 'UserDto':
        """DTOをエンティティに変換

        Args:
            user (User): エンティティ

        Returns:
            UserDto: DTOインスタンス
        """        
        return UserDto(
            id = user.id.value,
            email = user.email.value,
            is_active = user.is_active,
            is_deleted = user.is_deleted
        )