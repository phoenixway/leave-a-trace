#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.request import urlopen, HTTPError
from webbrowser import open_new

REDIRECT_URL = 'http://localhost:3000/'
PORT = 3000
ACCESS_URI = 'https://public-api.wordpress.com/oauth2/authorize?client_id=78848&redirect_uri={}&response_type=token&blog=wayofphoenix'.format(REDIRECT_URL)
CLIENT_ID = 78848
CLIENT_SECRET = ''

def get_access_token_from_url(url):
    """
    Parse the access token from Facebook's response
    Args:
        uri: the facebook graph api oauth URI containing valid client_id,
             redirect_uri, client_secret, and auth_code arguements
    Returns:
        a string containing the access key 
    """
    token = str(urlopen(url).read(), 'utf-8')
    return token.split('=')[1].split('&')[0]

class HTTPServerHandler(BaseHTTPRequestHandler):

    """
    HTTP Server callbacks to handle Facebook OAuth redirects
    """
    def __init__(self, request, address, server, a_id, a_secret):
        self.app_id = a_id
        self.app_secret = a_secret
        super().__init__(request, address, server)

    def do_GET(self):
        # GRAPH_API_AUTH_URI = ('https://graph.facebook.com/v2.2/oauth/' 
        #     + 'access_token?client_id=' + self.app_id + '&redirect_uri=' 
        #     + REDIRECT_URL + '&client_secret=' + self.app_secret + '&code=')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        print('yy')
        # if 'code' in self.path:
        #     self.auth_code = self.path.split('=')[1]
        #     self.wfile.write(bytes('<html><h1>You may now close this window.'
        #                       + '</h1></html>', 'utf-8'))
        #     self.server.access_token = get_access_token_from_url(
        #             GRAPH_API_AUTH_URI + self.auth_code)

    # Disable logging from the HTTP Server
    def log_message(self, format, *args):
        return



open_new(ACCESS_URI)
httpServer = HTTPServer(
                ('localhost', PORT),
                lambda request, address, server: HTTPServerHandler(
                    request, address, server, CLIENT_ID, CLIENT_SECRET))
httpServer.handle_request()
#print(httpServer.access_token )