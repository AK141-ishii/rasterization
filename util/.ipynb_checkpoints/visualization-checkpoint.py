import matplotlib.pyplot as plt


def plot_figures(origin_data, pred_X1, pred_X2, pred_y, caption=None):
    """
    plot two figs
        target data (original)
        processed data
    input:
    origin_data : origin_data, shape=[[x1,x2,y], ...]
    pred_X1 : array x1_cor
    pred_X2 : array x2_cor
    pred_y  : array output
    
    return : plt.fig
    """
    fig = plt.figure(figsize=(10,5))
    ax_origin = fig.add_subplot(1,2,1)
    ax_origin = plt.imshow(origin_data)
    ax_pred = fig.add_subplot(1,2,2)
    ax_pred.scatter(pred_X1, pred_X2, c=pred_y, marker='.')
    if caption != None:
        ax_pred.set_xlabel(caption)
    return fig