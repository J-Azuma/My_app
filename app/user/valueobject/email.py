from dataclasses import dataclass
from typing import ClassVar
class Email():
    """ユーザのメールアドレスを保持する

    Returns:
        _type_: Email
    """    
    _value: str
    
    
    def __init__(self, value: str) -> None:
        """インスタンス初期化

        Args:
            value (str): メールアドレスの値
        """        
        # 空文字またはNoneを許容しない
        if not value:
            raise ValueError("メールアドレスを入力してください。")
        
        # 文字列型以外を許容しない
        if not isinstance(value, str):
            raise ValueError("メールアドレスを正しく入力してください。")
        
        
        object.__setattr__(self, "_value" , value)
        
    
    @property
    def value(self) -> str:
        """変数を隠蔽する

        Returns:
            str: メールアドレスの値
        """        
        return self._value