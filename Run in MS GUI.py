'''

This code is intended to be run from the Metashape GUI. As of March 2021, it works with python 3.5 - 3.8. Python 3.9 is
not supported, although this is unlikely to matter for scripts run directly from the GUI.

This script executes over all chunks of data, and expects that there are already multiple chunks in the open project,
each already populated with photographs, which is how EcoRRAP's data is structured.

There are several values within the script that are expected to be chosen by the user, which are referred to in
the script. As a default, these are:

Disable photos with quality <0.5
Align photos with high accuracy
Delete points from sparse cloud with reprojection error >0.5
Build dense cloud with low quality

'''

import Metashape


doc = Metashape.app.document
chunk = doc.chunk

for chunk in Metashape.app.document.chunks:
    chunk.analyzePhotos()

    print("---Showing quality of first 10 images as check ---")

    camera = chunk.cameras

    for camera in chunk.cameras[:10]:
        print(camera.meta["Image/Quality"])

    print("---done---")

    print("There are " + str(len(chunk.cameras)) + " photographs in this chunk.")

    ### Leave the below and above threshold values at 0, they are just a counter ###

    below_threshold = 0
    above_threshold = 0

    # Set threshold value for quality.

    threshold = 0.5

    # Function that returns number of photographs that will be rejected based on user-define threshold

    for camera in chunk.cameras:
        if float(camera.meta["Image/Quality"]) < threshold:
            below_threshold += 1
        else:
            above_threshold += 1


    print("--- Disabling cameras below " + str(threshold) + " threshold ---")
    for camera in chunk.cameras:
        if float(camera.meta["Image/Quality"]) < threshold:
            camera.enabled = False

    print(" --- Matching and aligning cameras --- ")

    '''
    
    For quality of photo matching, the following parameters correspond to metashape's GUI settings:
    
    Low quality = 4
    Medium quality = 2
    High quality = 1
    
    '''

    chunk.matchPhotos(downscale=1, generic_preselection=True, reference_preselection=True)
    chunk.alignCameras()

    print (" --- Cameras are aligned. Sparse point cloud generated ---")

    reprojthreshold = 0.5

    print (" Removing points with a reprojection error greater than " + str(reprojthreshold) + ".")

    f = Metashape.PointCloud.Filter()
    f.init(chunk, criterion = Metashape.PointCloud.Filter.ReprojectionError)
    f.selectPoints(reprojthreshold)
    f.removePoints(reprojthreshold)

    points_original = (len(chunk.point_cloud.points))

    valid_tie_points = len([p for p in chunk.point_cloud.points if p.valid])



    '''
    
    For quality of dense cloud, the downscale factor is the factor by which the image quality is reduced:
    Low quality = 8
    Medium quality = 4
    High quality = 2
    
    '''

    chunk.buildDepthMaps(downscale=8, filter_mode=Metashape.MildFiltering)
    chunk.buildDenseCloud()

    print("--- Dense cloud built. Moving on to 3D model generation ---")

    chunk.buildModel(surface_type=Metashape.Arbitrary, interpolation=Metashape.EnabledInterpolation)
    chunk.buildUV(mapping_mode=Metashape.GenericMapping)
    chunk.buildTexture(blending_mode=Metashape.MosaicBlending, texture_size=4096)

    print("--- Processing finished ---")

    print(str(below_threshold) + " photos fell below the threshold of " + str(threshold) + " and were disabled.\n"
          + str(above_threshold) + " photos were enabled.")

    print(str(points_original - valid_tie_points) + " points were removed from the sparse cloud.\n" "There were " +
          str(valid_tie_points) + " remaining from " + str(points_original) + " original points.")


doc.save()
