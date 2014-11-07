
import tornado.ioloop
import tornado.web
import tornado.websocket
import logging

log.getLogger('log')
log_file = logging.FileHandler('log.log')
log_file.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
log_file.setFormatter(formatter)
log.addHandler(log_file)


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        log.info('WebSocket opened' + self.current_user )
        

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        
application = tornado.web.Application([
    (r"/", EchoWebSocket),
])


    
if __name__ == "__main__":
    
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
