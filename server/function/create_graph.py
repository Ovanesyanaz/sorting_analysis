import matplotlib.pyplot as plt
import numpy as np
import base64
import io


def draw_graphic(abscissa, ordinates):
    _, axis = plt.subplots()
    plt.plot(abscissa, ordinates)
    bytes_buffer = io.BytesIO()
    plt.savefig(bytes_buffer, format='jpg')
    bytes_buffer.seek(0)
    my_base64_jpgData = base64.b64encode(bytes_buffer.read()).decode()
    return my_base64_jpgData

draw_graphic([0,1,2],[5,4,3])