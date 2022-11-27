# script to automate generating mcap and dcap dropdown values, which can be extremely tedious to do by hand
# CAMS - CrazyblocksTechnologies Computer Laboratories - November 23, 2022
import csv

mcap_mults = ["B", "K", "M", "G", "T"]
mcap_mults_full = ["Bytes", "Kibibytes", "Mebibytes", "Gibibytes", "Tebibytes"]
dcap_mults_full = ["Bits", "Kibibits", "Mebibits", "Gibits", "Tebibits"]
nums = ["1", "2", "4", "8", "16", "24", "32", "48", "64", "96", "128", "512"]
nums_pad = [i.rjust(3, "0") for i in nums]

# mcap, cipn values
mcap_cipn = []
for x in mcap_mults:
    for y in nums_pad:
        mcap_cipn.append(y + x)

# mcap, name values
mcap_name = []
for x in mcap_mults_full:
    for y in nums:
        mcap_name.append(y + " " + x)

dictlist = []
for x, y in zip(mcap_cipn, mcap_name):
    dictlist.append({"name": y, "cipn": x}) 

dialect = csv.unix_dialect

with open("mcap.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames = ["name", "cipn"], dialect = dialect)
    writer.writeheader()
    writer.writerows(dictlist)

# mcap, cipn values
dcap_cipn = []
for x in mcap_mults:
    for y in nums_pad:
        dcap_cipn.append(y + x)

# mcap, name values
dcap_name = []
for x in dcap_mults_full:
    for y in nums:
        dcap_name.append(y + " " + x)

dictlist = []
for x, y in zip(dcap_cipn, dcap_name):
    dictlist.append({"name": y, "cipn": x}) 

dialect = csv.unix_dialect

with open("dcap.csv", "w") as f:
    writer = csv.DictWriter(f, fieldnames = ["name", "cipn"], dialect = dialect)
    writer.writeheader()
    writer.writerows(dictlist)


