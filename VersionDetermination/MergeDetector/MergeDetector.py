import re
import git


class MergeDetector(object):

    def __init__(self, repository_path: str):
        self.__repository_path = repository_path
        self.__repository = git.Repo(repository_path)
        self.__init()
        pass

    def __init(self):
        self.__get_last_tag()

        pass

    def __get_last_tag(self):
        tags = self.__repository.git.log('--no-walk', '--merges', '--pretty="%H %d"', '--decorate=full').split('\n')

        print(tags)
        pass
