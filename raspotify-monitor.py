from flask import Flask, redirect
from jinja2 import Template
from subprocess import getoutput
import re

app = Flask(__name__)
status_template = Template(open('templates/status.html', 'r').read())


def refresh_status():
    stdout = getoutput("sudo netstat -anpt | awk '((/LISTEN/||/ESTABLISHED/)&&/librespot/)||/Program/{;print $0}'")
    stati = {'run': False, 'listen': False, 'established': False, 'statuslines': []}
    if re.search(r"(LISTEN\s+\d+\/librespot)", stdout, re.MULTILINE):
        stati['listen'] = True
    if re.search(r"(ESTABLISHED\s+\d+\/librespot)", stdout, re.MULTILINE):
        stati['established'] = True
    stdout2 = getoutput("sudo service raspotify status")
    stati['statuslines'] = stdout2.split('\n')
    if re.search(r"(Active:\sactive\s\(running\))", stdout2, re.MULTILINE):
        stati['run'] = True
    return stati


def control_service(task):
    stdout = getoutput("sudo service raspotify " + task)
    return stdout


@app.route('/')
def home():
    return redirect("/status", code=301)


@app.route('/status')
def status():
    print("STATUS CALLED")
    stati = refresh_status()
    return status_template.render(
        listenstatus=stati['listen'],
        establishedstatus=stati['established'],
        runstatus=stati['run'],
        statuslines=stati['statuslines'][:5],
        refreshtime=7
    )


@app.route('/restart')
def restart():
    output = control_service('restart')
    if output == '':
        return 'OK'
    else:
        return 'ERROR'


@app.route('/start')
def start():
    output = control_service('start')
    if output == '':
        return 'OK'
    else:
        return 'ERROR'


@app.route('/stop')
def stop():
    output = control_service('stop')
    if output == '':
        return 'OK'
    else:
        return 'ERROR'


if __name__ == '__main__':
    app.run()
