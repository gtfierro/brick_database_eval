#!/usr/bin/env python3
import requests
import xmltodict
import subprocess
from requests.auth import HTTPBasicAuth
import time
import json
from queries import *

class HodDB(object):
    setup="""
docker pull gtfierro/hod
docker kill hod
docker rm hod
docker run -d --name hod -p47808:47808 gtfierro/hod
"""
    def __init__(self, server="http://localhost:47808/api/query",init=False):
        """
        server: HTTP API endpoint
        """
        self.server = server
        if init:
            for line in self.setup.strip().split('\n'):
                print(line.split(' '))
                print(subprocess.run(line, shell=True))

    def query(self, qstr, varorder=None):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data=qstr)
        if not resp.ok:
            print(resp, resp.reason)
            return []
        rows = resp.json().get("Rows", [])
        res = []
        for row in rows:
            for key, val in row.items():
                val = val['Namespace'] + '#' + val['Value']
                row[key] = val
            if varorder is not None:
                real = []
                for var in varorder:
                    real.append(row[var])
                res.append(real)
            else:
                res.append(row)
        return list(map(tuple, res))

    def querytime(self, qstr, varorder=None):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data=qstr)
        if not resp.ok:
            print(resp, resp.reason)
            return []
        return resp.json().get("Elapsed")


class Fuseki(object):
    setup="""
docker pull gtfierro/fuseki
docker kill fuseki
docker rm fuseki
docker run -d --name fuseki -p3031:3030 gtfierro/fuseki
"""
    def __init__(self, server="http://localhost:3031/berkeley/query",init=False):
        """
        server: HTTP API endpoint
        """
        self.server = server
        if init:
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
        return list(map(
            lambda x: tuple(map(
                lambda y: y['value'], x.values())), resp.json()['results']['bindings']))

class AlegroGraph(object):
    setup = """
docker pull gtfierro/alegrograph
docker kill alegrograph
docker rm alegrograph
docker run -d --name alegrograph -p10035:10035 gtfierro/alegrograph"""

    def __init__(self, server="http://localhost:10035/repositories/berkeley/sparql", auth=HTTPBasicAuth('root','asdfasdf') ,init=False ):
        """
        server: HTTP API endpoint
        """
        self.server = server
        self.auth = auth
        if init:
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
        obj = xmltodict.parse(resp.text)
        if obj['sparql']['results'] is None:
            return []
        num_vars = len(obj['sparql']['head']['variable'])
        if num_vars > 1:
            return list(map(lambda x:
                        tuple(map(lambda y: y['uri'], x['binding'])),
                obj['sparql']['results']['result']))
        else:
            return list(map(lambda x: tuple([x['binding']['uri']]),
                obj['sparql']['results']['result']))

class BlazeGraph(object):
    setup = """
docker pull gtfierro/blazegraph
docker kill blazegraph
docker rm blazegraph
docker run -d --name blazegraph -p9998:9998 gtfierro/blazegraph"""

    def __init__(self, server="http://localhost:9998/blazegraph/sparql",init=False):
        """
        server: HTTP API endpoint
        """
        self.server = server
        if init:
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
        obj = xmltodict.parse(resp.text)
        if obj['sparql']['results'] is None:
            return []
        num_vars = len(obj['sparql']['head']['variable'])
        if num_vars > 1:
            return list(map(lambda x:
                        tuple(map(lambda y: y['uri'], x['binding'])),
                obj['sparql']['results']['result']))
        else:
            return list(map(lambda x: tuple([x['binding']['uri']]),
                obj['sparql']['results']['result']))

class RDF3X(object):
    setup = """
docker pull gtfierro/rdf3x
docker kill rdf3x
docker rm rdf3x
docker run -d --name rdf3x -p8080:8080 gtfierro/rdf3x"""

    def __init__(self, server="http://localhost:8080/bar",init=False):
        """
        server: HTTP API endpoint
        """
        self.server = server
        if init:
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

    def __init__(self, server="http://localhost:8081/query",init=False):
        """
        server: HTTP API endpoint
        """
        self.server = server
        if init:
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
        return list(map(tuple, resp.json()))


if __name__ == '__main__':
    hod = HodDB()
    fuseki = Fuseki()
    alegro = AlegroGraph()
    blaze = BlazeGraph()
    rdf3x = RDF3X()
    rdflib = RDFlib()
