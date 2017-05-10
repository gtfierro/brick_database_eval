#!/usr/bin/env python3
import requests
import subprocess
from requests.auth import HTTPBasicAuth
import time

class HodDB(object):
    setup="""
docker pull gtfierro/hod
docker kill hod
docker rm hod
docker run -d --name hod -p47808:47808 gtfierro/hod
"""
    def __init__(self, server="http://localhost:47808/api/query"):
        """
        server: HTTP API endpoint
        """
        self.server = server
        for line in self.setup.strip().split('\n'):
            print(line.split(' '))
            print(subprocess.run(line, shell=True))

    def query(self, qstr):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data=qstr)
        if not resp.ok:
            print(resp, resp.reason)
            return []
        return resp

class Fuseki(object):
    setup="""
docker pull gtfierro/fuseki
docker kill fuseki
docker rm fuseki
docker run -d --name fuseki -p3031:3030 gtfierro/fuseki
"""
    def __init__(self, server="http://localhost:3031/berkeley/query"):
        """
        server: HTTP API endpoint
        """
        self.server = server
        for line in self.setup.strip().split('\n'):
            print(line.split(' '))
            print(subprocess.run(line, shell=True))

    def query(self, qstr):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, params={'query': qstr})
        if not resp.ok:
            print(resp, resp.reason)
            return None
        return resp

class AlegroGraph(object):
    setup = """
docker pull gtfierro/alegrograph
docker kill alegrograph
docker rm alegrograph
docker run -d --name alegrograph -p10035:10035 gtfierro/alegrograph"""

    def __init__(self, server="http://localhost:10035/repositories/berkeley/sparql", auth=HTTPBasicAuth('root','asdfasdf')  ):
        """
        server: HTTP API endpoint
        """
        self.server = server
        self.auth = auth
        for line in self.setup.strip().split('\n'):
            print(line.split(' '))
            print(subprocess.run(line, shell=True))

    def query(self, qstr):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data={'query': qstr}, auth=self.auth)
        if not resp.ok:
            print(resp, resp.reason)
            return None
        return resp

class BlazeGraph(object):
    setup = """
docker pull jbkoh/blazegraph
docker kill blazegraph
docker rm blazegraph
docker run -d --name blazegraph -p9998:9998 jbkoh/blazegraph"""

    def __init__(self, server="http://localhost:9998/blazegraph/sparql"):
        """
        server: HTTP API endpoint
        """
        self.server = server
        for line in self.setup.strip().split('\n'):
            print(line.split(' '))
            print(subprocess.run(line, shell=True))

    def query(self, qstr):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data={'query': qstr})
        if not resp.ok:
            print(resp, resp.reason)
            return None
        return resp

class RDF3X(object):
    setup = """
docker pull gtfierro/rdf3x
docker kill rdf3x
docker rm rdf3x
docker run -d --name rdf3x -p8080:8080 gtfierro/rdf3x"""

    def __init__(self, server="http://localhost:8080/bar"):
        """
        server: HTTP API endpoint
        """
        self.server = server
        for line in self.setup.strip().split('\n'):
            print(line.split(' '))
            print(subprocess.run(line, shell=True))

    def query(self, qstr):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data=qstr)
        if not resp.ok:
            print(resp, resp.reason)
            return None
        return resp

class RDFlib(object):
    setup = """
docker pull gtfierro/rdflib
docker kill rdflib
docker rm rdflib
docker run -d --name rdflib -p8081:8081 gtfierro/rdflib"""

    def __init__(self, server="http://localhost:8081/query"):
        """
        server: HTTP API endpoint
        """
        self.server = server
        for line in self.setup.strip().split('\n'):
            print(line.split(' '))
            print(subprocess.run(line, shell=True))

    def query(self, qstr):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data={'query': qstr})
        if not resp.ok:
            print(resp, resp.reason)
            return None
        return resp
    

if __name__ == '__main__':
    hod = HodDB()
    fuseki = Fuseki()
    alegro = AlegroGraph()
    blaze = BlazeGraph()
    rdf3x = RDF3X()
    rdflib = RDFlib()
