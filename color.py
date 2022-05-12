import colorsys

original_rgb = 0.8, 0.2, 0.7
print(original_rgb)
print(type(original_rgb))

# convert from RGB to HSV
# NOTE: operator * will unpack the tuple and then the elements 
# can be used as args
hsv = colorsys.rgb_to_hsv(*original_rgb)
print(hsv)
print(type(hsv))

# convert from HSV to RGB
rgb = colorsys.hsv_to_rgb(*hsv)
print(rgb)
print(type(rgb))

