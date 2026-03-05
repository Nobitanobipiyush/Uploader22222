import logging

logging.basicConfig(
    format='[%(levelname)s] - %(message)s',
    level=logging.INFO
)

LOGGER = logging.getLogger(__name__)
