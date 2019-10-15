import re

import git


class LastVersionDetector(object):

    def __init__(self, repository: str):
        self.__repository_path = repository
        self.__repository = git.Repo(repository)

        self.__major_version = None
        self.__minor_version = None
        self.__patch_version = None
        self.__commit_hash = None

        self.__init()
        pass

    @property
    def major_version(self) -> int:
        return self.__major_version

    @property
    def minor_version(self) -> int:
        return self.__minor_version

    @property
    def patch_version(self) -> int:
        return self.__patch_version

    @property
    def commit(self):
        return self.__commit_hash

    def __init(self):
        commit_hash, tag = self.__get_last_tag()

        tag = re.sub('[A-Za-z,]', '', tag)

        version = tag.split('.')
        self.__major_version = int(version[0])
        self.__minor_version = int(version[1])
        self.__patch_version = int(version[2])

        self.__commit_hash = commit_hash
        pass

    def __get_last_tag(self):
        tags = self.__repository.git.log('--no-walk', '--tags', '--pretty="%H %d"', '--decorate=full').split('\n')
        last_tag = tags[0]
        commit_hash = last_tag.split(" ")[0]
        tag = last_tag.split(" ")[3].split("/")[2]
        return commit_hash, tag


# if __name__ == "__main__":
#     vs = LastVersionDetector("/home/uwe/com.grobbles.app.gridflow4")
