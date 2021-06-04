import win32api
import win32print
import logging
from configuration import config

configitems = config.configuration()
DBConnString = configitems["databaseconnstr"]
logfilename = configitems["logfilename"]
loglevel = configitems["loglevel"]

logging.basicConfig(filename=logfilename, level=loglevel)

def printdefault(filename):

    logging.debug("filename: " + str(filename))

    win32api.ShellExecute(
    0,"print",
    filename,
    '/d: "%s"' % win32print.GetDefaultPrinter(),
    '.',
    0
    )

    logging.debug(win32print.GetDefaultPrinter())
    return None