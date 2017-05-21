#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle


enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


####   MY CODE   ####
rows=len(enron_data);
import numpy
print "Number of Entries :",rows

cols=len(enron_data["SKILLING JEFFREY K"])
print "Number of attributes :",cols
counts=0
error=0

arr=enron_data.values()

for i in range(rows):
    if (arr[i]["poi"]):
        error+=1
print counts,error
print float(error)

print "skilling money",enron_data["SKILLING JEFFREY K"]["total_payments"]
print "andrew money",enron_data["FASTOW ANDREW S"]["total_payments"]
print "andrew money",enron_data["LAY KENNETH L"]

