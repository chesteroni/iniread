import ConfigParser
import StringIO
import sys

iniPath='config.ini'
expectedVariables = ['host', 'port', 'user', 'pass']
config = {}

try:
    iniAsStr = '[section]\n' + open(iniPath, 'r').read()
    iniFp = StringIO.StringIO(iniAsStr)
    configRead = ConfigParser.RawConfigParser()
    configRead.readfp(iniFp)
except:
    print "Missing config file: " + iniPath
    sys.exit()

for var in expectedVariables:
    if var not in configRead.options("section"):
        print "Missing config variable: " + var
	sys.exit()
    config[var] = configRead.get("section", var).strip('"')


print config['host']
print config['port']
print config['user']
print config['pass']
