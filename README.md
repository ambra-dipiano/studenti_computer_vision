# studenti_computer_vision

Before cloning this repository to your local machine be sure to have set up the environment. 
You should have jupyter notebook installed alongside the <code>sagsci</code> package and all dependencies. 
You should also have installed the <code>ctools</code> software package and the <code>prod3b-v2</code> calibration database.

## 1) CTA Simulations and maps

The first tutorials will guide you throught the simulation of background and background+source observations with the <code>ctools</code> software package, and produce counts map that can be plotted as images and inspected visually. You will use a template for the background and the source models. These templates you will learn how to modify in later tutorials.

## 2) Inspect simulations

In this tutorial you will learn an alternative way of visualising the counts maps produced in the previous step. Instead of using DS9 you will use astropy and matplotlib packages.

## 3) Find the prefactor

In order to simulate a source with a given level of significance, you will learn how to use some photometry tools to extract the prefactor values required to update your source model. In this tutorial you will see a simple example for significance = 4 sigmas. 

## 4) Modify the XML source model

In this last tutorial you will learn how to use the lxml package and a wrapper class to it, in order to modify programmatically the source model. This way, you won't need to manually edit the files and you can insert this step into a python script. 
