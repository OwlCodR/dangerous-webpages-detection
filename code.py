import vk

accessFile = open("access.key", "r")
accessToken = accessFile.read()
accessFile.close()

groupId = input()

session = vk.Session(access_token=accessToken)
api = vk.API(session, v='5.124', lang='ru', timeout=10)
print(api.groups.getById(group_id=groupId))

#Yes it works