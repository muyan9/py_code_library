import time
from daemonize import Daemonize

def main():
    while 1:
        print 1
        time.sleep(1)

daemon = Daemonize(app="honeypot_heartbeat", pid="daemon.pid", action=main)
daemon.start()