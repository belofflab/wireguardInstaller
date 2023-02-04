from http.server import HTTPServer, SimpleHTTPRequestHandler


class CORSRequestHandler(SimpleHTTPRequestHandler):
  def end_headers(self):
    if self.client_address[0] not in ['194.87.82.228', ]:
      return self.send_response(code=403, message='No access to see this page')
    return super(CORSRequestHandler, self).end_headers()

if __name__ == '__main__':
  httpd = HTTPServer(('0.0.0.0', 8000), CORSRequestHandler)
  httpd.serve_forever()