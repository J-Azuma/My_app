from injector import inject
from typing import Final
from sqlalchemy.exc import SQLAlchemyError
from app.password.password import Password
from app.user.service.validateuser import ValidateUser
from app.user.user import User 
from app.user.userfactory import UserFactory
from app.user.valueobject.email import Email
from app.user.Iuserrepository import IuserRepository
from app.password.Ipasswordrepository import IpassWordRepository
from app.configration.database.initdb import db_session

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
        """ユーザをリポジトリに渡す

        Args:
            param (dict): パラメータ

        Raises:
            ValueError: メールアドレスが重複
        """        
        
        email: Email = Email(param["email"])
        user: User = UserFactory.create(email)
        
        if self.validateuser.email_duplicate(email):
            raise ValueError("メールアドレスが重複しています。")
        
        password: Password = Password(user.id, param["password"])
        
        # 整合性担保のためにトランザクションを張る
        try:
            self.iuserrepository.add(user)
            db_session.flush()
            self.ipasswordrepository.add(password)
            db_session.commit()
        except SQLAlchemyError as e:
            db_session.rollback()
            raise SQLAlchemyError("ユーザ登録中にエラーが発生しました。")