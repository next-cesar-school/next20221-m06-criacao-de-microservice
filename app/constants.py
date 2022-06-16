
# Number of chars in String attributes from db.tables
CHARS_NAME = 100
CHARS_DATE = 10
CHARS_REGISTRATION_NUMBER = 15

# List of values for Enum attributes
PROJECT_STATUS = ('ongoing', 'on hold', 'finished', 'on approval')
PROJECT_FLAG = ('red', 'yellow', 'green')
USER_STATUS = ('active', 'inactive')

# Return messages in CRUD methods
GENERAL_ID_NOT_FOUND = {'message': 'Oops! This ID was not found'}, 404
GENERAL_ID_ALREADY_EXISTS = {'message': 'ID already exists.'}, 400
GENERAL_ID_DELETED = {'message': 'Deleted successfully.'}, 200
GENERAL_INTERNAL_ERROR_SAVE = {
    'message': 'An internal error occurred when trying to save this.'}, 500
GENERAL_INTERNAL_ERROR_DELETE = {
    'message': 'An internal error occurred when trying to delete this.'}, 500

USER_REGISTRATION_NUMBER_ALREADY_EXISTS = {
    'message': 'User registration number already exists.'}, 400
COST_CENTER_SECTOR_ALREADY_EXISTS = {
    'message': 'Cost center sector already exists.'}, 400

PROJECT_NOT_FOUND = {'message': 'Oops! Project ID is not valid'}, 404
USER_NOT_FOUND = {'message': 'Oops! User ID is not valid'}, 404
