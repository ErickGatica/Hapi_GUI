import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import numpy as np

# Function to compute the result (replace with your own function)
from Spectrums import spectrum

# Function to update the plot
def update_plot():
    try:
        T_ = float(T.get())
        P_ = float(P.get())
        length_ = float(length.get())
        molecule_id_ = int(molecule_id.get())
        isotopo_id_ = int(isotopo_id.get())
        numin_ = float(numin.get())
        numax_ = float(numax.get())
        #save = float(save.get())  # Retrieve the save value as a string

        # Calling HITRAN functions and generating data
        Data = spectrum(P_, T_, length_, numin_, numax_, molecule_id_, isotopo_id_)

        #nu = 10**7/Data.nu   # conversion from cm^-1 of HITRAN to nm, CHECK
        nu=Data.nu
        coef = Data.coef
        absorp = Data.absorp
        trans = Data.trans
        radi = Data.radi
        name_isoto = Data.name_isoto  # Corrected the variable name here
        '''
        if int(save)==1:
            # Function to download data as a text file
                data_dict = {
                "Wavenumber (nu)": nu,
                "Coefficient": coef,
                "Absorbance": absorp,
                "Transmittance":trans,
                "Radiance": radi,
            }

                with open("spectra_data.txt", "w") as file:
                    for key, data in data_dict.items():
                        file.write(f"{key}:\n")
                        for value in data:
                            file.write(f"{value:.4f}\n")
                            file.write("\n")
        '''


        # Clear previous plots
        ax1.clear()
        ax2.clear()
        ax3.clear()
        ax4.clear()

        # Plotting
        ax1.plot(nu, coef)
        # Add a legend
        ax1.legend(loc='upper right')
        # Label the axes
        ax1.set_xlabel(r'$\nu$ $cm^{-1}$')
        ax1.set_ylabel(r'Coefficient $cm^2/molecule$')
        # Title
        ax1.set_title('Absorption coefficient for ' + name_isoto + '$T$=' + str(T_) + 'K $P$=' + str(P_) + 'atm')

        ax2.plot(nu, absorp)
        # Add a legend
        ax2.legend(loc='upper right')
        # Label the axes
        ax2.set_xlabel(r'$\nu$ $cm^{-1}$')
        ax2.set_ylabel(r'Absorbance')
        # Title
        ax2.set_title('Absorption spectrum for ' + name_isoto + '$T$=' + str(T_) + 'K $P$=' + str(P_) + 'atm')

        ax3.plot(nu, trans)
        # Add a legend
        ax3.legend(loc='upper right')
        # Label the axes
        ax3.set_xlabel(r'$\nu$ $cm^{-1}$')
        ax3.set_ylabel(r'Transmittance')
        # Title
        ax3.set_title('Transmittance spectrum for ' + name_isoto + '$T$=' + str(T_) + 'K $P$=' + str(P_) + 'atm')

        ax4.plot(nu, radi)
        # Add a legend
        ax4.legend(loc='upper right')
        # Label the axes
        ax4.set_xlabel(r'$\nu$ $cm^{-1}$')
        ax4.set_ylabel(r'Radiance')
        # Title
        ax4.set_title('Radiance spectrum for ' + name_isoto + '$T$=' + str(T_) + 'K $P$=' + str(P_) + 'atm')

        canvas.draw()

        return Data
    
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

    


# Create the main application window
root = tk.Tk()
root.title("Spectrum analyzer")
# Create a dark mode color scheme
dark_background = "#282c36"
dark_foreground = "#ffffff"


# Create input fields
# Create a frame for the introductory paragraph
intro_frame = ttk.Frame(root)
intro_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Add a label with your introductory paragraph text
intro_label = ttk.Label(intro_frame, text="Welcome to the Spectra Analyzer GUI!\nThis GUI allows you to obtain spectra data from HITRAN using HT (Hartmann-Tran) profile.\nDeveloped by Erick Gatica")
intro_label.pack()

# Frame for inputs
input_frame = ttk.LabelFrame(root, text="Input Parameters")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

T_label = ttk.Label(input_frame, text="Temperature [K]:")
T_label.grid(row=0, column=0)
T = ttk.Entry(input_frame)
T.grid(row=0, column=1)

P_label = ttk.Label(input_frame, text="Pressure [atm]:")
P_label.grid(row=1, column=0)
P = ttk.Entry(input_frame)
P.grid(row=1, column=1)

length_label = ttk.Label(input_frame, text="Path Length [cm]:")
length_label.grid(row=2, column=0)
length = ttk.Entry(input_frame)
length.grid(row=2, column=1)

molecule_id_label = ttk.Label(input_frame, text="Molecule ID:")
molecule_id_label.grid(row=3, column=0)
molecule_id = ttk.Entry(input_frame)
molecule_id.grid(row=3, column=1)

isotopo_id_label = ttk.Label(input_frame, text="Isotopologue ID:")
isotopo_id_label.grid(row=4, column=0)
isotopo_id = ttk.Entry(input_frame)
isotopo_id.grid(row=4, column=1)

numin_label = ttk.Label(input_frame, text="Min Wavelength [cm^-1]:")
numin_label.grid(row=5, column=0)
numin = ttk.Entry(input_frame)
numin.grid(row=5, column=1)

numax_label = ttk.Label(input_frame, text="Max Wavelength [cm^-1]:")
numax_label.grid(row=6, column=0)
numax = ttk.Entry(input_frame)
numax.grid(row=6, column=1)

'''
save_label = ttk.Label(input_frame, text="Save the data as a text file (1) or not (0):")
save_label.grid(row=7, column=0)
save = ttk.Entry(input_frame)
save.grid(row=7, column=1)
'''
# Next frame

# Create a button to trigger the function and update the plot
compute_button = ttk.Button(input_frame, text="Compute and Plot", command=update_plot)
compute_button.grid(row=8, column=0, columnspan=2)


# Create a Matplotlib figure for the plots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))
fig.subplots_adjust(hspace=0.5, wspace=0.5)  # Adjust vertical and horizontal spacing between subplots

# Create a Matplotlib canvas for embedding the figure in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=8, column=0, columnspan=2, sticky=tk.NSEW)

# Create a frame for the Matplotlib toolbar
toolbar_frame = ttk.Frame(root)
toolbar_frame.grid(row=9, column=0, columnspan=2, sticky="nsew")

# Add a Matplotlib toolbar for zooming
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.X)
canvas_widget.grid(row=10, column=0, columnspan=2, sticky=tk.NSEW)

# Configure grid row and column of plots weights to make them expand with the window
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(0, weight=1)

# Configure grid row and column of zoombar weights to make them expand with the window
root.grid_rowconfigure(10, weight=1)
root.grid_columnconfigure(0, weight=1)



# Start the Tkinter main loop
root.mainloop()
