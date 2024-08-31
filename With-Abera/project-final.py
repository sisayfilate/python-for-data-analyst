import pandas as pd
import numpy as np

...


bmi = None


def full_name(fname, lname):
    return fname + " " + lname


bmi["full name"] = bmi.apply(
    lambda row: full_name(row["first name"], row["last name"]), axis=1
)
