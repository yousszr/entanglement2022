from codecs import xmlcharrefreplace_errors
from os import system
import sys
import itertools
from collections import OrderedDict
from operator import itemgetter
# generate random integer values
from random import seed
from random import randint
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

    # def __repr__(self) -> str:
    #     return "Project -->  " + " : " + str(self.arg1) + " Ing dislike: " + str(self.arg2)

    # def __str__(self):
    #     return "Clients -->  " + " Ing Like: " + str(self.arg1) + " Ing dislike: " + str(self.arg2)


class Skill:
    def __init__(self, name, level):
        self.name = name
        self.level = level
    #
    # def __repr__(self) -> str:
    #     return "Clients -->  " + " Ing Like: " + str(self.arg1) + " Ing dislike: " + str(self.arg2)

    # def __str__(self):
    #     return "Clients -->  " + " Ing Like: " + str(self.arg1) + " Ing dislike: " + str(self.arg2)
    #

class Roles:
    def __init__(self, id, req):
        self.id = id
        self.req = req

    # def __repr__(self) -> str:
    #     return "Clients -->  " + " Ing Like: " + str(self.arg1) + " Ing dislike: " + str(self.arg2)
    #
    # def __str__(self):
    #     return "Clients -->  " + " Ing Like: " + str(self.arg1) + " Ing dislike: " + str(self.arg2)
    #

class Contributor:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    # def __repr__(self) -> str:
    #     return "Clients -->  " + " Ing Like: " + str(self.arg1) + " Ing dislike: " + str(self.arg2)
    #
    # def __str__(self):
    #     return "Clients -->  " + " Ing Like: " + str(self.arg1) + " Ing dislike: " + str(self.arg2)


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
            skills = []
            for i in range(int(elem[1])):
                line = f.readline()
                elem = line.split()
                skills.append(Skill(elem[0], int(elem[1])))
            CONTRIBUTORS.append(Contributor(name, skills))
            countC += 1

        while (countP != P):
            line = f.readline()
            elem = line.split()
            name = elem[0]
            duration = int(elem[1])
            score = int(elem[2])
            bestday = int(elem[3])
            roles = elem[4]
            for i in range(int(roles)):
                line = f.readline()
                elem = line.split()
                skills.append(Skill(elem[0], int(elem[1])))
            PROJECTS.append(Project(name, duration, score, bestday, skills))
            countP += 1

        return CONTRIBUTORS, PROJECTS


def object_score(object):
    finalscore = 0

    return finalscore


def ObjectsUpdate(object):
    new_list = []
    return new_list


def all_score(solution):
    score = 0

    return score


def output(objects, file_input):
    sourceFile = open(file_input + "_output.txt", 'w')
    sourceFile.write("{} ".format(str(len(objects))) + " ".join(list(objects)))
    sourceFile.close()


def resolution(file_input):
    Contributors, Projects = parseInput(file_input)
    print(f"File {file} found {len(Contributors)} contributors and {len(Projects)} projects")
    objects = []
    not_finished = False
    while (not_finished):

        if (True):  # Pulisco la lista di ingredienti da quelli scelti
            newscore = []
            if (newscore > scores):
                scores = newscore

            Objects = ObjectsUpdate(objects)  # aggiorna la lista dei clietni,
            print("SCORE --> " + str(scores))

        else:

            not_finished = False

    output(objects, file_input)


def object_score(object):
    finalscore = 0

    return finalscore


def ObjectsUpdate(object):
    new_list = []
    return new_list


def all_score(solution):
    score = 0

    return score


def output(objects, file_input):
    sourceFile = open(file_input + "_output.txt", 'w')
    sourceFile.write("{} ".format(str(len(objects))) + " ".join(list(objects)))
    sourceFile.close()


if __name__ == "__main__":

    input_file = ["a"]
    # input_file = ["a", "b", "c", "d", "e"]

    for file in input_file:
        print("---- Start file " + file + " -----")
        # file_input = open(file + ".txt", "r")
        # file_output = open("output_" + file + ".txt", "w")
        resolution(file + ".txt")
