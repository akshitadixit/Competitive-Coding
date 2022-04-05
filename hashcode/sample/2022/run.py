from contributor import Contributor
from bhai import Ordonnancer
from project import Project
files = ["./a_an_example.in.txt"]


def process(files):
    for file in files:
        listContributor = []
        listProjet = []
        with open(file, "r") as f:
            C, P = (f.readline().split())
            for i in range(int(C)):
                name, numberSkill = f.readline().split()
                contributor = Contributor(name)
                listContributor.append(contributor)
                for j in range(int(numberSkill)):
                    skill, lvl = f.readline().split()
                    contributor.addSkill(skill, lvl)
            for k in range(int(P)):
                name, nbr_days, score, bb, roles = f.readline().split()
                project = Project(name, int(nbr_days), int(
                    score), int(bb), int(roles))
                for _ in range(int(roles)):
                    skill, lvl = f.readline().split()
                    project.addSkill(skill, lvl)
                listProjet.append(project)
            ordonnancer = Ordonnancer(listContributor, listProjet)
            ordonnancer.evaluateProject()
            ordonnancer.createDistribution()

        with open("out/a_output.txt", 'w') as f:
            f.write(len(ordonnancer.distributionTaches))
            print(len(ordonnancer.distributionTaches))
            for project in ordonnancer.distributionTaches:
                f.write(project[0])
                print(project[0])
                for contri in project[1]:
                    f.write(contri.name+" ", end="")
                    print(contri.name+" ", end="")
                f.write("")


if (__name__ == "__main__"):
    process(files)
