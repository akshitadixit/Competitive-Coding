class Contributor:
    def __init__(self, name) -> None:
        self.name = name
        self.skills = {}
        self.currentProject = ""

    def setProject(self, project):
        self.currentProject = project

    def upgradeSkills(self, skillName):
        self.skills[skillName] = self.skills.get(skillName, 0) + 1

    def addSkill(self, skillName, lvl):
        self.skills[skillName] = lvl
