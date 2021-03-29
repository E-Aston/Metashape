import Metashape


def netprocess(path="Z:/projects/EcoRRAP/202101/pilot_testing/Eoghan_PythonTesting.psx", tname='RunScript',
               script="C:/Users/easton/Documents/Python metashape/Run in MS GUI.py"):

    client = Metashape.NetworkClient()

    task1 = Metashape.NetworkTask()

    task1.name = tname

    task1.params['path'] = script

    client.connect('agisoft-qmgr.aims.gov.au')
    batch_id = client.createBatch(path, [task1])
    client.resumeBatch(batch_id)
    print("Job Started...")


netprocess()

