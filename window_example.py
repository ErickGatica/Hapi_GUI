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
from PIL import Image, ImageTk

#method = tk.StringVar()
#method.set("HT")  # Set a default value

# Function to update the plot
def update_plot():
    #global axis
    try:
        T_ = float(T.get())
        P_ = float(P.get())
        length_ = float(length.get())
        molecule_id_ = int(molecule_id.get())
        isotopo_id_ = int(isotopo_id.get())
        numin_ = float(numin.get())
        numax_ = float(numax.get())
        method_=str(method_var.get())
        wavestep_ = float(wavestep.get())


        if method_ not in ["HT", "V", "L", "D"]:
            messagebox.showerror("Error", "Invalid method. Please select a valid method.")
            return 0

        # Calling HITRAN functions and generating data
        Data = spectrum(P_, T_, length_, numin_, numax_, molecule_id_, isotopo_id_,method_,wavestep_)

        #nu = 10**7/Data.nu   # conversion from cm^-1 of HITRAN to nm, CHECK
        nu=Data.nu
        coef = Data.coef
        absorp = Data.absorp
        trans = Data.trans
        radi = Data.radi
        name_isoto = Data.name_isoto  # Corrected the variable name here

        # Clear previous plots, now i defined a button to do it

        # Plotting
        ax1.plot(nu, coef, label=name_isoto + ' $T$=' + str(T_) + 'K $P$=' + str(P_) + 'atm')
        # Add a legend
        ax1.legend(loc='upper right', bbox_to_anchor=(1.0, 1.0))
        # Label the axes
        ax1.set_xlabel(r'$\nu$ $cm^{-1}$')
        ax1.set_ylabel(r'Coefficient $cm^2/molecule$')
        # Title
        ax1.set_title('Absorption coefficient')

        ax2.plot(nu, absorp, label=name_isoto + ' $T$=' + str(T_) + 'K $P$=' + str(P_) + 'atm')
        # Add a legend
        ax2.legend(loc='upper right')
        # Label the axes
        ax2.set_xlabel(r'$\nu$ $cm^{-1}$')
        ax2.set_ylabel(r'Absorbance')
        # Title
        ax2.set_title('Absorption spectrum')

        ax3.plot(nu, trans, label=name_isoto + ' $T$=' + str(T_) + 'K $P$=' + str(P_) + 'atm')
        # Add a legend
        ax3.legend(loc='upper right')
        # Label the axes
        ax3.set_xlabel(r'$\nu$ $cm^{-1}$')
        ax3.set_ylabel(r'Transmittance')
        # Title
        ax3.set_title('Transmittance spectrum' )

        ax4.plot(nu, radi, label=name_isoto + '$T$=' + str(T_) + 'K $P$=' + str(P_) + 'atm')
        # Add a legend
        ax4.legend(loc='upper right')
        # Label the axes
        ax4.set_xlabel(r'$\nu$ $cm^{-1}$')
        ax4.set_ylabel(r'Radiance')
        # Title
        ax4.set_title('Radiance spectrum ')

        # Redraw the plot
        canvas.draw()

        return Data,ax1,ax2,ax3,ax4
    
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

    
def Save_data():
    try:
        T_ = float(T.get())
        P_ = float(P.get())
        length_ = float(length.get())
        molecule_id_ = int(molecule_id.get())
        isotopo_id_ = int(isotopo_id.get())
        numin_ = float(numin.get())
        numax_ = float(numax.get())
        #method_=str(method.get())
        method_="HT"
        Data = spectrum(P_, T_, length_, numin_, numax_, molecule_id_, isotopo_id_,method_)
        
        # Getting the data from the function result
        nu = Data.nu
        coef = Data.coef
        absorp = Data.absorp
        
        # Save nu and coef to a new variable
        saved_data = {'nu': nu, 'coef': coef} # This is a dictionary for saving the data
        
        # Export the saved data to a text file
        with open('saved_data.txt', 'w') as file: # The statement with is for open a resource and close it automatically when is finished
            # Writing a header
            file.write('nu, Abs_coef\n')
            for i in range(len(nu)):
                file.write(f'{nu[i]}, {coef[i]}\n')
        
        return 0

    except Exception as e:
        print(f"An error occurred saving the data")


def clear_plot():
    # Function to clear plots
    ax1.clear()
    ax2.clear()
    ax3.clear()
    ax4.clear()
    # Redraw the plot
    canvas.draw()


# Create input fields
# Create a frame for the introductory paragraph
root = tk.Tk()
intro_frame = ttk.Frame(root)
root['bg'] = 'white'
intro_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

# Add a label with your introductory paragraph text
intro_label = ttk.Label(intro_frame, text="Welcome to the Spectra Analyzer GUI!\nThis GUI allows you to obtain spectra data from HITRAN. \n Developed by Erick Gatica \n University of Colorado Boulder \n Department of Mechanical Engineering")
intro_label.pack()
# Add a second label with interesting link to the HITRAN database
intro2_label = ttk.Label(intro_frame, text="For information of the molecule and isotopologue number, visit: \n https://hitran.org/docs/molec-meta/  &   https://hitran.org/docs/iso-meta/ ")
intro2_label.pack()
# Add a third label with an image
image = Image.open(r"C:\Users\Erick\OneDrive - UCB-O365\Research\Codes\Hapi\Practising\laser_lab.jpg")
# Resize the image if needed
image = image.resize((250, 250))
# Create a PhotoImage object from the image
photo = ImageTk.PhotoImage(image)

# Add a label for the image
image_label = ttk.Label(intro_frame, image=photo)
image_label.pack()

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

wavestep_label = ttk.Label(input_frame, text="Wave number step [cm^-1]:")
wavestep_label.grid(row=7, column=0)
wavestep = ttk.Entry(input_frame)
wavestep.grid(row=7, column=1)

# Method of Compute (New variable)
method_label = ttk.Label(input_frame, text="Method of Compute HT, Voigt, Lorentz or Doppler:")
method_label.grid(row=8, column=0)
method_var = tk.StringVar()
method_dropdown = ttk.Combobox(input_frame, textvariable=method_var, values=["HT", "V", "L","D"])  # Add more values as needed
method_dropdown.grid(row=8, column=1)
method_dropdown.set("HT")  # Set a default value

# Next frame

# Create a button to trigger the function and update the plot
compute_button = ttk.Button(input_frame, text="Compute and Plot", command=update_plot)
compute_button.grid(row=9, column=0, columnspan=2)

# Create a button to to save the data
saveD_button = ttk.Button(input_frame, text="Save the last data in a text file", command=Save_data)
saveD_button.grid(row=10, column=0, columnspan=2)

# Button for clear the plots
clear_button = ttk.Button(input_frame, text="Clear the plots", command=clear_plot)
clear_button.grid(row=11, column=0, columnspan=2)

#Create 

# Create a Matplotlib figure for the plots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 8))
fig.subplots_adjust(hspace=0.5, wspace=0.5)  # Adjust vertical and horizontal spacing between subplots

# Create a Matplotlib canvas for embedding the figure in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=12, column=0, columnspan=2, sticky=tk.NSEW)

# Create a frame for the Matplotlib toolbar
toolbar_frame = ttk.Frame(root)
toolbar_frame.grid(row=13, column=0, columnspan=2, sticky="nsew")

# Add a Matplotlib toolbar for zooming
toolbar = NavigationToolbar2Tk(canvas, toolbar_frame)
toolbar.update()
toolbar.pack(side=tk.BOTTOM, fill=tk.X)
canvas_widget.grid(row=14, column=0, columnspan=2, sticky=tk.NSEW)

# Configure grid row and column of plots weights to make them expand with the window
root.grid_rowconfigure(14, weight=1)
root.grid_columnconfigure(0, weight=1)

# Configure grid row and column of zoombar weights to make them expand with the window
root.grid_rowconfigure(14, weight=1)
root.grid_columnconfigure(0, weight=1)



# Start the Tkinter main loop
root.mainloop()
