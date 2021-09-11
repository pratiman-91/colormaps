from glob import glob
import os

import numpy as np
import matplotlib.pyplot as plt
import colormaps as cmaps

# Manually put all the folders (May change in future!)
folders = ['cartocolors','cmocean','colorbrewer','cubehelix','ncar_ncl','scientific','tableau','sciviz']

# Generating a gradient
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

# Function to plot cmaps
def plot_color_gradients(cname):

    fig, axs = plt.subplots(nrows= 1, figsize=(8, 1.5))
    axs.imshow(gradient, aspect='auto', cmap=eval("cmaps." + cname))

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    axs.set_axis_off()

# Generate Docs for each folder
for i in range(0,len(folders)):

    # Open the file
    f= open(folders[i] + '.md',"w+")

    # Writing the headers
    header1 = "--- \n layout: default \n title: %s \n " %(folders[i])
    header2 = "nav_order: %i \n " %(i+2)
    header3 = "permalink: /docs/%s \n--- \n\n" %(folders[i])

    # Writing the main heading
    main_heading1 = "# %s \n" %(folders[i]) 
    main_heading2 = "{: .no_toc } \n\n ```python \n import colormaps as cmaps \n ``` \n\n\n"

    # Writing the tables headings
    table_heading1 = "| Name        | Colormap    | Code       | Levels     | \n"
    table_heading2 = "| ----------- | ----------- | -----------| -----------| \n"

    # Finalize all the stuff to the file
    f.write(header1)
    f.write(header2)
    f.write(header3)
    f.write(main_heading1)
    f.write(main_heading2)
    f.write(table_heading1)
    f.write(table_heading2)

    # Loop for the rows and plotting the cmaps
    for files in sorted(glob('colormaps/colormaps/' + folders[i] + '/*.rgb')):
        print("Processing: " + files)

        # Split the filenames
        cname = files.split(os.sep)
        cname = cname[-1][:-4]

        # Writing Row
        col1 = "| " + cname + "| "
        col2 = "![" + cname + "](/colormaps/assets/images/" + folders[i] + "/" + cname + ".png) | " 
        col3 = "```cmaps." + cname + "``` | "
        col4 = str(eval("cmaps." + cname + '.N')) + "| \n"

        # Finalie the rows
        f.write(col1 + col2 + col3 + col4)

        # Generate the plot of cmap
        plot_color_gradients(cname)

        # Save the plot
        #os.path.exists()
        plt.savefig('/home/ghost/Documents/colormaps/docs/assets/images/' + folders[i] + "/" + cname + ".png")

    # Close the file 
    f.close()