from ulid import ULID
from app.user.valueobject.email import Email
from app.user.valueobject.userid import UserId
from app.user.user import User

class UserFactory():
    
    # 注： インスタンスの再構成や、Userクラスのインスタンスメソッドからインスタンスを
    # 生成する時はIDの同一性を担保するためにこのメソッドを使わない。
    @staticmethod
    def create(emai: Email) -> User:
        """Userインスタンスを初期化するFactoryメソッド

        Args:
            emai (Email): Emailインスタンス

        Returns:
            User: Userインスタンス
        """        
        userid: UserId = UserId(str(ULID))
        user: User = User(userid, emai)
        return user