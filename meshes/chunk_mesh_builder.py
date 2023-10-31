from settings import *

def build_chunk_mesh(chunk_voxels):
    vertex_data = np.empty(CHUNK_VOL * 18 * 5, dtype='uint8')
    index = 0

    def is_void(voxel_pos, chunk_voxels):
        x, y, z = voxel_pos
        if 0 <= x < CHUNK_SIZE and 0 <= y < CHUNK_SIZE and 0 <= z < CHUNK_SIZE:
            if chunk_voxels[x + CHUNK_SIZE * z + CHUNK_AREA * y]: 
                return False
            
        return True

    for x in range(CHUNK_SIZE):
        for y in range(CHUNK_SIZE):
            for z in range(CHUNK_SIZE):
                voxel_id = chunk_voxels[x + CHUNK_SIZE * z + CHUNK_AREA * y]
                if not voxel_id:
                    continue