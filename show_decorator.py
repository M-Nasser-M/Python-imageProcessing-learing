# you can add this decorator to your filter function in the filter function file
# so each image open up after it being modified and saved
def show_image(func):
    def wrapper_func(*args,**kwargs):
        img =func(*args,**kwargs)
        img.show()
    return wrapper_func