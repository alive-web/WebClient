import tornado.ioloop
import tornado.web
import tornado.websocket
import logging

LOG_PATH = '/opt/lv128/log/'

log = logging.getLogger('socket_log')
log.setLevel(logging.INFO)
file_handler = logging.FileHandler(LOG_PATH+'web_client.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)
log.addHandler(file_handler)



class EchoWebSocket(tornado.websocket.WebSocketHandler):
    clients = set()
    def open(self):
        self.clients.add(self)
        log.info("Connection opened")
        print "WS opened"
        

    def on_message(self, message):
        log.info(message)
        msg = message
        for con in self.clients:
            con.write_message(msg)

    def on_close(self):
        log.info("Connection closed")
        print "closed"
        self.clients.remove(self) 

application = tornado.web.Application([
    (r"/", EchoWebSocket),
])


    
if __name__ == "__main__":
    
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start(
        
