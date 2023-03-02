# CAMS Software
# Purpose: Flask forms
# Date: ???, 2022 - March 1, 2023
# CTCL 2022-2023

from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField, SelectField, DecimalField, DateField, DateTimeField, IntegerRangeField, IntegerField, TextAreaField, SelectFieldBase, PasswordField
from wtforms.fields.numeric import LocaleAwareNumberField
from wtforms.widgets import NumberInput
from wtforms.widgets.core import html_params
from wtforms.validators import DataRequired, Length, NumberRange, Optional
from wtforms.utils import unset_value
import csv
from markupsafe import escape
from markupsafe import Markup

# DecimalField but with custom step values
# Adapted from flask-wtf, see flask-wtf docs/source for more information
class DecimalFieldStep(LocaleAwareNumberField):
    def __init__(self, label = None, validators = None, places = 2, rounding = unset_value, step = 1, **kwargs):
        self.widget = NumberInput(step = step)        
        super().__init__(label, validators, **kwargs)
        
        if self.use_locale and (places is not unset_value or rounding is not None):
            raise TypeError(
                "When using locale-aware numbers, 'places' and 'rounding' are ignored."
            )

        self.places = places
        self.rounding = rounding

    def _value(self):
        if self.raw_data:
            return self.raw_data[0]

        if self.data is None:
            return ""

        if self.use_locale:
            return str(self._format_decimal(self.data))

        if self.places is None:
            return str(self.data)

        if not hasattr(self.data, "quantize"):
            # If for some reason, data is a float or int, then format
            # as we would for floats using string formatting.
            format = "%%0.%df" % self.places
            return format % self.data

        exp = decimal.Decimal(".1") ** self.places
        if self.rounding is None:
            quantized = self.data.quantize(exp)
        else:
            quantized = self.data.quantize(exp, rounding=self.rounding)
        return str(quantized)

    def process_formdata(self, valuelist):
        if not valuelist:
            return
        try:
            if self.use_locale:
                self.data = self._parse_decimal(valuelist[0])
            else:
                self.data = decimal.Decimal(valuelist[0])
        except (decimal.InvalidOperation, ValueError) as exc:
            self.data = None
            raise ValueError(self.gettext("Not a valid decimal value.")) from exc

# Adapted from flask-wtf, see flask-wtf docs/source for more information
class Select2:
    validation_attrs = ["required"]

    def __init__(self, multiple=False):
        self.multiple = multiple

    def __call__(self, field, **kwargs):
        kwargs.setdefault("id", field.id)
        if self.multiple:
            kwargs["multiple"] = True
        flags = getattr(field, "flags", {})
        for k in dir(flags):
            if k in self.validation_attrs and k not in kwargs:
                kwargs[k] = getattr(flags, k)
        html = ["<select class=\"js-example-basic-single\">"]
        if field.has_groups():
            for group, choices in field.iter_groups():
                html.append("<optgroup %s>" % html_params(label=group))
                for val, label, selected in choices:
                    html.append(self.render_option(val, label, selected))
                html.append("</optgroup>")
        else:
            for val, label, selected in field.iter_choices():
                html.append(self.render_option(val, label, selected))
        html.append("</select>")
        return Markup("".join(html))

    @classmethod
    def render_option(cls, value, label, selected, **kwargs):
        if value is True:
            # Handle the special case of a 'True' value.
            value = str(value)

        options = dict(kwargs, value=value)
        if selected:
            options["selected"] = True
        return Markup(
            "<option {}>{}</option>".format(html_params(**options), escape(label))
        )

# Adapted from flask-wtf, see flask-wtf docs/source for more information
class Select2Field(SelectFieldBase):
    widget = Select2()

    def __init__(
        self,
        label=None,
        validators=None,
        coerce=str,
        choices=None,
        validate_choice=True,
        **kwargs,
    ):
        super().__init__(label, validators, **kwargs)
        self.coerce = coerce
        if callable(choices):
            choices = choices()
        if choices is not None:
            self.choices = choices if isinstance(choices, dict) else list(choices)
        else:
            self.choices = None
        self.validate_choice = validate_choice

    def iter_choices(self):
        if not self.choices:
            choices = []
        elif isinstance(self.choices, dict):
            choices = list(itertools.chain.from_iterable(self.choices.values()))
        else:
            choices = self.choices

        return self._choices_generator(choices)

    def has_groups(self):
        return isinstance(self.choices, dict)

    def iter_groups(self):
        if isinstance(self.choices, dict):
            for label, choices in self.choices.items():
                yield (label, self._choices_generator(choices))

    def _choices_generator(self, choices):
        if not choices:
            _choices = []

        elif isinstance(choices[0], (list, tuple)):
            _choices = choices

        else:
            _choices = zip(choices, choices)

        for value, label in _choices:
            yield (value, label, self.coerce(value) == self.data)

    def process_data(self, value):
        try:
            # If value is None, don't coerce to a value
            self.data = self.coerce(value) if value is not None else None
        except (ValueError, TypeError):
            self.data = None

    def process_formdata(self, valuelist):
        if not valuelist:
            return

        try:
            self.data = self.coerce(valuelist[0])
        except ValueError as exc:
            raise ValueError(self.gettext("Invalid Choice: could not coerce.")) from exc

    def pre_validate(self, form):
        if self.choices is None:
            raise TypeError(self.gettext("Choices cannot be None."))

        if not self.validate_choice:
            return

        for _, _, match in self.iter_choices():
            if match:
                break
        else:
            raise ValidationError(self.gettext("Not a valid choice."))

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
    
    # Convert into list of tuples, with both values of each tuple being the same
    choices = [(i,i) for i in choices]
    return choices

# Haha form printer go brrrr
def form_printer(fields):
    class NewForm(Form):
        pass

    for f in fields:
        fieldtype = f["datatype"]
        # autointeger is a automatically incrementing integer in the database
        if fieldtype == "autointeger":
            pass

        # Whole number
        elif fieldtype == "integer":
            vlds = [NumberRange(min = int(f["min"]), max = int(f["max"]), message = "Value should be between {0!s} and {1!s}".format(f["min"],f["max"]))]
            if f["required"] == "True":
                vlds.append(DataRequired())
            setattr(NewForm, f["col"], IntegerField(f["name"], validators = vlds))

        # Decimal numbers
        elif fieldtype == "decimal":
            vlds = [NumberRange(min = float(f["min"]), max = float(f["max"]), message = "Value should be between {0!s} and {1!s}".format(f["min"],f["max"]))]
            if f["required"] == "True":
                vlds.append(DataRequired())
            setattr(NewForm, f["col"], DecimalFieldStep(f["name"], validators = vlds, step = float(f["step"])))

        # Single-line text input
        elif fieldtype == "text":
            vlds = [Length(min = int(f["min"]), max = int(f["max"]), message = "Value should be between {0!s} and {1!s} characters".format(f["min"],f["max"])), DataRequired()]
            if f["required"] == "True":
                vlds.append(DataRequired())
            setattr(NewForm, f["col"], StringField(f["name"], validators = vlds))

        # Multi-line text input
        elif fieldtype == "textarea":
            setattr(NewForm, f["col"], TextAreaField(render_kw = {"rows": "20"}))

        # Dropdown menu
        elif fieldtype == "select":
            with open(f["ddfile"]) as ddfile:
                ddfile = list(csv.DictReader(ddfile))
                ddfile = [i["name"] for i in ddfile]
            setattr(NewForm, f["col"], SelectField(f["name"], choices = ddfile))

        # Dropdown menu with Select2
        elif fieldtype == "select2":
            with open(f["ddfile"]) as ddfile:
                ddfile = list(csv.DictReader(ddfile))
                ddfile = [i["name"] for i in ddfile]
            setattr(NewForm, f["col"], Select2Field(f["name"], choices = ddfile))

        else:
            raise Exception(f"{fieldtype} is not a valid field type") 

        # todo, not immediately needed
        # elif f["datatype"] == "multiple"
        # elif f["datatype"] == "multiple2"
        # elif f["datatype"] == "boolean"
        # elif f["datatype"] == "macaddress"
        # elif f["datatype"] == "ipaddress"
        # elif f["datatype"] == "url"

    return NewForm

class appsearch(Form):
    pass

# Hard-coded signup form
class signup(Form):
    name = StringField(
        "Name",
        validators=[DataRequired()]
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8, message="Password must be at least eight (8) characters.")
        ]
    )
    repeat = PasswordField(
        "Repeat password to confirm",
        validators=[
            DataRequired(),
            EqualTo("Password", message="Passwords must match")
        ]
    )
    submit = SubmitField('Register')

# Hard-coded login form
class LoginForm(Form):
    name = StringField(
        "Username",
        validators=[
            DataRequired(),
            Email(message="Username")
        ]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")

