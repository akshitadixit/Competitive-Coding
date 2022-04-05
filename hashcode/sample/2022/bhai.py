from heapq import heappop, heappush, heapify
from project import Project
import contributor


class Ordonnancer:
    def __init__(self, listContributor, listProjet) -> None:
        self.listProject = listProjet
        self.listContributor = listContributor
        self.distributionTaches = []
        self.order = []
        heapify(self.order)

    def calculerScore(self, project, listContributor):
        for skills in project.skills:
            for contri in listContributor:
                if (project.skills[skills] <= contri.skills.get(skills, 0)):
                    continue
                return 0
        return project.details[1] * (1 - project.details[2])

    def evaluateProject(self):
        for project in self.listProject:
            heappush(self.order, (self.calculerScore(
                project, self.listContributor), project))

    def createDistribution(self):
        _, project = heappop(self.order)
        self.distributionTaches.append(
            (project.name, project.selectContributor(self.listContributor)))
