import logging
import sys
from twisted.python import log
from twisted.internet import reactor
from autobahn.twisted.websocket import WebSocketServerFactory, WebSocketServerProtocol

# Set debug logging level
logging.basicConfig(level=logging.DEBUG)


class EchoServerProtocol(WebSocketServerProtocol):
	logger = logging.getLogger("EchoServerProtocol")

        def __init__(self):
		self.logger.debug("Instance initialisation")

	def onConnect(self, request):
		self.logger.debug("Client connecting: %s " % str(request))

	def onOpen(self):
		self.logger.debug("Opening web socket connection")

	def onMessage(self, msg, binary):
                self.logger.debug("OnMessage")
		self.sendMessage(msg, binary)


mainLogger = logging.getLogger("main")

if __name__ == '__main__':

	log.startLogging(sys.stdout)

        mainLogger.debug("Creating factory")
	factory = WebSocketServerFactory("ws://localhost:9000", debug = True )

	mainLogger.debug("Setting protocol")
	factory.protocol = EchoServerProtocol
	reactor.listenTCP(9000, factory)

	mainLogger.debug("Running the reactor")
	reactor.run()


