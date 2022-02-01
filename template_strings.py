# Template strings use $placeholder for a value that will be swapped in later.
# Template strings are often used for internationalization.
# Template string's substitute() can take a dictionary-like object 
# or keyword arguments.

from string import Template   # It's using the built-in string.py file

# Template string's substitute() can take keyword arguments
t = Template("This is $name's YouTube channel")
t.substitute(name="MrBeast")
print(t)   # <string.Template object at 0x7f4d9b8bd210>

print(Template("This is $name's YouTube channel").substitute(name="MrBeast"))

print(Template('Here is the calendar for the $year school year').substitute(year="2017-18"))

d = {
    "name": "Mary",
    "age": 8
}

# Template string's substitute() can take a dictionary-like object
print(Template("$name is $age years old.").substitute(d))
