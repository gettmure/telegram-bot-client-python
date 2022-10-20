import json
import urllib.request as request
from enum import Enum
from typing import Any, Dict, Iterable, TypeVar, TypedDict

T = TypeVar('T')


class TelegramMethod(Enum):
    GET_ME = 'getMe'
    GET_UPDATES = 'getUpdates'


class GetMeResponse(TypedDict):
    username: str
    # def __init__(self, response: dict[str, T]) -> None:
    # self.username = response['username']


class UpdateResponse(TypedDict):
    id: int
    message: str
    # def __init__(self, response: dict[str, T]) -> None:
    #     self.id = response['update_id']
    #     self.message = 'EmptyMessage'

    #     try:
    #         self.message = response['message']['text']
    #     except KeyError:
    #         self.message = 'NO MESSAGE! I THINK IT IS STICKER OR SMTH...'


class TelegramBot:
    def __init__(self, token: str) -> None:
        self.tgUrl = "https://api.telegram.org/bot%s/{method}" % (token)

        self.__last = 0

    def listenUpdates(self) -> None:
        while (True):
            lastUpdate = self.getUpdates()[-1]

            if self.__last == lastUpdate.id:
                continue
            else:
                self.__last = lastUpdate.id

            print(lastUpdate.message)

    def getMe(self) -> GetMeResponse:
        response = self.__sendRequest(TelegramMethod.GET_ME)

        return {'username': response['username']}

    def getUpdates(self) -> list[UpdateResponse]:
        response = self.__sendRequest(TelegramMethod.GET_UPDATES)

        def apply(item: Dict[str, Any]) -> UpdateResponse:
            return {'id': item['id'], 'message': item['message']['text']}

        return list(map(apply, response))

    def __sendRequest(
            self, method: TelegramMethod) -> Dict[str, Any]:
        response = request.urlopen(self.tgUrl.format(method=method.value))

        return json.loads(response.read().decode())['result']
