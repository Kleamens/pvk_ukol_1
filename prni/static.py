import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='log.log',
                    filemode='w')
logger = logging.getLogger()
