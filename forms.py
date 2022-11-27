from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField, SelectField, DecimalField, DateField, DateTimeField, IntegerRangeField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange, Optional
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

# Haha form printer go brrrr
def form_printer(fields, ddpath):
    class NewForm(Form):
        pass

    for f in fields:
        if f["datatype"] == "autointeger":
            pass
        elif f["datatype"] == "integer":
            setattr(NewForm, f["col"], IntegerField(f["name"], validators = [NumberRange(min = f["min"], max = f["max"], message = "Value should be between {0!s} and {1!s}".format(f["min"],f["max"])), DataRequired()]))
        elif f["datatype"] == "text":
            setattr(NewForm, f["col"], StringField(f["name"], validators = [Length(min = f["min"], max = f["max"], message = "Value should be between {0!s} and {1!s} characters".format(f["min"],f["max"])), DataRequired()]))
        elif f["datatype"] == "textarea":
            setattr(NewForm, f["col"], TextAreaField(render_kw = {"rows": "20"}))
        elif f["datatype"] == "dropdown":
            with open(ddpath + f["ddfile"]) as ddfile:
                ddfile = list(csv.DictReader(ddfile))
                ddfile = [i["name"] for i in ddfile]
            setattr(NewForm, f["col"], SelectField(f["name"], choices = ddfile))
        
        # todo, not immediately needed
        # elif f["datatype"] == "multiple"
        # elif f["datatype"] == "boolean"
        # elif f["datatype"] == "macaddress"
        # elif f["datatype"] == "ipaddress"
        # elif f["datatype"] == "url"

    return NewForm
    
class appsearch(Form):
    pass


