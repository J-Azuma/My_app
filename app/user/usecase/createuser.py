from injector import inject
from typing import Final
from app.password.password import Password
from app.user.service.validateuser import ValidateUser
from app.user.user import User 
from app.user.userfactory import UserFactory
from app.user.valueobject.email import Email
from app.user.Iuserrepository import IuserRepository
from app.password.Ipasswordrepository import IpassWordRepository

class CreateUser():
    
    @inject
    def __init__(self, iuserrepository: IuserRepository, ipasswordrepository: IpassWordRepository, validateuser: ValidateUser) -> None:
        """インスタンス初期化

        Args:
            iuserrepository (IuserRepository): userrepositoryのインターフェース
            ipasswordrepository (IpassWordRepository): passwordrepositoryのインターフェース
            validateuser (ValidateUser): ユーザのバリデーションを行うドメインサービス
        """        
        self.iuserrepository: Final[IuserRepository] = iuserrepository
        self.ipasswordrepository: Final[IpassWordRepository] = ipasswordrepository
        self.validateuser: Final[ValidateUser] = validateuser
    
    
    def create_user(self, param: dict) -> None:
        
        email: Email = Email(param["email"])
        user: User = UserFactory.create(email)
        
        if self.validateuser.email_duplicate(email):
            raise ValueError("メールアドレスが重複しています。")
        
        password: Password = Password(user.id, param["password"])
        
        self.iuserrepository.add(user)
        self.ipasswordrepository.add(password)
        