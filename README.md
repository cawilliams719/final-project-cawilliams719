#This README includes the documentation write-up portion of the final project 

The goal of the final project script is to pull from a collection or dictionary of common land cover albedo types and to calculate 
albedo based on the mean brightness of a surface. By creating a collection of common albedo values, this portion of the code can act as 
a facilitator in creating extensive albedo scripts and act as a basis for another user’s analysis. This dictionary and the provided 
functions will allow another user to pull for instance the value portion of the dictionary to use for further analysis. For example, if 
a user wanted to average all the different land cover type albedos to see what the reflectivity of the earth’s surface typically is, 
then one can produce additional code based on the dictionary and function provided. The second portion of the code looks to calculate 
the common albedo values similar to those in the dictionary. While there are several ways to calculate albedo and at various scales, 
this code calculates albedo based on the average value of pixel brightness of a particular surface. While the code uses these values in 
measuring the reflectivity of land cover types, additional software is required to achieve these values. ImageJ was used to determine 
the surface value of grassland and the value of paper to act as a control value. White paper acts as a control due to the high 
reflectivity of a white surface. After inputting a surface and control value, a ratio is produced in the following line. This 
calculation can be accomplished for any land cover type by changing the surface value in the ratio. To find a new surface value the user 
can take a picture of any outdoor surface outside alongside a piece of paper and extract the surface value and control value 
respectively. With the created output, the following step in the equation is to multiply the result by 0.65, the typical albedo of 
paper. Lastly, a function is defined to output one of three statements based on the final albedo output derived from the calculation 
portion of the code. The magnitude of albedo is described based on three thresholds, 0.25, 0.50, and 0.75 to state that albedo is low, 
average, or high respectively. 

Little to no errors occurred in the making of this script. Due to the use of key concepts from the course, the only errors that resulted 
from writing the code, were syntax related. With minor debugging and referencing previously created scripts in lab and in-class demos, 
these errors were easily resolved. In writing the code, the difficultly only lied in the framework of the script. Deciding what to 
include in the script and for what purpose required thinking about the functionality of this albedo script, and the potential use in 
other projects. 

This script in calculating and managing albedo has great potential to act as a basis for additional projects that further explore albedo 
and the relationship across different land cover types. The benefit of this script likes in its mutability. It can easily be adapted by 
changing the values of the common albedo types or changing the surface value input if the user wishes to observe perhaps the albedo of 
artificial and urban areas. This code can be expanded to tackle research involving albedo. For example, a user can expand on the 
provided code to calculate the albedo of different forested regions at various latitudes. This code featuring albedo calculation and 
management demonstrates the versatility of key concepts in python. The functions used in this code can easily be changed to address 
another project allowing for great usability among users who may pull this code for their own scripting needs. 
