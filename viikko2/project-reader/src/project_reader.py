from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        di = toml.loads(content)
      
        dependensies = []
        for key in di["tool"]["poetry"]["dependencies"]:
            dependensies.append(key)
        devdeps = []
        for key in di["tool"]["poetry"]["dev-dependencies"]:
            devdeps.append(key)


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(di["tool"]["poetry"]["name"], di["tool"]["poetry"]["description"], dependensies, devdeps)
