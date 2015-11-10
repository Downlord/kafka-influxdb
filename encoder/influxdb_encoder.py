import logging
class Encoder(object):
    def encode(self, msg):
        """
        Don't change the message at all
        """
	logging.debug("XXX RECVD LINE: %s", msg)
        return msg
