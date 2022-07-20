 # unix shell syntax
from string import Template
tmpl = Template("welcome $name, what a $adjective player")
print(f"tmpl :{tmpl}")
res = tmpl.substitute(name="Sachin", adjective="super")
print(res)


# format string from python
print("Welcome {}, what a {} player for {}".format("Sachin", "superb", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin","superb", "India"))
print("Welcome {gname}, what a {adj} player for {cntry}".format(gname="Sachin", adj="superb", cntry="India"))
print("Welcome {name}, your rating of {rating:.3f}, what a player".format(name="sachin", rating=4))

# interpolation
from math import pi, e
print(f"PI = {pi} and Eulers constant ={e}")

print("PI ={} and Eulers constant ={}".format(pi, e))
print("PI = {0} and Eulers constant = {1} and magic number = {2}".format(pi, e, 40585))
print("PI = {} and Eulers constant = {} and magic number = {magic}".format(pi, e, magic=40585))
print("PI = {0} and Eulers constant = {1} and magic number = {magic}".format(pi, e, magic=40585))

print("-" * 40)
fullname = ["Sachin", "Tendulkar"]
print(f"fullname :{fullname}")
print("Mr.{name}".format(name="Sachin"))





print("-" * 40)
import math
print(__name__)
print(math.__name__)

print("The {mod.__name__} module gives the value of pi= module and eulers=")