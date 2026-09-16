# try to append a tuple. It wont work.
#Name: Ayla Alameida
#Date: 9/16/2026

survey_respondants = (1012, 1035, 1021, 1053)
##surevey_respondants.append(1054) # this will raise an attribute error because tuples are immutable and do not have an append method.

survey_respondants = survey_respondants + (1054,) # this will work because we are creating a new tuple by concatenating the old tuple with a new tuple containing the new value.
print("Updated survey respondants:", survey_respondants)



