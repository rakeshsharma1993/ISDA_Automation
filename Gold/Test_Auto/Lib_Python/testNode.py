import urllib2, json  
from robot.libraries.BuiltIn import BuiltIn  
from robot.api import logger  
from urlparse import urlparse  

class testNode(object):
    
    def get_node_hostname(self,host, port):
        #s2l = BuiltIn().get_library_instance('CustomSeleniumLibrary')
        s2l = BuiltIn().get_library_instance('Selenium2Library')
        session_id = s2l._current_browser().session_id
        query_url = 'http://%s:%s/grid/api/testsession?session=%s' % (host, port, session_id)
        req = urllib2.Request(url=query_url)
        resp = urllib2.urlopen(req).read()
        json_blob = json.loads(resp)
        if 'proxyId' in json_blob:
            proxy_id = json_blob['proxyId']
            print '*WARN* Le test s\'est joue sur le node : %s' % proxy_id
            parse_result = urlparse(proxy_id)
            return parse_result.hostname
        else:
            raise RuntimeError('Failed to get hostname. Is Selenium running locally? hub response: %s' % resp)
