import os

from cvat.settings.production import *

STATIC_URL=os.getenv("MLSTEAM_ANNOTATOR_BASEURL","") + "/static/"
