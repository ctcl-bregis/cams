from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length

class appsearch(Form):
    pass


class entry_memd(Form):
    mgen = StringField("Memory Generation", [DataRequired()])
    mcap = StringField("Module Capacity in MBytes", [DataRequired()])
    ddbw = StringField("Total data bit width", [DataRequired()])
    ddew = StringField("Total ECC bit width", [DataRequired()])
    dpkg = StringField("Die count per package", [DataRequired()])
    dcap = StringField("Die capacity in Mbit", [DataRequired()])
    rspd = StringField("Rated Speed (XMP) in MT/s", [DataRequired()])
    rvlt = StringField("Rated Voltage (XMP) in volts", [DataRequired()])
    tcal = StringField("Rated CAS Latency in clock cycles", [DataRequired()])
    dbnd = StringField("Memory IC brand", [DataRequired()])
    dvnd = StringField("Memory IC die vendor", [DataRequired()])
    dmpn = StringField("Memory IC part number", [DataRequired()])
    drev = StringField("Memory IC revision", [DataRequired()])
    riv1 = StringField("Register IC 1 vendor", [DataRequired()])
    rip1 = StringField("Register IC 1 part number", [DataRequired()])
    riv2 = StringField("Register IC 2 vendor", [DataRequired()])
    rip2 = StringField("Register IC 2 part number", [DataRequired()])
    pmiv = StringField("PMIC vendor", [DataRequired()])
    pmip = StringField("PMIC part number", [DataRequired()])
    note = StringField("Notes", [DataRequired()])
