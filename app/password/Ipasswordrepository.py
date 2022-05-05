

from abc import ABCMeta
from abc import ABCMeta, abstractmethod
from app.password.password import Password

class IpassWordRepository(metaclass=ABCMeta):
    """Passwordリポジトリのインターフェース

    Args:
        metaclass (_type_, optional): _description_. Defaults to ABCMeta.
    """    
    @abstractmethod
    def add(self, password: Password) -> None:
        """パスワード追加処理

        Args:
            password (Password): パスワードエンティティ
        """        
        pass
    
    
    