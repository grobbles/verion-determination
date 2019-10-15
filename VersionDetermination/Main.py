import git

from VersionDetermination.MergeDetector.MergeDetector import MergeDetector
from VersionDetermination.LastVersionDetector.LastVersionDetector import LastVersionDetector


# https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-log.html#_pretty_formats

class Main(object):
    
    def __init__(self, repository: str):
        self.__repository_path = repository
        self.__repository = git.Repo(repository)

        last_version = LastVersionDetector(repository)
        MergeDetector(repository)
        print(last_version.major_version)
        print(last_version.minor_version)
        print(last_version.patch_version)
        pass


if __name__ == "__main__":
    vs = Main("/home/uwe/com.grobbles.app.gridflow4")
