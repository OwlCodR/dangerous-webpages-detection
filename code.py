import vk

def printUserInfo(userID):
    print(api.users.get(user_ids=userID)[0])

accessFile = open("access.key", "r")
accessToken = accessFile.read()
accessFile.close()

session = vk.Session(access_token=accessToken)
api = vk.API(session, v='5.124', lang='ru', timeout=10)

groups = ['104658778', '104658778', '172239942', '161204702', '179390182']
maxMembers = '10'

for group_id in groups:
    print()
    for member_id in api.groups.getMembers(group_id=group_id, count=maxMembers).get('items'):
        printUserInfo(member_id)

'''
Example data
{'id': 27385, 'first_name': 'Сергей', 'last_name': 'Билетов', 'is_closed': False, 'can_access_closed': True}
{'id': 90807, 'first_name': 'Алексей', 'last_name': 'Цыганов', 'is_closed': True, 'can_access_closed': False}
{'id': 419729, 'first_name': 'Юрий', 'last_name': 'Альфист', 'is_closed': False, 'can_access_closed': True}
{'id': 1576826, 'first_name': 'Дмитрий', 'last_name': 'Ильвовский', 'deactivated': 'banned'}
{'id': 1722490, 'first_name': 'Елизавета', 'last_name': 'Денисова', 'is_closed': True, 'can_access_closed': False}
{'id': 2339913, 'first_name': 'Сергей', 'last_name': 'Латышев', 'is_closed': True, 'can_access_closed': False}
{'id': 2521750, 'first_name': 'DELETED', 'last_name': '', 'deactivated': 'deleted'}
{'id': 2541045, 'first_name': 'Сергей', 'last_name': 'Иванов', 'is_closed': False, 'can_access_closed': True}
{'id': 3608532, 'first_name': 'Владимир', 'last_name': 'Александров', 'is_closed': True, 'can_access_closed': False}
{'id': 3744563, 'first_name': 'Александр', 'last_name': 'Бирюков', 'is_closed': False, 'can_access_closed': True}

{'id': 27385, 'first_name': 'Сергей', 'last_name': 'Билетов', 'is_closed': False, 'can_access_closed': True}
{'id': 90807, 'first_name': 'Алексей', 'last_name': 'Цыганов', 'is_closed': True, 'can_access_closed': False}
{'id': 419729, 'first_name': 'Юрий', 'last_name': 'Альфист', 'is_closed': False, 'can_access_closed': True}
{'id': 1576826, 'first_name': 'Дмитрий', 'last_name': 'Ильвовский', 'deactivated': 'banned'}
{'id': 1722490, 'first_name': 'Елизавета', 'last_name': 'Денисова', 'is_closed': True, 'can_access_closed': False}
{'id': 2339913, 'first_name': 'Сергей', 'last_name': 'Латышев', 'is_closed': True, 'can_access_closed': False}
{'id': 2521750, 'first_name': 'DELETED', 'last_name': '', 'deactivated': 'deleted'}
{'id': 2541045, 'first_name': 'Сергей', 'last_name': 'Иванов', 'is_closed': False, 'can_access_closed': True}
{'id': 3608532, 'first_name': 'Владимир', 'last_name': 'Александров', 'is_closed': True, 'can_access_closed': False}
{'id': 3744563, 'first_name': 'Александр', 'last_name': 'Бирюков', 'is_closed': False, 'can_access_closed': True}

{'id': 14278468, 'first_name': 'Никита', 'last_name': 'Соломонов', 'is_closed': False, 'can_access_closed': True}
{'id': 15864567, 'first_name': 'Денис', 'last_name': 'Егоров', 'is_closed': False, 'can_access_closed': True}
{'id': 17469710, 'first_name': 'Николя', 'last_name': 'Ланин', 'is_closed': False, 'can_access_closed': True}
{'id': 17606604, 'first_name': 'Алина', 'last_name': 'Берикбол', 'is_closed': True, 'can_access_closed': False}
{'id': 24393908, 'first_name': 'Полина', 'last_name': 'Пушкарева', 'is_closed': False, 'can_access_closed': True}
{'id': 25222703, 'first_name': 'Николай', 'last_name': 'Калинкин', 'is_closed': True, 'can_access_closed': False}
{'id': 25782053, 'first_name': 'Светлана', 'last_name': 'Кириченко', 'is_closed': False, 'can_access_closed': True}
{'id': 27646241, 'first_name': 'Ксения', 'last_name': 'Смирнова', 'is_closed': False, 'can_access_closed': True}
{'id': 32324207, 'first_name': 'Эльнара', 'last_name': 'Джавадова', 'is_closed': True, 'can_access_closed': False}
{'id': 33024723, 'first_name': 'Аня', 'last_name': 'Вергунова', 'is_closed': False, 'can_access_closed': True}

{'id': 3233002, 'first_name': 'Илья', 'last_name': 'Белов', 'is_closed': False, 'can_access_closed': True}
{'id': 3578424, 'first_name': 'Серёга', 'last_name': 'Афанасьев', 'is_closed': False, 'can_access_closed': True}
{'id': 22835053, 'first_name': 'Елена', 'last_name': 'Киптева', 'is_closed': True, 'can_access_closed': False}
{'id': 25782053, 'first_name': 'Светлана', 'last_name': 'Кириченко', 'is_closed': False, 'can_access_closed': True}
{'id': 40633266, 'first_name': 'Сергей', 'last_name': 'Лобанов', 'is_closed': False, 'can_access_closed': True}
{'id': 40901502, 'first_name': 'Яна', 'last_name': 'Цветкова', 'is_closed': True, 'can_access_closed': False}
{'id': 50590609, 'first_name': 'Андрей', 'last_name': 'Кузьмин', 'is_closed': False, 'can_access_closed': True}
{'id': 67595063, 'first_name': 'Даниил', 'last_name': 'Декапольцев', 'is_closed': True, 'can_access_closed': False}
{'id': 78774525, 'first_name': 'Ира', 'last_name': 'Ерохина', 'is_closed': False, 'can_access_closed': True}
{'id': 83184393, 'first_name': 'Елизавета', 'last_name': 'Соловьёва', 'is_closed': True, 'can_access_closed': False}

{'id': 661198, 'first_name': 'Юлия', 'last_name': 'Hatesweets', 'is_closed': False, 'can_access_closed': True}
{'id': 19072710, 'first_name': 'Феликс', 'last_name': 'Астольфов', 'is_closed': True, 'can_access_closed': False}
{'id': 23136094, 'first_name': 'Дарья', 'last_name': 'Афоничева', 'is_closed': True, 'can_access_closed': False}
{'id': 34182386, 'first_name': 'Наталия', 'last_name': 'Жеребкина', 'is_closed': True, 'can_access_closed': False}
{'id': 39089177, 'first_name': 'Арсений', 'last_name': 'Берч', 'is_closed': False, 'can_access_closed': True}
{'id': 41103408, 'first_name': 'Святослав', 'last_name': 'Ершов', 'is_closed': False, 'can_access_closed': True}
{'id': 46798580, 'first_name': 'Влада', 'last_name': 'Яковлева', 'is_closed': False, 'can_access_closed': True}
{'id': 52024394, 'first_name': 'Николай', 'last_name': 'Миронов', 'is_closed': False, 'can_access_closed': True}
{'id': 55853034, 'first_name': 'Дамир', 'last_name': 'Гизатуллин', 'is_closed': False, 'can_access_closed': True}
{'id': 58080770, 'first_name': 'Даша', 'last_name': 'Бычкова', 'is_closed': False, 'can_access_closed': True}
'''