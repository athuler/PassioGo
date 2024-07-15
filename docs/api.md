
# API Reference

## `TransportationSystem`

- **id** (*int*): ID of the system
- **name** (*str*): The full name of the system
- **username** (*str*): URL-friendly system name
- **goAgencyName** (*str*): Display name of the system
- **email** (*str*): Contact email address for the system
- **goTestMode** (*bool*): Unknown
- **name2** (*bool*): Unknown
- **homepage** (*str*): URL to the agency's homepage
- **logo** (*bool*): Unknown
- **goRoutePlannerEnabled** (*bool*): Unknown
- **goColor** (*str*): Unknown
- **goSupportEmail** (*str*): Unknown
- **goSharedCode** (*int*): Unknown
- **goAuthenticationType** (*bool*): Unknown


## `getSystems()`

Gets all systems supported by PassioGo.

**Inputs**:

- **appVersion** (*int*): Version of the application (Default: 2)
- **sortMode** (*int*): Unknown (Default: 1)

**Returns**: *list* of [`TransportationSystem`](#transportationsystem)


## `printAllSystemsMd()`

Prints all system names as a markdown list.

**Input**:

- **includeHtmlBreaks** (*bool*): Whether to include HTML line breaks (Default: True)

**Returns**: None


## `getAllRoutes()`

Obtains every route for the selected system.

**getAllRoutes**(systemSelected = 1068, paramDigit = 1, amount = 1)

- **systemSelected**: 
- **paramDigit**: 
- **amount**: 

## `getAllStops()`

## `getSystemAlerts()`

## `getBuses()`



