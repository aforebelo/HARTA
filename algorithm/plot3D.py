from skimage import measure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_3d(image, threshold=0, filename = 'imagens/3d.png'):
    'Position the scan upright,'
    'so the head of the patient would be at the top facing the camera'
    p = image.transpose(2, 1, 0)
    p = p[:, :, ::-1]

    verts, faces = measure.marching_cubes(p, threshold, method='_lorensen')

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    'Fancy indexing: `verts[faces]` to generate a collection of triangles'
    mesh = Poly3DCollection(verts[faces], alpha=0.1)
    face_color = [0.5, 0.5, 0.5]
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)

    ax.set_xlim(0, p.shape[0])
    ax.set_ylim(0, p.shape[1])
    ax.set_zlim(0, p.shape[2])

    plt.savefig(filename)
    plt.close()