# ascii

Turns images into ascii art

## Installation
```shell
pip install ascii
```

## Usage
```python
import ascii

#
# CONVERT WHOLE IMAGE
#

output = ascii.loadFromUrl("http://i.imgur.com/ITx3Jcd.jpg") # load a funny picture :)
print(output) # display it here

#
# CONVERT ONE PIXEL
#

output = ascii.onePixel(13,13,13) # rgb values go here
print(output) # display this one pixel
```