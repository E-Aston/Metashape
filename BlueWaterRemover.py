# Cleans the dense cloud of the active chunk to remove dead points associated with blue water. 
# Save the document beforehand in case parts of the mesh are deleted

import Metashape


doc = Metashape.app.document
chunk = Metashape.app.document.chunk

dense_cloud = chunk.dense_cloud


dense_cloud.selectPointsByColor(color=[85,170,255], tolerance=50, channels='RGB')
dense_cloud.removeSelectedPoints()
dense_cloud.selectPointsByColor(color=[151,224,255], tolerance=50, channels='RGB')
dense_cloud.removeSelectedPoints()
dense_cloud.selectPointsByColor(color=[117,168,193], tolerance=50, channels='RGB')
dense_cloud.removeSelectedPoints()
dense_cloud.selectPointsByColor(color=[117,184,204], tolerance=25, channels='RGB')
dense_cloud.removeSelectedPoints()
