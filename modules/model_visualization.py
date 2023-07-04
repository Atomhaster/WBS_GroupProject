import visualkeras
from PIL import ImageFont

def visualize(model, file=None):
    visualkeras.layered_view(model= model, to_file=file, legend=True)
    
if __name__ == "__main__":
    pass