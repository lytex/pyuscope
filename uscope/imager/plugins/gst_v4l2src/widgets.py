from PyQt5 import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from uscope.gui.control_scroll import GstControlScroll

from collections import OrderedDict

# v4l2src reports 0 as the default for these properties (not the camera's)
# Writing that back sets e.g. saturation=0 => black and white image
# Instead use None so the value is read back from the camera
groups_gst = OrderedDict([
    ("HSV+", [
        {
            "prop_name": "brightness",
            "default": None,
            "min": 0,
            "max": 255
        },
        {
            "prop_name": "contrast",
            "default": None,
            "min": 0,
            "max": 255
        },
        {
            "prop_name": "saturation",
            "default": None,
            "min": 0,
            "max": 100
        },
        {
            "prop_name": "hue",
            "default": None,
            "min": -180,
            "max": 180
        },
    ]),
])


class V4L2GstControlScroll(GstControlScroll):
    """
    Display a number of gst-toupcamsrc based controls and supply knobs to tweak them
    """
    def __init__(self, vidpip, ac=None, parent=None):
        GstControlScroll.__init__(self,
                                  vidpip=vidpip,
                                  groups_gst=groups_gst,
                                  ac=ac,
                                  parent=parent)

    # Generic camera: no exposure / auto controls exposed
    def get_exposure_disp_property(self):
        return None

    def auto_exposure_enabled(self):
        return False

    def auto_color_enabled(self):
        return False


class V4L2GstControlScrollTest(V4L2GstControlScroll):
    def auto_exposure_enabled(self):
        # Might not be true, but turns off warning
        # TODO: check if property is found
        # Assume off otherwise to avoid generating a warning for something we can't check
        return False

    def auto_color_enabled(self):
        return False
