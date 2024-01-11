# devtype
The directory "config/devtypes" holds base configuration files for database, dropdown and form definitions for each device type.

## Directories

Each subdirectory of devtypes is a device type. However, the subdirectory "common" is not a device type but instead contains files that are shared across device types.

Device types are registered in the devtypes.json file as "tables". "common" should not be registered, if it is registed, errors during build may occur.

### Columns

Columns are defined under the "cols" key in the device type configuration. 

Behavior is different depending on what "type" is set to.

#### Type: dropdown
When "type" is set to dropdown, the model is set to CharField with choices set to the defined choices.

With "type", these are the valid keys:
- ddfile