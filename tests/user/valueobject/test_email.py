from app.user.valueobject.email import Email
from tests.util.factory import create_email

def test_Emailインスタンス生成_正常系():
    # 事前準備： なし
    
    # 操作： インスタンス生成
    email = create_email()
    
    # 想定結果：1. インスタンスが正しく生成されている
    assert isinstance(email, Email)
    
    # 2. メールアドレスの値が正常
    assert isinstance(email.value , str)
    assert email.value == "hoge@example.com"
    