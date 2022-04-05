class Project:
    def __init__(self, name, nbr_days, Maxscore, best_before, nbr_roles) -> None:
        self.details = [nbr_days, Maxscore, best_before, nbr_roles]
        self.skills = {}
        self.name = name

    def addSkill(self, skillName, lvl):
        self.skills[skillName] = lvl

    # def addRole(self, skillName, lvl):
    #     self.role[skillName] = lvl

    def selectContributor(self, listContributor):
        role = {}
        for skills in self.skills:
            for contri in listContributor:
                if (self.skills[skills] == contri.skills.get(skills, 0)):
                    role[contri] = skills
        return role
