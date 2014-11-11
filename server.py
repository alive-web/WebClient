import tornado.ioloop
import tornado.web
import tornado.websocket
import logging

log = logging.getLogger('socket_log')
log.setLevel(logging.INFO)
file_handler = logging.FileHandler('web_socket.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)
log.addHandler(file_handler)


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        log.info("Connection opened")
        print "WS opened"
        

    def on_message(self, message):
        log.info(message)
        self.write_message(message)

    def on_close(self):
        log.info("Connection closed")
        print "closed"

application = tornado.web.Application([
    (r"/", EchoWebSocket),
])


    
if __name__ == "__main__":
    
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
