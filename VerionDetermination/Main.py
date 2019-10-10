import git


repo = git.Repo("..")
heads = repo.heads
master = heads.master 
tags = repo.tags
log = master.log()

print(log)

# assert not repo.bare


# class Main(object):

#     def __init__(self):
#         print("hallo")
#         pass

#     def add(self, x: int, y: int) -> int:
#         return x + y

#         pass


# if __name__ == "__main__":
#     main = Main()
#     print(main.add(2, 3))
