import jinja2

from jinja2 import Environment, FileSystemLoader

persons = [{
}]
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons, title="Домашнее задание")

print(msg)
