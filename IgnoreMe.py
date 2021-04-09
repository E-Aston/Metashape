'''
import Metashape


path = Metashape.app.getOpenFileName("Specify path to the PSX document:")
doc = Metashape.Document()
doc.open(path)
chunk = doc.chunks[5]
dense_cloud = chunk.dense_cloud


dense_cloud.selectPointsByColor(color=[85,170,255], tolerance=50, channels='RGB')
dense_cloud.removeSelectedPoints()
dense_cloud.selectPointsByColor(color=[151,224,255], tolerance=50, channels='RGB')
dense_cloud.removeSelectedPoints()
dense_cloud.selectPointsByColor(color=[117,168,193], tolerance=50, channels='RGB')
dense_cloud.removeSelectedPoints()
dense_cloud.selectPointsByColor(color=[117,184,204], tolerance=25, channels='RGB')
dense_cloud.removeSelectedPoints()

'''
import Metashape

doc = Metashape.app.document
chunk = doc.chunks[0]

dense_cloud = chunk.dense_cloud


dense_cloud.selectPointsByColor(color=[206,141,47], tolerance=50, channels='RGB')
dense_cloud.removeSelectedPoints()
