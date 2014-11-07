
import tornado.ioloop
import tornado.web
import tornado.websocket
import logging




class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print "WS opened"
        

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print "closed"
        
application = tornado.web.Application([
    (r"/", EchoWebSocket),
])


    
if __name__ == "__main__":
    
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
