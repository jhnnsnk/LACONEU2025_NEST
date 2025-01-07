# Material for NEST-related tutorial at LACONEU 2025

This material is publicly available at https://github.com/jhnnsnk/LACONEU2025_NEST.

| :memo:  Please fork this repository and then clone the fork. |
| --- |
| :zap:  **Do not clone this repository directly.** |

**Latin-American Summer School in Computational Neuroscience (LACONEU)**  
Valparaíso, Chile  
6-24 January 2025   
https://laconeu.cl

**Simulated dynamics of spiking full-scale network models with NEST**

10 & 13 January 2025.  
Presented by Johanna Senk (j.senk@sussex.ac.uk).  
This tutorial gives an introduction and demonstration into modeling of the dynamics and plasticity of spiking neuronal networks. The tutorial explains graphical as well as programmatic approaches on the basis of the simulation code NEST. We emphasize that full-scale models representing all the neurons and all the synapses of a circuit are within reach, removing the uncertainties of downscaling. Examples and exercises make use of the graphical user interface NEST Desktop and Jupyter notebooks for PyNEST code using the EBRAINS infrastructure.

## EBRAINS

Go to https://www.ebrains.eu and create an EBRAINS account with your institutional email address.
If this does not work, contact the presenter and ask for a guest account.

## NEST Desktop

1. Go to https://nest-desktop.apps.hbp.eu. The Chrome browser usually works best.
1. Sign in with your EBRAINS account.
1. Click `START A NEW PROJECT`.
1. If you want to load the project prepared in this repository, go to`PROJECTS -> Import Projects -> URL` and paste the link to the `Raw` version of `1_NESTDesktop2PyNEST/balanced_network.json`.  
   (for convenience: https://raw.githubusercontent.com/jhnnsnk/LACONEU_NEST/main/1_NESTDesktop2PyNEST/balanced_network.json)  
   Press enter, select the file and `IMPORT`.

### How NEST Desktop stores models

- NEST Desktop stores models as *cookies in your browser*
- Models will disappear when your browser cleans up cookies.

| :zap: Always **export your models** to disk for safe storage. |
|---------------------------------------------------------------|

- And vice versa, if you experience any issues with the simulation, deleting cookies often helps.

## Working with the PyNEST examples on EBRAINS

| :zap:  Material not pushed from EBRAINS back to GitHub may disappear overnight. |
| --- |

1. **Fork this repository**.
1. Go to https://lab.ebrains.eu.
1. Choose Germany (Fenix DE - Jülich Supercomputing Center (JSC)) or Switzerland (Fenix CH - Swiss National Supercomputing Center (CSCS).
1. Remember which one you chose.
1. Upon "Start Server", EBRAINS spins up a virtual machine (VM) for you with 2 GB RAM.
1. You have a file browser to your left.
   - Top level is your **local home** on the VM. It exists as long as the VM.
   - **Do not use** `shared` (contains long-term storage but needs a *Collab* and is not suitable for storing Git repos) or `drive` (deprecated).
1. **Clone your fork** of the `LACONEU2025_NEST` repository under the "Git" logo in the left margin (use the HTTPS version: https://github.com/jhnnsnk/LACONEU2025_NEST.git ). There you also find tools for managing Git.
1. **Always commit and push at the end of a session.**
1. EBRAINS will from time to time shut down inactive VMs. **Any material in your VM home directory will then be lost**—remember to push!
1. You can shut down a server yourself via `File > Hub Control Panel`. The entire VM including your home on the VM is deleted then.
   
### Direct access to the execution sites

If you remember on which site your VM is running, you can contact it directly:

- https://lab.de.ebrains.eu
- https://lab.ch.ebrains.eu

Please **do not** create VMs on both sites simultaneously to avoid resource waste!
