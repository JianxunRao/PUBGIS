import mss
import numpy as np

from pubgis.match import MMAP_HEIGHT, MMAP_WIDTH, MMAP_X, MMAP_Y


class LiveFeed:  # pylint: disable=no-self-use
    def __iter__(self):
        return self

    def __next__(self):
        with mss.mss() as sct:
            frame = np.array(sct.grab(sct.monitors[1]))
        minimap = frame[MMAP_Y:MMAP_Y + MMAP_HEIGHT, MMAP_X:MMAP_X + MMAP_WIDTH][:, :, :3]
        minimap = minimap.copy()
        return 50, minimap
