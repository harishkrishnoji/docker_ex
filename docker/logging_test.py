import logging
logging.basicConfig(format='%(asctime)s %(levelname)s | %(module)s | %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
log = logging.getLogger("Test")
log.setLevel(logging.DEBUG)

log.info("Hello Info")
log.debug("Hello Debug")