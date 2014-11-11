import tornado.ioloop
import tornado.web
import tornado.websocket
import logging
<<<<<<< HEAD
=======



>>>>>>> 70ef4814a647c44cc623cf899857447e92687338

log = logging.getLogger('socket_log')
log.setLevel(logging.INFO)
file_handler = logging.FileHandler('web_socket.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)
log.addHandler(file_handler)
class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
<<<<<<< HEAD
        log.info("Connection opened")
=======
        print "WS opened"
        
>>>>>>> 70ef4814a647c44cc623cf899857447e92687338

    def on_message(self, message):
    	log.info(message)
        self.write_message(message)

    def on_close(self):
<<<<<<< HEAD
        log.info("Connection closed")
=======
        print "closed"
        
>>>>>>> 70ef4814a647c44cc623cf899857447e92687338
application = tornado.web.Application([
    (r"/", EchoWebSocket),
])


    
if __name__ == "__main__":
    
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
