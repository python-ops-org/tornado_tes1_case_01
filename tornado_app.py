'''
first module used to manage the event loop
second module  provides classes for building
'''

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):

    '''
    This class handle incoming HTTP requests
    '''

    def get(self) -> None:
        '''
        GET METHOD FOR URL
        '''
        self.write("Hello, Tornado!")

def make_app() -> tornado.web.Application:
    '''
    The make_app function is defined to create instance
    '''
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Tornado server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()

