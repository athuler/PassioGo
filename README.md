# Passio Go API

[![PyPI - Version](https://img.shields.io/pypi/v/passiogo?label=Latest%20Version&link=https%3A%2F%2Fpypi.org%2Fproject%2FPassioGo%2F)](https://pypi.org/project/PassioGo/)
[![Pepy Total Downlods](https://img.shields.io/pepy/dt/PassioGo)](https://www.pepy.tech/projects/passiogo)
[![Documentation Status](https://readthedocs.org/projects/passiogo/badge/?version=latest)](https://passiogo.readthedocs.io/en/latest/?badge=latest)




An **unofficial** Python API for [Passio Go](https://passiogo.com/) allowing anyone to build transit-based applications for hundreds of Universities, Municipalities, Paratransit, and Airports. 


## Installation

The package is available to download using [pip](https://pypi.org/project/PassioGo/).

```
pip install passiogo
```

## Documentation

Project documentation for the latest stable version is available at [passiogo.readthedocs.io](https://passiogo.readthedocs.io/). Documentation for other versions is available at [passiogo.readthedocs.io/en/X.X.X](https://passiogo.readthedocs.io/en/0.1.2/).

The documentation is built using `mkdocs` and can be rebuilt using the following:

```
pip install -r docs/requirements.txt
mkdocs serve
```


## Usage

### Transportation System

Before doing anything, you will need a [`TransportationSystem`](api/#transportationsystem) object.

If you know the `id` of the desired transportation system, you can obtain the object using `passiogo.getSystemFromID(id)`.

```python
system = passiogo.getSystemFromID(1068)
```

If you do not know the ID of your desired transportation system, you can find it [here](#all-transportation-systems-accessible-by-the-api) or with the following:

```python
system = passiogo.printAllSystemsMd()
```

```md
- 3630 Peachtree (#951)<br/>
- 5025 Apartments (#1634)<br/>
- 725 Ponce (#1832)<br/>
- Agnes Scott College (#1471)<br/>
...
```

### Routes

You can obtain all the routes for a given transportation system using `TransportationSystem.getRoutes()`:

```python
routes = system.getRoutes()
```

Here, `routes` is a list of [`Route`](api/#route) objects. We can look at how much information is available for each route.

```python
routes[0].__dict__
```

```
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
 'outdated': '0',
 'distance': 578,
 'latitude': '41.780867018',
 'longitude': '-87.592902254',
 'serviceTime': None,
 'serviceTimeShort': None,
 'systemId': 1068,
 'system': <passiogo.TransportationSystem at 0x24a77026a00>}
```

### Stops

You can get all the stops within a given transportation system using `TransportationSystem.getStops()`:

```python
stops = system.getStops()
```

Here, `stops` is a list of [`Stop`](api/#stop) objects. We can look at how much information is available for each route.

```python
stops[0].__dict__
```

```
{'id': '10103',
 'routesAndPositions': {'4009': [0]},
 'systemId': 1068,
 'name': 'Medical Stop',
 'latitude': 41.79668374,
 'longitude': -87.595753286,
 'radius': 36,
 'system': <passiogo.TransportationSystem at 0x24a77026850>}
```

If you only wish to get stops for a given route, you can use the `Route.getStops()` method.

```python
stops = routes[0].getStops()
```

### System Alerts

You can get all system alerts within a given transportation system with the `TransportationSystem.getSystemAlerts()`.

```python
alerts = system.getSystemAlerts()
```

Here, `alerts` is a list of [`SystemAlert`](api/#systemalert). We can look at how much information is available for each alert.

```python
alerts[0].__dict__
```

```
{'id': '27535',
 'systemId': '1068',
 'system': <passiogo.TransportationSystem at 0x24a764e7a90>,
 'routeId': None,
 'name': 'Nightride Assistance Contact',
 'html': 'During the hours of 4 p.m. until 4 a.m., if you do not see arrival times or buses on route in the app, or experience any unusual event, please contact <b>773-573-7201</b> for assistance.',
 'archive': '0',
 'important': '1',
 'dateTimeCreated': '2024-04-09 09:43:10',
 'dateTimeFrom': '2024-04-09 15:40:44',
 'dateTimeTo': '2025-04-16 09:40:44',
 'asPush': '1',
 'gtfs': '1',
 'gtfsAlertCauseId': None,
 'gtfsAlertEffectId': None,
 'gtfsAlertUrl': None,
 'gtfsAlertHeaderText': 'Nightride Assistance Contact',
 'gtfsAlertDescriptionText': 'During the hours of 4 p.m. until 4 a.m., if you do not see arrival times or buses on route in the app, or experience any unusual event, please contact 773-573-7201 for assistance.',
 'routeGroupId': None,
 'createdUtc': '2024-04-09 14:43:10',
 'authorId': '1202',
 'author': 'John Appleseed (abc@domain.com)',
 'updated': '2024-07-17 16:12:02',
 'updateAuthorId': '1217',
 'updateAuthor': 'Mark Appleseed (def@domain.com)',
 'createdF': 'Tuesday, April 9th, 2024 3:40 PM',
 'fromF': 'Tuesday, April 9th, 2024 3:40 PM',
 'fromOk': '1',
 'toOk': '1'}
```

## Changelog

This project's changelog is available at [`CHANGELOG.md`](https://github.com/athuler/PassioGo/blob/main/CHANGELOG.md)


## Bug Reporting / Feedback

Found a bug? Have an idea for a new feature? Please [send it in as a GitHub issue](https://github.com/athuler/PassioGo/issues)!


## Contributing

Interested in contributing to this package? Check out [open issues](https://github.com/athuler/PassioGo/issues).

When ready, [fork the repository](https://github.com/athuler/PassioGo/fork), make your edits, then open a pull request on the active development branch.


## All Transportation Systems Accessible By The API

Collapsed below are all the transportation systems publicly available through this API.

<details>
<summary>Expand to Show All Systems</summary>

<br/>

<i>Last Updated: 2025/11/10</i><br/><br/>

- 5025 Apartments (#1634)<br/>
- 725 Ponce (Reef Parking) (#1832)<br/>
- AUC (#67)<br/>
- Agnes Scott College (#1471)<br/>
- Alabama A&M University (#2456)<br/>
- Albany State University  (#5213)<br/>
- Anne Arundel County Office of Transportation (#3469)<br/>
- Athens Public Transit (#5842)<br/>
- Atlantic Station (#4349)<br/>
- Audible (#876)<br/>
- Augusta University (#553)<br/>
- BLT (Propark) (#4940)<br/>
- Bayonne Bay (#1808)<br/>
- Bayway Transit (#6736)<br/>
- Beacon College (#3389)<br/>
- Beacon Shuttle (#3561)<br/>
- Beloit Transit (#3655)<br/>
- Bis-Man Transit (#4121)<br/>
- Boise Airport (The Car Park) (#5366)<br/>
- Bowie State University (#3001)<br/>
- Brockton Area Transit Authority (BAT) (#2046)<br/>
- Brown University  (#1067)<br/>
- Bull Runner at USF (#2343)<br/>
- CHOA (#3489)<br/>
- CSULB (#4163)<br/>
- Calabasas Transit (LAZ Parking) (#5211)<br/>
- Canby Area Transit (#3274)<br/>
- Cascades East Transit (#2460)<br/>
- Casper Area Transit (#4055)<br/>
- Cecil Transit (#6135)<br/>
- Century Village (TD) (#444)<br/>
- Chapman University (#263)<br/>
- Charles River TMA (#5019)<br/>
- Charleston Airport REEF (#4749)<br/>
- Charm City Circulator (#3554)<br/>
- Chemung County (C-Tran) (#4009)<br/>
- Chestnut Ridge (#5659)<br/>
- Citrus Connection (#1752)<br/>
- City of Arcadia (#3304)<br/>
- City of Bangor (#4631)<br/>
- City of Billings MET Transit (#3901)<br/>
- City of Cerritos (#2282)<br/>
- City of Clovis (#3743)<br/>
- City of Galesburg (#6268)<br/>
- City of Hoboken (#466)<br/>
- City of Irvine (#4502)<br/>
- City of Jackson (JTRAN) (#3363)<br/>
- City of Jacksonville (#3521)<br/>
- City of Janesville (#5599)<br/>
- City of Monterey Park (#3215)<br/>
- City of Newport Beach (Balboa Peninsula Trolley) (#4883)<br/>
- City of North Augusta (#6850)<br/>
- City of Olean (#2084)<br/>
- City of Passaic UEZ Shuttle (Propark) (#5730)<br/>
- City of Rosemead (#3670)<br/>
- City of Sandy (#3183)<br/>
- City of Watertown (CitiBus) (#2775)<br/>
- citylink | LATC (#5863)<br/>
- Citylink Edmond (#4662)<br/>
- Citylink North (Kootenai County) (#2016)<br/>
- Citylink South (#2059)<br/>
- Clackamas County (#3205)<br/>
- Clemson Tiger Transit (#1654)<br/>
- Clemson University (#793)<br/>
- Cleveland Urban Area Transit System (CUATS) (#4836)<br/>
- Colby College (#3377)<br/>
- Concho Valley Transit (#3281)<br/>
- Concord Kannapolis Area Transit (#4124)<br/>
- Concourse (#1841)<br/>
- Connect Douglas (#1661)<br/>
- Connecticut Children's Medical Center (Propark) (#5387)<br/>
- Cooperative Alliance for Seacoast Transportation (COAST) (#2962)<br/>
- Coos County Area Transit (#4835)<br/>
- County Connector (#2933)<br/>
- Dana Point Summer Trolley (#6059)<br/>
- Denver International Airport (#5397)<br/>
- Disney Programs (#2208)<br/>
- Drury Plaza Hotel - Disney Springs (#4748)<br/>
- ES Atlanta (#2280)<br/>
- ETHRA (#4583)<br/>
- EWR Employee Shuttle (#2989)<br/>
- EWR Port Authority NYNJ (#2496)<br/>
- Eastern Kentucky University (#3828)<br/>
- Eastern Panhandle Transit Authority (EPTA) (#1298)<br/>
- Elon University (#3045)<br/>
- Emory University (#4432)<br/>
- Endicott College (#2873)<br/>
- Escambia County Area Transit (ECAT) (#2283)<br/>
- Fitchburg State University (#1000000002)<br/>
- Florham Park (Sun Valley/River Bend) (#2311)<br/>
- Florida Gulf Coast University (FGCU) (#2281)<br/>
- Florida International University (#4119)<br/>
- Fort Valley State University (#6065)<br/>
- Four Points Sheraton (Propark) (#5208)<br/>
- Franklin Regional Transit Authority (#2771)<br/>
- Franklin Transit (#1652)<br/>
- Free Downtown Connection NY (#7073)<br/>
- Fresh Direct (Pro Park) (#4691)<br/>
- George Washington University (GW) (#4120)<br/>
- Georgia College & State University (GCSU) (#895)<br/>
- Georgia Southern University (#137)<br/>
- Georgia State University (#480)<br/>
- Greenville (#1000000001)<br/>
- HARTransit (#2250)<br/>
- Harbortown (Atlantic Realty) (#4686)<br/>
- Harford County (#4620)<br/>
- Harris County Transit (#3497)<br/>
- Harrisonburg Transit (#2868)<br/>
- Harvard University (#831)<br/>
- Hendry County Transit System (#2217)<br/>
- Highland Hospital Metropolis (#3829)<br/>
- Hill Place Apartments (#1092)<br/>
- Hollins University (#3014)<br/>
- Hotel Indigo Flushing (#5525)<br/>
- Houston Airport (SP+) (#4919)<br/>
- Hutch Metro Center (#1569)<br/>
- Interurban Trolley (#3639)<br/>
- Island Transit (#5245)<br/>
- JAX Mass Transit (#5153)<br/>
- JFK LGA Shuttles (#2494)<br/>
- JPS Health Network (#5158)<br/>
- JTA (#6089)<br/>
- Jasper Transit Local and Regional (#4294)<br/>
- Kennesaw State University (#66)<br/>
- Kentucky River Foothills (#3630)<br/>
- Key West Transit (#4440)<br/>
- LIJ Valley Stream (#7086)<br/>
- LaGuardia Plaza Hotel (#5526)<br/>
- Laguna Niguel Summer Trolley (#6058)<br/>
- Lawrence Transit (#4834)<br/>
- Lehigh University (#1090)<br/>
- Lewiston Transit & Asotin County Transit (#4939)<br/>
- Long Island University (#5082)<br/>
- MIT (#94)<br/>
- Marymount University (#4716)<br/>
- Mass General Brigham (#6313)<br/>
- Mayaguez (Skytec) (#3206)<br/>
- McAfee Knob Trailhead (Ridesource) (#3069)<br/>
- Mercy University (#694)<br/>
- Metropolis Parking (Anschutz Campus) (#3282)<br/>
- Missouri State University (#459)<br/>
- Montachusett Regional Transit Authority (MART) (#2173)<br/>
- Montana State University (#5210)<br/>
- Municipio de Utuado (#6307)<br/>
- NC Central University (#6919)<br/>
- NC State University (#3827)<br/>
- NYU Langone Long Island Security (#5455)<br/>
- National Cancer Institute (#3293)<br/>
- Naval Base San Diego (#5477)<br/>
- New River Transit Authority (#3362)<br/>
- New York University (#1007)<br/>
- North Carolina A&T State University (#261)<br/>
- North Fork Area Transit (#2587)<br/>
- Oak Ridge National Laboratory (#6357)<br/>
- Orlando International Airport (#4692)<br/>
- Otter Bus (Ridesource) (#3015)<br/>
- Ozark Regional Transit (#1589)<br/>
- Pensacola Airport Parking Shuttle (#3520)<br/>
- Pepperdine University (#3593)<br/>
- Perimeter Summit Shuttle (#5214)<br/>
- Pittsburgh International Airport (PIT)(LAZ) (#3200)<br/>
- Port of Galveston (#3294)<br/>
- Portage Area Regional Transit Authority (PARTA) (#3420)<br/>
- Providence College (#4147)<br/>
- Quinnipiac University (#3899)<br/>
- Radford Transit (#1248)<br/>
- Ravinia Shuttle (#5231)<br/>
- Rivendell Properties (#5409)<br/>
- River Valley Transit (#1726)<br/>
- Roadrunner Transit (#4010)<br/>
- Rochester Institute of Technology (RIT) (#4006)<br/>
- Roger Williams University (#1850)<br/>
- Rural Transit / Beyond the Borders / ATS (#4820)<br/>
- Rutgers University (#1268)<br/>
- SAT Parking (#5479)<br/>
- SCAD Atlanta (#5306)<br/>
- SCAD Savannah (#5305)<br/>
- SMART Transit (#4476)<br/>
- SMU (#5155)<br/>
- SPOT Bus (Selkirks - Pend Oreille Transit) (#5698)<br/>
- Sacramento Airport Park & Ride (#898)<br/>
- Saint Peter's University (#493)<br/>
- Sales Demo - SR (#5047)<br/>
- Salve Regina University (#894)<br/>
- San Clemente Trolley (#6061)<br/>
- San Juan Capistrano Summer Trolley (#6060)<br/>
- Santa Fe Trails (#5880)<br/>
- Seneca Transit System (#2035)<br/>
- Sioux City Transit (#4832)<br/>
- Somerset County Transportation (#5160)<br/>
- South Clackamas Transportation District (#4233)<br/>
- Southeastern Louisiana University (#186)<br/>
- Southern Connecticut State University (#431)<br/>
- St. Lawrence County Public Transit (#4234)<br/>
- St. Vincent's (Pinnacle Transportation Group) (#2561)<br/>
- State Shuttle (First Mile Capital) (#2780)<br/>
- Stevens Point - Central Transportation (#2556)<br/>
- Summit East (#5795)<br/>
- Tennessee Technological University (#1736)<br/>
- Terraces (Pinnacle Transportation Group) (#3270)<br/>
- Texas Medical Center (#5595)<br/>
- Texas State University  (#5078)<br/>
- The Concord Trolley (#3089)<br/>
- The Cottages at Lake Tamaha Tuscaloosa (#1093)<br/>
- The Galleria (Reef Parking) (#1900)<br/>
- The Hartford (#4581)<br/>
- The Woodlands Express  (#6282)<br/>
- The Woodlands Town Center Trolley (#5962)<br/>
- TheBus Hernando County (#5732)<br/>
- Thomas Jefferson University (#6436)<br/>
- Township of West Orange (#3166)<br/>
- Towson Loop (Baltimore County) (#2153)<br/>
- Transit Services of Frederick County (#4821)<br/>
- Transpo (#3490)<br/>
- Tufts University (#6670)<br/>
- Tulane University (#353)<br/>
- Tuscaloosa Transit Authority (#3817)<br/>
- UARK (University of Arkansas) (#3778)<br/>
- UB Shuttle (#5230)<br/>
- UB Stampede (#4882)<br/>
- UCONN/WRTD (#1541)<br/>
- UNC Charlotte (#1053)<br/>
- UNC Greensboro (#2874)<br/>
- UNC Wilmington (#3952)<br/>
- UTHealth Houston (#6717)<br/>
- University of Alabama (#240)<br/>
- University of Chicago (#1068)<br/>
- University of Florida (#3826)<br/>
- University of Georgia (UGA) (#3994)<br/>
- University of Hartford (#3305)<br/>
- University of Miami Hurry ’Canes Shuttle (#5657)<br/>
- University of Miami Medical Center (Lanier Parking)) (#4201)<br/>
- University of Montana (ASUM) (#4041)<br/>
- University of New Haven (#3900)<br/>
- University of New Mexico (UNM) (#2156)<br/>
- University of North Georgia (#646)<br/>
- University of Rochester (#3214)<br/>
- University of San Diego Tram Services (#3444)<br/>
- University of Texas at El Paso (UTEP) (#2383)<br/>
- University of Wisconsin-Milwaukee (GO Riteway) (#728)<br/>
- Upper Cumberland Human Resource Agency (UCHRA) (#2875)<br/>
- Utah State University (#3499)<br/>
- Valdosta State University  (#6090)<br/>
- Vanderbilt University (#3622)<br/>
- Vanderbilt University Medical Center (#1332)<br/>
- Via Mobility Services (#4729)<br/>
- Vincennes Trolley (#5365)<br/>
- WRTA (#6684)<br/>
- Wake Forest University (#3669)<br/>
- Washington County Transit (WCT) (#5594)<br/>
- WaterColor Community Association (#4842)<br/>
- West Midtown Shuttle (#4473)<br/>
- WestMar (#1091)<br/>
- Western Carolina University (#2597)<br/>
- Wilmington International Airport (#5596)<br/>
- Winston - Salem University (#6848)<br/>
- Woodbridge Village/Gardens/Colonial (#1642)<br/>
- XChange at Secaucus Junction (#432)<br/>
- Yellowknife (#4825)<br/>
- Yuba-Sutter Transit Authority (#6871)<br/>

</details>
<br/>
