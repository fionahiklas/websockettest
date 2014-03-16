import logging
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol, listenWS

# Set debug logging level
logging.basicConfig(level=logging.DEBUG)


class EchoServerProtocol(WebSocketServerProtocol):
	log = logging.getLogger("EchoServerProtocol")

        def __init__(self):
		self.log.debug("Instance initialisation")

	def onConnect(self, request):
		self.log.debug("Client connecting: "+request)

	def onOpen(self):
		self.log.debug("Opening web socket connection")

	def onMessage(self, msg, binary):
                log.debug("OnMessage: msg="+msg+" binary="+binary)
		self.sendMessage(msg, binary)


mainLogger = logging.getLogger("main")

if __name__ == '__main__':
        mainLogger.debug("Creating factory")
	factory = WebSocketServerFactory("ws://localhost:9000", debug = False)

	mainLogger.debug("Setting protocol")
	factory.protocol = EchoServerProtocol
	reactor.listenTCP(9000,factory)

	mainLogger.debug("Running the reactor")
	reactor.run()


