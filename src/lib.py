# CAMS Software
# Purpose: Commonly used functions, inspired by Rust's lib.rs
# Date: Febuary 1, 2023 - February 10, 2023
# CTCL 2023

import csv

def csv2list(path):
	with open(path) as f:
		ls = list(csv.DictReader(f))
		
	return ls
