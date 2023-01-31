import jinja2

from jinja2 import Environment, FileSystemLoader

persons = [{
}]
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm1 = env.get_template('main.html')
msg = tm1.render(users=persons, title="Домашнее задание")

print(msg)
