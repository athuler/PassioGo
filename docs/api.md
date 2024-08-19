
# API Reference

## `getSystems()`

Gets all systems supported by PassioGo.

**Inputs**:

- **appVersion** (*int*): Version of the application (Default: 2)
- **sortMode** (*int*): Unknown (Default: 1)

**Returns**: *list* of [`TransportationSystem`](#transportationsystem)

```python
passiogo.getSystems()
```

```
[<passiogo.TransportationSystem at 0x1d62cb54a30>,
 <passiogo.TransportationSystem at 0x1d62cb54b20>,
 <passiogo.TransportationSystem at 0x1d62d8bb310>,
 ...
 <passiogo.TransportationSystem at 0x1d62d599be0>,
 <passiogo.TransportationSystem at 0x1d62d599c10>]
```

## `getSystemFromID()`

Gets the system with the corresponding id. If there is no match, returns *None*.

**Inputs**:

- **appVersion** (*int*): Version of the application (Default: 2)
- **sortMode** (*int*): Unknown (Default: 1)

**Returns**:  [`TransportationSystem`](#transportationsystem) or *None* if no match

```python
passiogo.getSystemFromID(1068)
```

```
<passiogo.TransportationSystem at 0x1d62da31550>
```


## `TransportationSystem`

### `TransportationSystem.__init__()`

**id** is the only required parameter, all other default to *None*.

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

```json
{'id': 1068,
 'name': 'University of Chicago',
 'username': 'chicago',
 'goAgencyName': 'University of Chicago',
 'email': 'bus@uchicago.edu',
 'goTestMode': False,
 'name2': False,
 'homepage': 'https://safety-security.uchicago.edu/en/transportation',
 'logo': True,
 'goRoutePlannerEnabled': False,
 'goColor': '#843c39',
 'goSupportEmail': 'bus@uchicago.edu',
 'goSharedCode': 1312,
 'goAuthenticationType': False}
```

### `TransportationSystem.getRoutes()`

Get all routes for the appropriate system.

**Input**:

- **appVersion** (*int*): Version of the application (Default: 1)
- **amount** (*int*): Unknown (Default: 1)

**Output**: *List* of [`Route`](#route)

```python
passiogo.getSystemFromID(1068).getRoutes()
```

```
[<passiogo.Route at 0x1d62db3fac0>,
 <passiogo.Route at 0x1d62db3f520>,
 <passiogo.Route at 0x1d62db3f790>,
 <passiogo.Route at 0x1d62db3fdc0>,
 <passiogo.Route at 0x1d62db3fa90>,
 <passiogo.Route at 0x1d62db3ff10>,
 <passiogo.Route at 0x1d62db3f2e0>,
 <passiogo.Route at 0x1d62db3f310>,
 <passiogo.Route at 0x1d62db3fb20>,
 <passiogo.Route at 0x1d62db3f4f0>,
 <passiogo.Route at 0x1d62db3f8e0>,
 <passiogo.Route at 0x1d62db3fbb0>,
 <passiogo.Route at 0x1d62db3fa30>,
 <passiogo.Route at 0x1d62db3f5e0>,
 <passiogo.Route at 0x1d62db3f220>,
 <passiogo.Route at 0x1d62db3f1c0>,
 <passiogo.Route at 0x1d62db3fca0>]
```

### `TransportationSystem.getRouteById()`

Get all routes for the appropriate system.

**Input**:

- **routeId** (*str*): ID of the desired route
- **appVersion** (*int*): Version of the application (Default: 1)
- **amount** (*int*): Unknown (Default: 1)

**Output**: [`Route`](#route)

```python
passiogo.getSystemFromID(1068).getRouteById(133007)
```

```
<passiogo.Route at 0x1c26a30a1c0>
```


### `TransportationSystem.getStops()`

Gets all stops for the given transportation system.

**Inputs**:

- **appVersion** (*int*): Version of the application (Default: 2)
- **sA** (*int*): Unknown (Default: 1)

**Output**: *List* of [`Stop`](#stop)

```python
passiogo.getSystemFromID(1068).getStops()
```

```
[<passiogo.Stop at 0x1d62c89a670>,
 <passiogo.Stop at 0x1d62d2adc10>,
 <passiogo.Stop at 0x1d62d57bac0>,
 <passiogo.Stop at 0x1d62d57b5b0>,
 <passiogo.Stop at 0x1d62d57b520>,
 <passiogo.Stop at 0x1d62d57b3d0>,
 <passiogo.Stop at 0x1d62d57ba60>,
 <passiogo.Stop at 0x1d62d57bd90>,
 <passiogo.Stop at 0x1d62d57bee0>,
 ...
 <passiogo.Stop at 0x1d62da5a700>]
```

### `TransportationSystem.getSystemAlerts()`

Gets all alerts for the corresponding transportation system.

**Inputs**:

- **appVersion** (*int*): Version of the application (Default: 1)
- **amount** (*int*): Unknown (Default: 1)
- **routesAmount** (*int*): Unknown (Default: 1)

**Output**: *List* of [`SystemAlert`](#systemalert)

```python
passiogo.getSystemFromID(1068).getSystemAlerts()
```

```
[<passiogo.SystemAlert at 0x1d62dbe0130>,
 <passiogo.SystemAlert at 0x1d62dbe0190>,
 <passiogo.SystemAlert at 0x1d62dbe0370>,
 <passiogo.SystemAlert at 0x1d62dbe0490>]
```


### `TransportationSystem.getVehicles()`

Gets all alerts for the corresponding transportation system.

**Inputs**:

- **appVersion** (*int*): Version of the application (Default: 1)


**Output**: *List* of [`Vehicle`](#vehicle)

```python
passiogo.getSystemFromID(1068).getVehicles()
```

```
[<passiogo.Vehicle at 0x21b59af8d00>,
 <passiogo.Vehicle at 0x21b59af8f70>,
 <passiogo.Vehicle at 0x21b59af8d90>,
 <passiogo.Vehicle at 0x21b59af8370>,
 ...
 <passiogo.Vehicle at 0x21b597bfd90>,
 <passiogo.Vehicle at 0x21b597bfbe0>,
 <passiogo.Vehicle at 0x21b597bff10>]
```

## `Route`

### `Route.__init__()`

**id** is the only required parameter, all other default to *None*.

- **id** (*int*): ID of the route
- **groupId** (*int*): Unknown
- **groupColor** (*str*): Unknown
- **name** (*str*): Name of the route
- **shortName** (*str*): Short name / abbreviation of the route
- **nameOrig** (*str*): Unknown
- **fullname** (*str*): Unknown
- **myid** (*int*): Unknown
- **mapApp** (*bool*): Unknown
- **archive** (*bool*): Unknown
- **goPrefixRouteName** (*bool*): Unknown
- **goShowSchedule** (*bool*): Unknown
- **outdated** (*bool*): Unknown
- **distance** (*int*): Unknown
- **latitude** (*float*): Unknown
- **longitude** (*float*): Unknown
- **timezone** (*str*): Timezone of the route
- **serviceTime** (*str*): Route Schedule
- **serviceTimeShort** (*str*): Route Schedule
- **systemId** (*int*): ID of the transportation system
- **system** (*[`TransportationSystem`](#transportationsystem)*): transportation system object

```json
{'id': '133007',
 'groupId': '5702',
 'groupColor': '#0000ff',
 'name': 'Apostolic',
 'shortName': 'AP',
 'nameOrig': 'Apostolic',
 'fullname': 'University of Chicago',
 'myid': '38729',
 'mapApp': '1',
 'archive': '0',
 'goPrefixRouteName': '1',
 'goShowSchedule': 1,
 'outdated': '1',
 'distance': 578,
 'latitude': '41.780867018',
 'longitude': '-87.592902254',
 'serviceTime': 'is not provided: no bus on the route',
 'serviceTimeShort': 'No bus in service',
 'systemId': 1068,
 'system': <passiogo.TransportationSystem at 0x1d62db57c10>}
```

### `Route.getStops()`

Gets the list of stops for this route and stores it as an argument

**Output**: *List* of [`Stop`](#stop)

```python
passiogo.getSystemFromID(1068).getRoutes()[0].getStops()
```

```
[<passiogo.Stop at 0x24a762ad250>,
 <passiogo.Stop at 0x24a762ada60>,
 <passiogo.Stop at 0x24a762ad850>,
 <passiogo.Stop at 0x24a762ad0d0>,
 <passiogo.Stop at 0x24a762ad2b0>,
 <passiogo.Stop at 0x24a75deabe0>,
 <passiogo.Stop at 0x24a75deae80>,
 <passiogo.Stop at 0x24a75dea790>,
 <passiogo.Stop at 0x24a75dead60>]
```

## `Stop`

### `Stop.__init__()`

**id** is the only required parameter, all other default to *None*.

- **id** (*str*): ID of the stop
- **routeId** (*str*): ID of the route
- **systemId** (*int*): ID of the transportation system
- **position** (*int*): Unknown
- **name** (*str*): Name of the stop
- **latitude** (*float*): Latitude of the stop
- **longitude** (*float*): Longitude of the stop
- **radius** (*int*): Unknown
- **routeName** (*str*): Name of the route
- **routeShortname** (*str*): Short Name / Abbreviation of the route
- **routeGroupId** (*int*): Unknown
- **system** (*[`TransportationSystem`](#transportationsystem)*): Transportation system object
- **route** (*[`Route`](#route)*): Route object

```json
{'id': '8611',
 'routesAndPositions': {'38728': [0, 7], '38730': [7]},
 'systemId': 1068,
 'name': 'Drexel Garage',
 'latitude': 41.784433,
 'longitude': -87.604445,
 'radius': 75,
 'system': <passiogo.TransportationSystem at 0x24a7681b670>}
```


## `SystemAlert`

### `SystemAlert.__init__()`

**id** is the only required parameter, all other default to *None*.

- **id** (*int*): ID of the alert
- **systemId** (*int*): ID of the system
- **system** (*[`TransportationSystem`](#transportationsystem)*): Transportation System object
- **routeId** (*int*): Route ID this alert relates to
- **name** (*str*): Name/Title of the alert
- **html** (*str*): Content of the alert in HTML format
- **archive** (*bool*): Unknown
- **important** (*bool*): Unknown
- **dateTimeCreated** (*str*): Date and time when the alert was created
- **dateTimeFrom** (*str*): Start date and time from which the alert is in effect
- **dateTimeTo** (*str*): End date and time from which the alert is in effect
- **asPush** (*bool*): Unknown
- **gtfs** (*bool*): Unknown
- **gtfsAlertCauseId** (*bool*): Unknown
- **gtfsAlertEffectId** (*bool*): Unknown
- **gtfsAlertUrl** (*str*): Unknown
- **gtfsAlertHeaderText** (*str*): Name/Title of the alert in text format
- **gtfsAlertDescriptionText** (*str*): Content of the alert in text format
- **routeGroupId** (*int*): Unknown
- **createdUtc** (*str*): Date and time when the alert was created in UTC
- **authorId** (*int*): User ID of the author
- **author** (*str*): Name and email of the author
- **updated** (*str*): Date and time when the alert was updated
- **updateAuthorId** (*int*): User ID of the author of the update
- **updateAuthor** (*str*): Name and email of the author of the update
- **createdF** (*str*): Human friendly date and time when the alert was created
- **fromF** (*str*): Human friendly start date and time of the alert
- **fromOk** (*bool*): Unknown
- **toOk** (*bool*): Unknown

```json
{'id': '27926',
 'systemId': '1068',
 'system': <passiogo.TransportationSystem at 0x1d62ddcc760>,
 'routeId': '38731',
 'name': 'Midway Metra Reroute',
 'html': 'Due to road reconstruction at 60th & Stony Island, Midway Metra will detour to Dorchester Ave., bypassing the parking lot at Stony Island. The new stop for the parking lot is on the Midway EB, across from the Stony Island Parking Lot.',
 'archive': '0',
 'important': '1',
 'dateTimeCreated': '2024-04-18 10:17:44',
 'dateTimeFrom': '2024-07-12 06:10:34',
 'dateTimeTo': '2024-07-30 22:15:34',
 'asPush': '1',
 'gtfs': '1',
 'gtfsAlertCauseId': None,
 'gtfsAlertEffectId': None,
 'gtfsAlertUrl': None,
 'gtfsAlertHeaderText': 'Midway Metra Reroute',
 'gtfsAlertDescriptionText': 'Due to road reconstruction at 60th Stony Island, Midway Metra will detour to Dorchester Ave., bypassing the parking lot at Stony Island. The new stop for the parking lot is on the Midway EB, across from the Stony Island Parking Lot.',
 'routeGroupId': None,
 'createdUtc': '2024-04-18 15:17:44',
 'authorId': '1217',
 'author': 'John Appleseed (sample@email.com)',
 'updated': '2024-07-12 06:09:22',
 'updateAuthorId': '1202',
 'updateAuthor': 'John Appleseed (sample@email.com)',
 'createdF': 'Friday, July 12th, 2024 6:10 AM',
 'fromF': 'Friday, July 12th, 2024 6:10 AM',
 'fromOk': '1',
 'toOk': '1'}
```

## `Vehicle`

### `Vehicle.__init__()`

All attributes default to **None**.

- **id** (*str*): ID of the vehicle
- **name** (*str*): Name of the vehicle
- **type** (*str*): Type of the vehicle
- **system** (*[`TransportationSystem`](#transportationsystem)*): Type of the vehicle
- **calculatedCourse** (*int*): Unknown
- **routeId** (*str*): ID of the route the vehicle is part of
- **routeName** (*str*): Name of the route the vehicle is part of
- **color** (*str*): Color in which the vehicle/route is displayed
- **created** (*str*): When the vehicle was created
- **latitude** (*float*): Current latitude of the vehicle
- **longitude** (*float*): Current longitude of the vehicle
- **speed** (*float*): Current speed of the vehicle
- **paxLoad** (*float*): Current number of passengers on board
- **outOfService** (*bool*): Whether the vehicle is currently in service
- **more** (*str*): Unknown
- **tripId** (*str*): Unknown


```python
{'id': '7998',
 'name': '7998 (CTA)',
 'type': 'bus',
 'system': <passiogo.TransportationSystem at 0x21b59b13460>,
 'calculatedCourse': '0',
 'routeId': 'cta4',
 'routeName': 'Cottage Grove (CTA) (CTA)',
 'color': '#565a5c',
 'created': '20240818 11:13',
 'longitude': 41.6861457824707,
 'speed': None,
 'paxLoad': 0,
 'outOfService': None,
 'more': None,
 'tripId': None}
```

## `printAllSystemsMd()`

Prints all system names as a markdown list.

**Input**:

- **includeHtmlBreaks** (*bool*): Whether to include HTML line breaks (Default: True)

**Returns**: None

```python
passiogo.printAllSystemsMd()
```

```md
- 3630 Peachtree (#951)<br/>
- 5025 Apartments (#1634)<br/>
- 725 Ponce (#1832)<br/>
- Agnes Scott College (#1471)<br/>
...
```





