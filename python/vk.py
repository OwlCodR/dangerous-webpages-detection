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
'''