# Selects cameras in the GUI based on a user-input selection step. Useful for selecting photos at regular intervals to trim down photosets. Start by disabling all photos
# in the chunk, then run the script. Enable the cameras selected as a result.  

import Metashape

doc = Metashape.app.document
chunk = doc.chunk

step = Metashape.app.getInt("Specify the selection step:",2)
index = 1
for camera in chunk.cameras:
      if not (index % step):
            camera.selected = True
      else:
            camera.selected = False
      index += 1
