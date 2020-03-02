import argparse
import os
from xfinity_bot import XfinityBot

USERNAME = os.environ["XFINITY_USERNAME"]
PASSWORD = os.environ["XFINITY_PASSWORD"]
WAIT_SECONDS = 10


def expose(service_name, ip, port):
    try:
        bot = XfinityBot()
        bot.login(USERNAME, PASSWORD).wait(WAIT_SECONDS)
        bot.toggle_port_forwarding(True).wait(WAIT_SECONDS)
        bot.add_service_port(service_name, ip, port).wait(WAIT_SECONDS)
        return True
    except Exception as e:
        print(e)
    finally:
        bot.shutdown()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage Xfinity router settings")
    parser.add_argument("--username", help="Username to login")
    parser.add_argument("--password", help="Password to login")

    subparsers = parser.add_subparsers(help="Command", dest="command")

    expose_service = subparsers.add_parser("expose", help="Expose service port")
    expose_service.add_argument("--service-name", help="Service name")
    expose_service.add_argument("--ip", help="IP of service to expose")
    expose_service.add_argument("--port", type=int, help="Port of service to expose")

    args = parser.parse_args()

    USERNAME = args.username if args.username else USERNAME
    PASSWORD = args.password if args.password else PASSWORD

    if args.command == "expose":
        expose(args.service_name, args.ip, args.port)
