import eventlet
eventlet.monkey_patch()  # noqa
import sys
import yaml
import logging

from nameko.constants import AMQP_URI_CONFIG_KEY
from nameko.cli.run import run, import_service

from .. import autoreload

AUTORELOAD_CONFIG_KEY = 'AUTORELOAD'

logger = logging.getLogger(__name__)


def main(args):
    if '.' not in sys.path:
        sys.path.insert(0, '.')

    if args.config:
        with open(args.config) as fle:
            config = yaml.load(fle)
    else:
        config = {
            AMQP_URI_CONFIG_KEY: args.broker
        }

    if args.logging_config_file:
        logging.config.fileConfig(
            args.logging_config_file, disable_existing_loggers=False)
    elif 'LOGGING' in config:
        logging.config.dictConfig(config['LOGGING'])
    else:
        logging.basicConfig(level=logging.INFO, format='%(message)s')

    services = []
    for path in args.services:
        services.extend(
            import_service(path)
        )

    kwargs = {'backdoor_port': args.backdoor_port}
    if config.get(AUTORELOAD_CONFIG_KEY):
        logger.info('autoreload enabled')
        autoreload.make_autoreload(run, args=(services, config), kwargs=kwargs)
    else:
        run(services, config, **kwargs)
