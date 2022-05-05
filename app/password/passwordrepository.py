from app.password.Ipasswordrepository import IpassWordRepository
from app.configration.database.initdb import session
from app.password.password import Password
from app.password.passworddto import PasswordDto
from app.password.convertpassword import ConvertPassword

class PasswordRepository(IpassWordRepository):
    """パスワード集約のリポジトリ実装クラス

    Args:
        IpassWordRepository (_type_): リポジトリのインターフェース
    """    
    def __init__(self) -> None:
        """インスタンス初期化
        """        
        self.session = session
        
    # パスワードのハッシュ化はインフラ層のConvertPasswordクラスの責務とする
    # ※ ハッシュ化はドメイン知識の範疇からは外れるため
    def add(self, password: Password) -> None:
        """パスワードを追加

        Args:
            password (Password): パスワードエンティティ
        """     
        passworddto: PasswordDto = PasswordDto.from_entity(password)
        hashed_passworddto: PasswordDto = ConvertPassword.hash(passworddto)
        self.add(hashed_passworddto)