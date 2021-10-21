def volume(slices, thickness, px_spacing):
    count_px = 0
    voxel_volume = thickness * px_spacing * px_spacing
    for slice in slices:
        count_px = count_px + slice.sum()
    return count_px * voxel_volume  * 0.001 #cm^3 = ml