#!/usr/bin/env python
#coding=utf-8
import os
import time
import logging
from multiprocessing import Process, Event
import signal

def GetTaskFromTBus( logname ):
    while True:
        time.sleep(1)

SUBPROCESSES = []
WORKERS = []
EXIT = Event()

def exit_handler(signum, frame):
    EXIT.set()
    time.sleep(1)
    for i in xrange(len(SUBPROCESSES)):
        try:
            WORKERS[i].stop_main_loop()
            os.kill(SUBPROCESSES[i].pid, 9)
        except Exception, e:
            pass

signal.signal( signal.SIGTERM, exit_handler )
signal.signal( signal.SIGINT, exit_handler )

class Processer(object):
    """docstring for Worker"""
    def __init__(self, arg ):
        super(Processer, self).__init__()
        self.arg = arg
        self.be_exit = Event()
        self.be_exit.clear()

    def stop_main_loop(self):
        self.be_exit.set()

    def main_loop(self):
        while not self.be_exit.is_set():
            try:
                GetTaskFromTBus( self.arg )
                time.sleep(1)
            except Exception, e:
                logger.exception( e )

def startprocess( worker ):
    worker.main_loop()

def createprocesser( inum ):
    '''
    @summary: create subprocess
    @return: (worker, process)
    '''
    worker = Processer( inum )
    process = Process( target = startprocess, args = ( worker, ) )
    process.daemon = True
    return ( worker, process )

if ( __name__ == '__main__' ):
    for i in range( 500 ):
        w, p = createprocesser( i )
        WORKERS.append( w )
##        p.daemon = True
        SUBPROCESSES.append( p )
    for each in SUBPROCESSES:
        each.start( )
    for each in SUBPROCESSES:
        each.join( )

    while not EXIT.is_set( ):
        iCount = 0
        for eachprocess in SUBPROCESSES:
            if ( not eachprocess.is_alive( ) ):
                w, p = createprocesser( iCount )
                SUBPROCESSES[iCount] = p
                WORKERS[iCount] = w
                p.start( )
            iCount += 1
        time.sleep( 10 )
