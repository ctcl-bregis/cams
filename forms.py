from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
import csv

def getdropdown(col, path):
    # Get device type file, path provided by path
    
    with open(path + "cols.csv") as cols:
        cols = list(csv.DictReader(cols))
    
    # Get "row" (dictionary in list) with column name defined by col
    choices = next(x for x in cols if x["col"] == col)
    
    # Get associated CSV file with dropdown value definitions
    with open(path + choices["ddfile"], "r") as dd:
        dd = list(csv.DictReader(dd))
        choices = [i["name"] for i in dd]
        print(choices)
    
    choices = [(i,i) for i in choices]
    return choices

# Form printer go brrrr
def form_factory(fields):
    class NewForm(Form):
        pass

    for f in fields:
        pass

class appsearch(Form):
    pass

# This may not be needed anymore?
class memd(Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        with open("config/devtypes/memd/cols.csv") as f:
            cols = list(csv.DictReader(f))

        self.fieldlist = []
        for i in cols:
            if i['datatype'] == "dropdown":
                choices = getdropdown(i['col'], "config/devtypes/memd/")
            
                field = SelectField(i['name'], validators=[DataRequired()], choices = choices).bind(self, i['col'])
                field.data = None
                self._fields[i['col']] = field
            
            elif i['datatype'] == "disabled": 
                field = StringField(i['name'], validators=[DataRequired()]).bind(self, i['col'])
                self._fields[i['col']] = field
        
            
        
    #mgen = SelectField("Memory Generation", [DataRequired()], choices = getdropdown("mgen", "config/devtypes/memd/"))
    #mcap = StringField("Module Capacity in MBytes", [DataRequired()])
    #ddbw = StringField("Total data bit width", [DataRequired()])
    #ddew = StringField("Total ECC bit width", [DataRequired()])
    #dpkg = StringField("Die count per package", [DataRequired()])
    #dcap = StringField("Die capacity in Mbit", [DataRequired()])
    #rspd = StringField("Rated Speed (XMP) in MT/s", [DataRequired()])
    #rvlt = StringField("Rated Voltage (XMP) in volts", [DataRequired()])
    #tcal = StringField("Rated CAS Latency in clock cycles", [DataRequired()])
    #dbnd = StringField("Memory IC brand", [DataRequired()])
    #dvnd = SelectField("Memory IC die vendor", [DataRequired()], choices = getdropdown("dvnd", "config/devtypes/memd/"))
    #dmpn = StringField("Memory IC part number", [DataRequired()])
    #drev = StringField("Memory IC revision", [DataRequired()])
    #riv1 = SelectField("Register IC 1 vendor", [DataRequired()], choices = getdropdown("riv1", "config/devtypes/memd/"))
    #rip1 = StringField("Register IC 1 part number", [DataRequired()])
    #riv2 = SelectField("Register IC 2 vendor", [DataRequired()], choices = getdropdown("riv2", "config/devtypes/memd/")) 
    #rip2 = StringField("Register IC 2 part number", [DataRequired()])
    #pmiv = SelectField("PMIC vendor", [DataRequired()], choices = getdropdown("pmiv", "config/devtypes/memd/")) 
    #pmip = StringField("PMIC part number", [DataRequired()])
    #note = StringField("Notes", [DataRequired()])


