
import functools
from xmlrpc import client as xmlrpclib

HOST = 'localhost'
PORT = 8070
DB = 'openacademy'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST, PORT)
 
# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print("Logged in as %s (uid:%d)" % (USER, uid))
 
call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)
 
# 2. Read the sessions
sessions = call('openacademy.session','search_read', [], ['session_name', 'seats'])
for session in sessions:
    print("Session %s (%s seats)" % (session['session_name'], session['seats']))

# 3. Create a new session
course_id = call('openacademy.course', 'search', [('course_name', 'ilike', 'Programming Languages & Structures')])[0]
session_id = call('openacademy.session', 'create', {'session_name': 'Fall-2018', 'course_id': course_id})