#!/usr/bin/env python

import os
from app import app
from models.mysql.rds import db as rds
from flask_script import Manager, Shell, Server, prompt_bool
from flask_migrate import Migrate, MigrateCommand

manager = Manager(app)#, with_default_commands=False)

migrate = Migrate(app,rds)
manager.add_command('db', MigrateCommand)

# @manager.command
@manager.option('-n', '--name', help='your name')
def hello(name):
	print("hello", name)

manager.add_command("runserver", Server(host='192.168.10.34', port='5000'))


def gen_admin(app, **kwargs):
    from app import admin_app
    ## easiest but possibly incomplete way to copy your settings
    return admin_app(config=app.config, **kwargs)
sub_manager = Manager(gen_admin)

manager.add_command("admin", sub_manager)

@manager.command
def dropdb():
	"drop db"
	result = prompt_bool("Are you sure to delete all databases?")
	print(result)
	if result:
		print("ahahaa")
		pass

if __name__ == '__main__':
	manager.run()
