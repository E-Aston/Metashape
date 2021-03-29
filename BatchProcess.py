import Metashape

doc = Metashape.app.document

chunk = doc.chunk

### match photos
task = Metashape.NetworkTask()
task.name = 'MatchPhotos'
task.params['keypoint_limit'] = 40000


client = Metashape.NetworkClient()
client.connect('agisoft-qmgr.aims.gov.au')
batch_id = client.createBatch('processing.project.psx', [task])
client.resumeBatch(batch_id)
print("Job Started...")