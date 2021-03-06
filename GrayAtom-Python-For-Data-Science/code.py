# --------------
# Code starts here

# Create the lists 
class_1=["Geoffrey Hinton","Andrew Ng","Sebastian Raschka","Yoshua Bengio"]
class_2=["Hilary Mason","Carla Gentry","Corinna Cortes"]

# Concatenate both the strings
new_class=class_1+class_2
print(new_class)

# Append the list
new_class.append("Peter Warden")

# Print updated list
print(new_class)


# Remove the element from the list
new_class.remove("Carla Gentry")


# Print the list
print(new_class)



# Create the Dictionary
courses={"Math":65,"English":70,"History":80,"French":70,"Science":60}


# Store the all the subject in one variable `Total`
total=sum(courses.values())

# Print the total
print(total)


# Insert percentage formula
percentage=(total/500)*100



# Print the percentage
print(percentage)



# Create the Dictionary
mathematics={"Geoffrey Hinton":78,"Andrew Ng":95,"Sebastian Raschka":65,"Yoshua Benjio":50,"Hilary Mason":70,"Corinna Cortes":66,"Peter Warden":75}



# Find the topper in the dictionary
topper=max(mathematics,key=mathematics.get)
print(topper)


#Create variables first_name and last_name
first_name,last_name=topper.split()[0],topper.split()[1]



#Print first_name and last_name
print(first_name)
print(last_name)


#Concatenate last_name and first_name to form certificate name (last name comes first, and then first name)
full_name=last_name+" "+first_name


#Convert the certificate name to upper case
certificate_name=full_name.upper()

#Print the certificate name
print(certificate_name)

