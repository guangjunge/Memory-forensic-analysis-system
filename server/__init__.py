import multiprocessing
import time, signal, traceback, os, sys, threading, sqlite3, subprocess, string
from flask import Flask, request, session, redirect, url_for, render_template, g
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
flask_bcrypt = Bcrypt(app)
api = Api(app)
checkout_time = 20
live_dic = {}

class Watcher:
    def __init__(self):
        """ Creates a child process, which returns. The parent
            process waits for a KeyboardInterrupt and then terminates
            the child process.
        """
        self.child = None
        self.watch()

    def watch(self):
        self.child = multiprocessing.Process(target=self.child_process)
        self.child.start()
        try:
            print('join child')
            self.child.join()
        except KeyboardInterrupt:
            # I put the capital B in KeyBoardInterrupt so I can
            # tell when the Watcher gets the SIGINT
            print('KeyBoardInterrupt')
            self.kill()
            sys.exit()

    def child_process(self):
        # Child process code goes here
        pass

    def kill(self):
        if self.child is not None and self.child.is_alive():
            self.child.terminate()
            self.child.join()


class HOST_LIVE(Resource):
    def get(self):
        return '456456'

    def put(self):
        heartbeat = request.get_json(force=True)
        NAME = heartbeat['CLIENT_NAME']
        if NAME in live_dic.keys():
            live_dic[NAME]['CLIENT_TIME'] = heartbeat['CLIENT_INFO']['CLIENT_TIME']
        else:
            live_dic[NAME] = heartbeat['CLIENT_INFO']
def check():
    while True:
        try:
            limit = time.time() - checkout_time
            for name in live_dic.keys():
                if live_dic[name]['CLIENT_TIME'] < limit:
                    del live_dic[name]
                    print("outoutout")
                else:
                    print("ininin")
            time.sleep(30)
        except Exception as e:
            print(e)

class Result(Resource):
    def get(self):
        return '123123'

    def put(self):
        r = request.get_json(force=True)
        print(r['task_result'])


api.add_resource(Result, '/task_result/')
api.add_resource(HOST_LIVE, '/active_client/')


'''
    def logwrite():
        while True:
            try:
                time.sleep(10)
                global logresult
                #logresult = str(subprocess.Popen(["tail","-n","2","log.txt"]))
                logresult = "123213"
                #print logresult
            except Exception,e:
                print e
    logmonitor = threading.Thread(target=logwrite)
    logmonitor.start()
'''

# database config
basedir = os.path.dirname(os.path.abspath(__file__)) + '\\db\\hit.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + basedir
CSRF_ENABLED = True
BCRYPT_LOG_ROUNDS = 12
app.config['SECRET_KEY'] = '6876876y78#@#@#@#}:>'
db = SQLAlchemy(app)

# init login manager
login_manager = LoginManager()
login_manager.setup_app(app)

from . import views
from . import forms
