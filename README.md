# ascii

Turns images into ascii art

## Installation
```shell
pip install ascii
```

## Basic Usage
```python
import ascii # import the package

output = ascii.loadFromUrl("http://i.imgur.com/ITx3Jcd.jpg") # load a funny picture :)
print(output)
```

## Advanced Usage
### Convert one pixel
```
output = ascii.onePixel(13,13,13) # some arbitrary rgb values
```

### Create image with fixed width
```
output = ascii.loadFromUrl("http://i.imgur.com/ITx3Jcd.jpg", columns=100)
``

### Don't color image
```
output = ascii.loadFromUrl("http://i.imgur.com/ITx3Jcd.jpg", color=False)
```