import configparser
cp = ConfigParser.RawConfigParser()
cp.read(r"C:\ProgramFiles\Mozilla Firefox\updater.ini")
print cp.sections()
print cp.options('Strings')
print cp.get('Strings', 'info')


