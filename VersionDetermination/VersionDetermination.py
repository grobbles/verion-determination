import git


# https://mirrors.edge.kernel.org/pub/software/scm/git/docs/git-log.html#_pretty_formats

class VersionDetermination:

    def __init__(self, repository: str):
        self.__repository_path = repository
        self.__repository = git.Repo(repository)
        pass

    def get_last_tag(self):
        tags = self.__repository.git.log('--no-walk', '--tags', '--pretty="%H %d"', '--decorate=full').split('\n')
        last_tag = tags[0]
        commit_hash = last_tag.split(" ")[0]
        tag = last_tag.split(" ")[3].split("/")[2]
        return commit_hash, tag


if __name__ == "__main__":
    vs = VersionDetermination("/home/uwe/com.grobbles.app.gridflow4")
    vs.get_last_tag()
    print(vs.get_last_tag())
