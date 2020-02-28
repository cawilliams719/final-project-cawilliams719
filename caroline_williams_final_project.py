"""
Caroline Williams
February 28, 2020
Python Final Project
Python 2.7.14
Calculating Albedo
URL: http://albedodreams.info/how_to/how-to-calculate-albedo-yourself/
The website above inspired the script below.
"""



"""
Part 1: The first half of the script is created to print the reflectance of
various cover types by creating a dictionary and function tom print the key,
value pair. This script can easily be modified to print just the key or the
value, if you wish to work with just the land cover types or albedos.
"""

#Dictionary of common albedo values based on cover type
covertype_albedo = {'soil': 0.10, 'sand': 0.20, 'grass': 0.25,
                    'crops': 0.20, 'tundra': 0.25, 'forest': 0.15,
                    'water': 0.05, 'snow': 0.95, 'ice': 0.45}

#Prints the key and corresponding values of a dictionary
def print_albedo (dictionary): #defines a new function and takes an argument
    for (key,value) in dictionary.items(): 
        print(key,value) 

print_albedo(covertype_albedo) #prints both the land cover type and albedo

#Prints the key of a dictionary
def print_landcover (dictionary): 
    for (key,value) in dictionary.items(): 
        print(key) 
        
print_landcover(covertype_albedo) #prints both the land cover type 

#Prints the key of a dictionary
def print_reflectance (dictionary): 
    for (key,value) in dictionary.items(): 
        print(key)
        
print_reflectance(covertype_albedo) #prints both the albedo in the dictionary

"""
Part 2: the URL above (line 7) inspired the creation of the second half of
this script. Using ImageJ software, the surface value of grassland and of paper was calculate.
The ratio of these two values are then used to calculate albedo, creating the albedo_final output.
Lastly, a function is created to print various statements based on albedo_final. It describes
if the albedo is high, average, or low based on the values 0.75, 0.50, and 0.25 respectively.
"""

#Calculate Albedo
surf_value = 120.456 #Input the mean brightness value of any land cover surface
control_val = 254.999 #Control variable in the ratio
albedo_ratio = surf_value/control_val #albedo ratio

#Multiply the Albedo ratio by the standard paper value 0.65 to get the final albedo
albedo_final = albedo_ratio*0.65 #0.65 is the standard paper value albedo
print (albedo_final) #final albedo value


#Defining the function Albedo to print the degree of albedo based on percentage
def albedo(x):
    if x>=0.75: 
        print("Albedo is high.") 
    elif x>=0.50: 
        print("Albedo is average.")
    else:
        x>=0.25
        print("Albedo is low.")
    
albedo(albedo_final)
