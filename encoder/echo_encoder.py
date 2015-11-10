import logging
class Encoder(object):
    @staticmethod
    def encode(msg):
#        logging.debug("XXX RECVD LINE: %s", msg)
	measurements = []
	measurements.append(msg)
	return measurements
	encoded=""
        for line in msg.decode().split("\n"):
            series, value, timestamp = line.split()
            if value:
                try:
		    val,tag = value.split(",")
 	            if not tag:
		        encoded = join([ line, "\n"])
            	        measurements.append(encoded)
                except ValueError:
                    pass
	        else:
		    cleanline = (series,val,timestamp)
		    newline=" ".join(cleanline)
                    out=(msg,newline)
		    outmsg="\n".join(out)
#		    logging.debug("XXX RECVD BAD LINE: %s", line)
#		    logging.debug("XXX -- SERIES --  : %s", series)
#		    logging.debug("XXX -- VALUE --   : %s", value)
#		    logging.debug("XXX -- VAL --     : %s", val)
#		    logging.debug("XXX -- TIMEST --  : %s", timestamp)
		    #logging.debug("XXX AUTOC BAD LINE: %s", newline)
		    encoded = ' '.join([ series, val, timestamp, "\n" ])
            	    measurements.append(encoded)
        return measurements
