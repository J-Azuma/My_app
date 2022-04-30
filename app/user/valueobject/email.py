from dataclasses import dataclass

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
        object.__setattr__(self, "_value" , value)
        
    
    @property
    def value(self) -> str:
        """変数を隠蔽する

        Returns:
            str: メールアドレスの値
        """        
        return self._value