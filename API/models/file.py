from multiprocessing.dummy import Array
from API.models.user import User

class File:
    def __init__(self, name :str, owner_user: User):
        self._name=name
        self._owner_user = owner_user

    def getFileName(self):
        return self._name

    def getFileOwner(self):
        return self._owner_user

    def getFileURL(self):
        return self._url

    def setFileURL(self, url: str):
        self._url=url
        return self

    def setFileRecipients(self, recipients: Array):
        self._recipients= recipients
        return self

    def getFileRecipients(self):
        return self._recipients

    def setObjectID(self, id):
        self._object_id= id
        return self

    def getObjectID(self):
        return self._object_id

    def setFilePath(self, filePath):
        self._filePath = filePath
        return self

    def getFilePath(self):
        return self._filePath

