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
docker pull gtfierro/{name}
docker kill {name}
docker rm {name}
docker run -d --name {name} -p47808:47808 gtfierro/paperhod
"""
    def __init__(self, server="http://localhost:47808/api/query",init=False,name="paperhod"):
        """
        server: HTTP API endpoint
        """
        self.server = server
        if init:
            for line in self.setup.format(name=name).strip().split('\n'):
                print(line.split(' '))
                print(subprocess.run(line, shell=True))

    def query(self, qstr, varorder=None):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data=qstr,timeout=300)
        if not resp.ok:
            print(resp, resp.reason,resp.content)
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
        resp = requests.post(self.server, data=qstr,timeout=300)
        if not resp.ok:
            print(resp, resp.reason,resp.content)
            return []
        return resp.json().get("Elapsed")


class Fuseki(object):
    setup="""
docker pull gtfierro/{name}
docker kill {name}
docker rm {name}
docker run -d --name {name} -p3031:3030 gtfierro/fuseki
"""
    def __init__(self, server="http://localhost:3031/berkeley/query",init=False,name="fuseki"):
        """
        server: HTTP API endpoint
        """
        self.server = server
        if init:
            for line in self.setup.format(name=name).strip().split('\n'):
                print(line.split(' '))
                print(subprocess.run(line, shell=True))

    def query(self, qstr):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, params={'query': qstr},timeout=300)
        if not resp.ok:
            print(resp, resp.reason,resp.content)
            return None
        return list(map(
            lambda x: tuple(map(
                lambda y: y['value'], x.values())), resp.json()['results']['bindings']))

class AlegroGraph(object):
    setup = """
docker pull gtfierro/{name}
docker kill {name}
docker rm {name}
docker run -d --name {name} -p10035:10035 gtfierro/alegrograph"""

    def __init__(self, server="http://localhost:10035/repositories/berkeley/sparql", auth=HTTPBasicAuth('root','asdfasdf') ,init=False, name="alegrograph"):
        """
        server: HTTP API endpoint
        """
        self.server = server
        self.auth = auth
        if init:
            for line in self.setup.format(name=name).strip().split('\n'):
                print(line.split(' '))
                print(subprocess.run(line, shell=True))

    def query(self, qstr):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data={'query': qstr}, auth=self.auth,timeout=300)
        if not resp.ok:
            print(resp, resp.reason,resp.content)
            return None
        obj = xmltodict.parse(resp.text)
        if obj['sparql']['results'] is None:
            return []
        num_vars = len(obj['sparql']['head']['variable'])
        if num_vars > 1:
            return list(map(lambda x:
                        tuple(map(lambda y: y['uri'] if 'uri' in y else y['literal'], x['binding'])),
                obj['sparql']['results']['result']))
        else:
            return list(map(lambda x: tuple([x['binding']['uri']]) if 'uri' in x['binding'] else tuple([x['binding']['literal']]),
                obj['sparql']['results']['result']))

class BlazeGraph(object):
    setup = """
docker pull gtfierro/{name}
docker kill {name}
docker rm {name}
docker run -d --name {name} -p9998:9998 gtfierro/blazegraph"""

    def __init__(self, server="http://localhost:9998/blazegraph/sparql",init=False,name="blazegraph"):
        """
        server: HTTP API endpoint
        """
        self.server = server
        if init:
            for line in self.setup.format(name=name).strip().split('\n'):
                print(line.split(' '))
                print(subprocess.run(line, shell=True))

    def query(self, qstr):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data={'query': qstr},timeout=300)
        if not resp.ok:
            print(resp, resp.reason,resp.content)
            return None
        obj = xmltodict.parse(resp.text)
        if obj['sparql']['results'] is None:
            return []
        num_vars = len(obj['sparql']['head']['variable'])
        if num_vars > 1:
            return list(map(lambda x:
                        tuple(map(lambda y: y['uri'] if 'uri' in y else y['literal'], x['binding'])),
                obj['sparql']['results']['result']))
        else:
            return list(map(lambda x: tuple([x['binding']['uri']]) if 'uri' in x['binding'] else tuple([x['binding']['literal']]),
                obj['sparql']['results']['result']))

class RDF3X(object):
    setup = """
docker pull gtfierro/{name}
docker kill {name}
docker rm {name}
docker run -d --name {name} -p8080:8080 gtfierro/rdf3x"""

    def __init__(self, server="http://localhost:8080/bar",init=False,name="rdf3x"):
        """
        server: HTTP API endpoint
        """
        self.server = server
        if init:
            for line in self.setup.format(name=name).strip().split('\n'):
                print(line.split(' '))
                print(subprocess.run(line, shell=True))

    def query(self, qstr):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data=qstr,timeout=300)
        if not resp.ok:
            print(resp, resp.reason,resp.content)
            return None
        return resp

class RDFlib(object):
    setup = """
docker pull gtfierro/{name}
docker kill {name}
docker rm {name}
docker run -d --name {name} -p8082:8081 gtfierro/rdflib"""

    def __init__(self, server="http://localhost:8082/query",init=False,name="rdflib"):
        """
        server: HTTP API endpoint
        """
        self.server = server
        if init:
            for line in self.setup.format(name=name).strip().split('\n'):
                print(line.split(' '))
                print(subprocess.run(line, shell=True))

    def query(self, qstr):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data={'query': qstr},timeout=300)
        if not resp.ok:
            print(resp, resp.reason,resp.content)
            return None
        return list(map(tuple, resp.json()))

class Virtuoso(object):
    setup = """
docker pull gtfierro/{name}
docker kill {name}
docker rm {name}
docker run -d --name {name} -p8890:8890 gtfierro/virtuoso"""

    def __init__(self, server="http://localhost:8890/sparql", auth=HTTPBasicAuth('dba','dba') ,init=False, name="virtuoso"):
        """
        server: HTTP API endpoint
        """
        self.server = server
        self.auth = auth
        if init:
            for line in self.setup.format(name=name).strip().split('\n'):
                print(line.split(' '))
                print(subprocess.run(line, shell=True))

    def query(self, qstr):
        """
        qstr: query string
        returns: list of triples
        """
        resp = requests.post(self.server, data={'query': qstr}, auth=self.auth,timeout=300)
        if not resp.ok:
            print(resp, resp.reason, resp.content)
            return None
        obj = xmltodict.parse(resp.text)

        if obj['sparql']['results'] is None:
            return []
        num_vars = len(obj['sparql']['head']['variable'])
        if num_vars > 1:
            return list(map(lambda x:
                        tuple(map(lambda y: y['uri'] if 'uri' in y else y['literal'], x['binding'])),
                obj['sparql']['results'].get('result',[])))
        else:
            return list(map(lambda x: tuple([x['binding']['uri']]) if 'uri' in x['binding'] else tuple([x['binding']['literal']]),
                obj['sparql']['results'].get('result',[])))


if __name__ == '__main__':
    hod = HodDB()
    fuseki = Fuseki()
    alegro = AlegroGraph()
    blaze = BlazeGraph()
    rdf3x = RDF3X()
    rdflib = RDFlib()
