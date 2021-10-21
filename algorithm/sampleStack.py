import matplotlib.pyplot as plt

def sample_stack(stack, rows=7, cols=7, start_with=0, show_every=1, n_subplots=50, filename='imagens/'):
    fig,ax = plt.subplots(rows,cols,figsize=[10,10])
    for i in range(rows*cols):
        ind = start_with + i * show_every + 1
        if ind < n_subplots:
            ax[int(i/rows),int(i % rows)].set_title('slice %d' % ind)
            ax[int(i/rows),int(i % rows)].imshow(stack[ind],cmap='gray')
            ax[int(i/rows),int(i % rows)].axis('off')
    plt.savefig(filename)
    plt.close(fig)