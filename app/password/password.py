from typing import ClassVar, Final
from app.user.valueobject.userid import UserId
import re


class Password():

    # 入力ルール1. ： 大文字小文字・数値・記号を最低1つ含む
    __REGEX_PATTERN: Final[str] = "\\A(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\\d)[a-zA-Z\\d]{10,20}\\Z"
    __MIN_RENGTH: Final[int] = 10
    __MAX_RENGTH: Final[int] = 20

    def __init__(self, user_id: UserId, value: str) -> None:

        if not re.fullmatch(self.__REGEX_PATTERN, value):
            raise ValueError("パスワードは数字、英語大文字小文字が必要です。")

        self.__user_id: Final[UserId] = user_id
        self.__value: Final[str] = value

    @property
    def user_id(self) -> UserId:
        return self.__user_id

    @property
    def value(self) -> str:
        return self.__value
