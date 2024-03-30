import matplotlib.pyplot as plt
import numpy as np
import base64
import io


def draw_graphic(info_about_sorting, which_sorting):
    _, axis = plt.subplots(figsize=(10, 6))

    for sort in which_sorting:
        abscissa, ordinates = np.arange(len(info_about_sorting[sort])), info_about_sorting[sort]

        axis.plot(
            abscissa,
            ordinates,
            label=f"{sort}"
        )

    # For tests
    axis.legend()
    plt.show()

    # Преобразование картинки в формат base64
    bytes_buffer = io.BytesIO()
    plt.savefig(bytes_buffer, format='jpg')
    bytes_buffer.seek(0)
    my_base64_jpgData = base64.b64encode(bytes_buffer.read()).decode()
    bytes_buffer.close()

    return my_base64_jpgData


info_about_sorting = {
    "bubble": [1, 4, 9, 16, 25],
    "quick": [1, 2, 3, 4, 5],
    "merge": [1, 2, 3.5, 5.4, 9],
    "bogo": [6, 4.7, 2, 7.2, 9],
}

which_sorting = ["bubble", "quick", "merge", "bogo"]

draw_graphic(info_about_sorting, which_sorting)