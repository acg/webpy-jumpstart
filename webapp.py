#!/usr/bin/env python

import web
from os import getpid

urls = ( '(/.*)', 'WebApp' )
app = web.application( urls, globals() )
state = { 'counter': 0 }


class WebApp:

  def __init__(self):
    global state
    self.state = state

  def GET(self, path):
    self.state['counter'] += 1
    return "Request number %d for path %s query %s for pid %d\n" % (
      self.state['counter'], path, web.ctx.query, getpid() )


if __name__ == '__main__':
  app.run()

