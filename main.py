from codecs import xmlcharrefreplace_errors
from os import system
import sys
import itertools
from collections import OrderedDict
from operator import itemgetter
# generate random integer values
from random import seed
from random import randint
from typing import List

import numpy as np


class Project:
    def __init__(self, name, duration, score_aw, best_before, roles):
        self.name = name
        self.duration = duration
        self.score_aw = score_aw
        self.best_before = best_before
        self.roles = roles
        self.planned = False
        self.contributors = []
        self.end = None

    # def __repr__(self) -> str:
    #     return f"Project {self.name} {self.best_before}"
    #
    # def __str__(self):
    #     return f"Project {self.name} {self.best_before}"


class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    #
    # def __repr__(self) -> str:
    #     return "Clients -->  " + " Ing Like: " + str(self.arg1) + " Ing dislike: " + str(self.arg2)

    def __str__(self):
        return "{} " + str(self.name)


class Roles:
    def __init__(self, id, req):
        self.id = id
        self.req = req

    # def __repr__(self) -> str:
    #     return "Clients -->  " + " Ing Like: " + str(self.arg1) + " Ing dislike: " + str(self.arg2)
    #
    def __str__(self):
        return "{} " + str(self.id)


class Contributor:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    # def __repr__(self) -> str:
    #     return "Clients -->  " + " Ing Like: " + str(self.arg1) + " Ing dislike: " + str(self.arg2)
    #
    def __str__(self):
        return "{} " + str(self.name)


def parseInput(file):
    CONTRIBUTORS = []
    PROJECTS = []

    global C, P
    lines = []
    count = 0
    with open(file) as f:
        line = f.readline()
        count += 1
        dim = line.split()
        C = int(dim[0])
        P = int(dim[1])
        countC = 0
        countP = 0
        while (countC != C):
            line = f.readline()
            elem = line.split()
            name = elem[0]
            skills = dict()
            for i in range(int(elem[1])):
                line = f.readline()
                elem = line.split()
                skills[elem[0]] = int(elem[1])
            CONTRIBUTORS.append(Contributor(name, skills))
            countC += 1

        while (countP != P):
            roles_list = []
            line = f.readline()
            elem = line.split()
            name = elem[0]
            duration = int(elem[1])
            score = int(elem[2])
            bestday = int(elem[3])
            roles = elem[4]
            for i in range(0, int(roles)):
                line = f.readline()
                elem = line.split()
                roles_list.append(Skill(elem[0], int(elem[1])))
            PROJECTS.append(Project(name, duration, score, bestday, roles_list))
            countP += 1

        return CONTRIBUTORS, PROJECTS


def best_before(prj: Project):
    return prj.best_before


def max_level(contributors, skill, level):
    for c in contributors:
        if skill in c.skills and c.skills[skill] >= level:
            return True

    return False


def assign_contributor(project: Project, contributors: List[Contributor]) -> (Project, List[Contributor]):
    assigned_contributors = []
    temporary_contributors = []
    for role in project.roles:
        for c in contributors:
            if c.skills.get(role.name) is not None and c.name not in temporary_contributors:
                actual_skill_level = c.skills.get(role.name)
                if ((role.level == actual_skill_level - 1 and max_level(assigned_contributors, role.name,
                                                                        role.level and c.name not in temporary_contributors))
                        or actual_skill_level >= role.level and c.name not in temporary_contributors):
                    assigned_contributors.append(c)
                    temporary_contributors.append(c.name)
                    break

    if len(assigned_contributors) != len(project.roles):
        project.planned = False
        return project, contributors

    project.contributors = assigned_contributors
    contributors = list(set(contributors) - set(assigned_contributors))

    project.planned = True
    return project, contributors


def resolution(file_input):
    Contributors, Projects = parseInput(file_input)
    print(f"File {file} found {len(Contributors)} contributors and {len(Projects)} projects")
    day = 0
    not_finished = True

    Projects.sort(key=best_before)
    available_projects = Projects[:]
    started_projects = []
    available_contributors = Contributors[:]

    while not_finished:
        print(f"---- Day {day} ----")

        # Release contributors
        for started_prj in started_projects:
            if started_prj.end == day:
                # learn(project)
                available_contributors.extend(started_prj.contributors)

        # occupied_contributors = set(Contributors) - set(available_contributors)

        # Start new projects
        for i, p in enumerate(available_projects):
            prj, available_contributors = assign_contributor(p, available_contributors)
            if prj.planned:
                available_projects.pop(i)
                prj.end = day + prj.duration
                started_projects.append(prj)
        day += 100
        if len(available_projects) == 0 or day >= 100000:
            not_finished = False

    output(started_projects, file_input + ".out.txt")


def object_score(object):
    finalscore = 0

    return finalscore


def ObjectsUpdate(object):
    new_list = []
    return new_list


def all_score(solution):
    score = 0

    return score


def output(final_projects, file_input):
    sourceFile = open(file_input + "_output.txt", 'w')
    sourceFile.write("{}\n".format(str(len(final_projects))))
    for prj in final_projects:
        sourceFile.write(f"{prj.name}\n")
        for ctrb in prj.contributors:
            sourceFile.write(f"{ctrb.name} ")
        sourceFile.write("\n")
    sourceFile.close()


if __name__ == "__main__":
    input_file = ["e"]
    # input_file = ["a", "b", "c", "d", "e", "f"]
    # input_file = ["f"]

    for file in input_file:
        print("---- Start file " + file + " -----")
        resolution(file + ".txt")
