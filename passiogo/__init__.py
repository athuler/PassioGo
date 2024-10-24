import json
import requests
import websocket

BASE_URL = "https://passiogo.com"


### Helper Functions ###

def toIntInclNone(toInt):
	if toInt == None:
		return toInt
	return(int(toInt))

	
def sendApiRequest(url, body):
	
	# Send Request
	response = requests.post(url, json = body)
	
	try:
		# Handle JSON Response
		response = response.json()
	except Exception as e:
		raise Exception(f"Error converting API response to JSON! Here is the response received: {response}")
		return None
	
	
	# Handle API Error
	if(
		"error" in response and 
		response["error"] != ""
	):
		raise Exception(f"Error in Response! Here is the received response: {response}")
	
	return(response)



### Transportation Systems ###


class TransportationSystem:
	
	def __init__(
		self,
		id: int,
		name: str = None,
		username: str = None,
		goAgencyName: str = None,
		email: str = None,
		goTestMode: bool = None,
		name2: bool = None,
		homepage: str = None,
		logo: bool = None,
		goRoutePlannerEnabled: bool = None,
		goColor: str = None,
		goSupportEmail: str = None,
		goSharedCode: int = None,
		goAuthenticationType: bool = None
	):
		
		self.id = id
		self.name = name
		self.username = username
		self.goAgencyName = goAgencyName
		self.email = email
		self.goTestMode = goTestMode
		self.name2 = name2
		self.homepage = homepage
		self.logo = logo
		self.goRoutePlannerEnabled = goRoutePlannerEnabled
		self.goColor = goColor
		self.goSupportEmail = goSupportEmail
		self.goSharedCode = goSharedCode
		self.goAuthenticationType = goAuthenticationType
		
		self.checkTypes()
	
	def checkTypes(self):
		# id : int
		assert type(self.id) == int, f"'id' parameter must be an int not {type(self.id)}"
		
		# name : str or None
		assert (type(self.name) == str or self.name is None), f"'name' parameter must be a str not {type(self.name)}"
		
		# username : str or None
		assert (type(self.username) == str or self.username is None), f"'username' parameter must be a str not {type(self.username)}"
		
		# goAgencyName : str or None
		assert (type(self.goAgencyName) == str or self.goAgencyName is None), f"'goAgencyName' parameter must be a str not {type(self.goAgencyName)}"
		
		# email : str or None
		assert (type(self.email) == str or self.email is None), f"'email' parameter must be a str not {type(self.email)}"
		
		# goTestMode : bool or None
		assert (type(self.goTestMode) == bool or self.goTestMode is None), f"'goTestMode' parameter must be a bool not {type(self.goTestMode)}"
		
		# name2 : bool or None
		assert (type(self.name2) == bool or self.name2 is None), f"'name2' parameter must be a bool not {type(self.name2)}"
		
		# homepage : str or None
		assert (type(self.homepage) == str or self.homepage is None), f"'homepage' parameter must be a str not {type(self.homepage)}"
		
		# logo : bool or None
		assert (type(self.logo) == bool or self.logo is None), f"'logo' parameter must be a bool not {type(self.logo)}"
		
		# goRoutePlannerEnabled : bool or None
		assert (type(self.goRoutePlannerEnabled) == bool or self.goRoutePlannerEnabled is None), f"'goRoutePlannerEnabled' parameter must be a bool not {type(self.goRoutePlannerEnabled)}"
		
		# goColor : str or None
		assert (type(self.goColor) == str or self.goColor is None), f"'goColor' parameter must be a str not {type(self.goColor)}"
		
		# goSupportEmail : str or None
		assert (type(self.goSupportEmail) == str or self.goSupportEmail is None), f"'goSupportEmail' parameter must be a str not {type(self.goSupportEmail)}"
		
		# goSharedCode : int or None
		assert (type(self.goSharedCode) == int or self.goSharedCode is None), f"'goSharedCode' parameter must be a int not {type(self.goSharedCode)}"
		
		# goAuthenticationType : bool or None
		assert (type(self.goAuthenticationType) == bool or self.goAuthenticationType is None), f"'goAuthenticationType' parameter must be a bool not {type(self.goAuthenticationType)}"
	
	def getRoutes(
		self,
		appVersion = 1,
		amount = 1
	) -> list["Route"]:
		"""
		Obtains every route for the selected system.
		=========
		systemSelected: system from which to get content
		paramDigit: does not affect content of response, only formatting
		amount:
			1: Returns all routes for given system
			0: Not Valid, Gives Error
			>=2: Returns all routes for given system in addition to unrelated routes. Exact methodology unsure.
		"""
		
		
		# Initialize & Send Request
		url = BASE_URL+f"/mapGetData.php?getRoutes={appVersion}"
		body = {
				"systemSelected0" : str(self.id),
				"amount" : amount
				}
		routes = sendApiRequest(url, body)
		
		# Handle Request Error
		if(routes == None):
			return(None)
		
		
		# Handle Differing Response Format
		if "all" in routes:
			routes = routes["all"]
		
		allRoutes = []
		for route in routes:
			possibleKeys = ["id", "groupId", "groupColor", "name", "shortName", "nameOrig", "fullname", "myid", "mapApp", "archive", "goPrefixRouteName", "goShowSchedule", "outdated", "distance", "latitude", "longitude", "timezone", "serviceTime", "serviceTimeShort"]
			
			for possibleKey in possibleKeys:
				if possibleKey not in route.keys():
					route[possibleKey] = None
			
			allRoutes.append(Route(
				id = route["id"],
				groupId = route["groupId"],
				groupColor = route["groupColor"],
				name = route["name"],
				shortName = route["shortName"],
				nameOrig = route["nameOrig"],
				fullname = route["fullname"],
				myid = route["myid"],
				mapApp = route["mapApp"],
				archive = route["archive"],
				goPrefixRouteName = route["goPrefixRouteName"],
				goShowSchedule = route["goShowSchedule"],
				outdated = route["outdated"],
				distance = route["distance"],
				latitude = route["latitude"],
				longitude = route["longitude"],
				timezone = route["timezone"],
				serviceTime = route["serviceTime"],
				serviceTimeShort = route["serviceTimeShort"],
				systemId = int(route["userId"]),
				system = self
			))
		
		return(allRoutes)
	
	def getStops(
		self,
		appVersion = 2,
		sA = 1,
		raw = False
	) -> list["Stop"]:
		"""
		Obtains all stop for the given system.
		=========
		appVersion: No discernible change
		sA:
			0: error
			1: Returns all stops for the given system
			>=2: Returns unrelated stops as well
		"""
		
		
		# Initialize & Send Request
		url = BASE_URL+"/mapGetData.php?getStops="+str(appVersion)
		body = {
			"s0" : str(self.id),
			"sA" : sA
		}
		stops = sendApiRequest(url, body)
		
		# Return Raw Response
		if raw:
			return(stops)
		
		# Handle Request Error
		if(stops == None):
			return(None)
		
		# Handle Empty Routes
		if stops["routes"] == []:
			stops["routes"] = {}
		
		# Handle Empty Stops
		if stops["stops"] == []:
			stops["stops"] = {}
		
		
		# Create Route & Stops Dictionary
		# {routeid -> [stopid, stopid]}
		routesAndStops = {}
		for routeId, route in stops["routes"].items():
			routesAndStops[routeId] = []
			for stop in route[2:]:
				if stop == 0:
					continue
				routesAndStops[routeId].append(stop[1])
		
		
		# Create Each Stop Object
		allStops = []
		for id, stop in stops["stops"].items():
			
			# Create Route & Positions Dictionary
			# {routeid -> [position]}
			routesAndPositions = {}
			for routeId in routesAndStops.keys():
				if stop["id"] not in routesAndStops[routeId]:
					continue
				routesAndPositions[routeId] = [i for i,x in enumerate(routesAndStops[routeId]) if x == stop["id"]]
			
			
			keys = ["userId", "radius"]
			for key in keys:
				if key not in stop:
					stop[key] = None
			
			allStops.append(Stop(
				id = stop["id"],
				routesAndPositions = routesAndPositions,
				systemId = None if stop["userId"] is None else int(stop["userId"]),
				name = stop["name"],
				latitude = stop["latitude"],
				longitude = stop["longitude"],
				radius = stop["radius"],
				system = self,
			))
		
		return(allStops)
	
	def getSystemAlerts(
		self,
		appVersion = 1,
		amount = 1,
		routesAmount = 0
	) -> list["SystemAlert"]:
		"""
		Gets all system alerts for the selected system.
		=========
		systemSelected: system from which to get content
		appVersion:
			0: Error
			>=1: Valid
		"""
		
		
		# Initialize & Send Request
		url = BASE_URL+f"/goServices.php?getAlertMessages={appVersion}"
		body = {
			"systemSelected0" : str(self.id),
			"amount" : amount,
			"routesAmount":routesAmount
		}
		errorMsgs = sendApiRequest(url, body)
		
		# Handle Request Error
		if(errorMsgs == None):
			return(None)
		
		# Create SystemAlert Objects
		allAlerts = []
		for errorMsg in errorMsgs["msgs"]:
			allAlerts.append(SystemAlert(
				id = errorMsg["id"],
				systemId = errorMsg["userId"],
				system = self,
				routeId = errorMsg["routeId"],
				name = errorMsg["name"],
				html = errorMsg["html"],
				archive = errorMsg["archive"],
				important = errorMsg["important"],
				dateTimeCreated = errorMsg["created"],
				dateTimeFrom = errorMsg["from"],
				dateTimeTo = errorMsg["to"],
				asPush = errorMsg["asPush"],
				gtfs = errorMsg["gtfs"],
				gtfsAlertCauseId = errorMsg["gtfsAlertCauseId"],
				gtfsAlertEffectId = errorMsg["gtfsAlertEffectId"],
				gtfsAlertUrl = errorMsg["gtfsAlertUrl"],
				gtfsAlertHeaderText = errorMsg["gtfsAlertHeaderText"],
				gtfsAlertDescriptionText = errorMsg["gtfsAlertDescriptionText"],
				routeGroupId = errorMsg["routeGroupId"],
				createdUtc = errorMsg["createdUtc"],
				authorId = errorMsg["authorId"],
				author = errorMsg["author"],
				updated = errorMsg["updated"],
				updateAuthorId = errorMsg["updateAuthorId"],
				updateAuthor = errorMsg["updateAuthor"],
				createdF = errorMsg["createdF"],
				fromF = errorMsg["fromF"],
				fromOk = errorMsg["fromOk"],
				toOk = errorMsg["toOk"],
			))
		
		return(allAlerts)

	def getVehicles(
		self,
		appVersion = 2
	) -> list["Vehicle"]:
		"""
		Gets all currently running buses.
		=========
		s0: system from which to get content
		paramDigit:
			0: Error
			>=1: Valid
		"""
		
		
		# Initialize & Send Request
		url = BASE_URL+"/mapGetData.php?getBuses="+str(appVersion)
		body = {
			"s0" : str(self.id),
			"sA" : 1
		}
		vehicles = sendApiRequest(url, body)
		
		# Handle Request Error
		if(vehicles == None):
			return(None)
		
		allVehicles = []
		for vehicleId, vehicle in vehicles["buses"].items():
			if vehicleId == '-1':
				continue
			
			vehicle = vehicle[0]
			
			for key in ["busId", "busName", "busType", "calculatedCourse", "routeId", "route", "color", "created", "latitude", "longitude", "speed", "paxLoad100", "outOfService", "more", "tripId"]:
				if key not in vehicle:
					vehicle[key] = None
			
			
			allVehicles.append(Vehicle(
				id = vehicle["busId"],
				name = vehicle["busName"],
				type = vehicle["busType"],
				system = self,
				calculatedCourse = vehicle["calculatedCourse"],
				routeId = vehicle["routeId"],
				routeName = vehicle["route"],
				color = vehicle["color"],
				created = vehicle["created"],
				latitude = vehicle["latitude"],
				longitude = vehicle["longitude"],
				speed = vehicle["speed"],
				paxLoad = vehicle["paxLoad100"],
				outOfService = vehicle["outOfService"],
				more = vehicle["more"],
				tripId = vehicle["tripId"],
			))
		
		return(allVehicles)


def getSystems(
	appVersion = 2,
	sortMode = 1,
) -> list["TransportationSystem"]:
	'''
	Gets all systems. Returns a list of TransportationSystem.
	
	sortMode: Unknown
	appVersion:
		<2: Error
		2: Valid
	'''
	
	
	# Initialize & Send Request
	url = f"{BASE_URL}/mapGetData.php?getSystems={appVersion}&sortMode={sortMode}&credentials=1"
	systems = sendApiRequest(url, None)
	
	
	# Handle Request Error
	if(systems == None):
		return([])
	
	
	allSystems = []
	for system in systems["all"]:
		
		# Convert Empty Strings To None Objects
		for parameter in system.keys():
			if system[parameter] == '':
				system[parameter] = None
		
		# Check all keys exist
		for key in ["goAgencyName", "email", "email", "goTestMode", "name2", "homepage", "logo", "goRoutePlannerEnabled", "goColor", "goSupportEmail", "goSharedCode", "goAuthenticationType"]:
			if key not in system.keys():
				system[key] = None
		
		allSystems.append(TransportationSystem(
			id = int(system["id"]),
			name = system["fullname"],
			username = system["username"],
			goAgencyName = system["goAgencyName"],
			email = system["email"],
			goTestMode = bool(int(system["goTestMode"])),
			name2 = bool(int(system["name2"])),
			homepage = system["homepage"],
			logo = bool(int(system["logo"])),
			goRoutePlannerEnabled = bool(int(system["goRoutePlannerEnabled"])),
			goColor = system["goColor"],
			goSupportEmail = system["goSupportEmail"],
			goSharedCode = toIntInclNone(system["goSharedCode"]),
			goAuthenticationType = bool(int(system["goAuthenticationType"])),
		))
	
	
	return(allSystems)


def getSystemFromID(
	id,
	appVersion = 2,
	sortMode = 1,
) -> TransportationSystem:
	
	# Check Input Type
	assert type(id) == int, "`id` must be of type int"
	
	# Check App Version Type
	assert type(appVersion) == int, "`appVersion` must be of type int"
	
	# Check sort Mode Type
	assert type(sortMode) == int, "`sortMode` must be of type int"
	
	systems = getSystems(appVersion,sortMode)
	
	for system in systems:
		if system.id == id:
			return system
	return None


def printAllSystemsMd(
	includeHtmlBreaks = True
):
	systems = getSystems()
	
	for system in systems:
		print(f"- {system.name} (#{system.id}){'<br/>' if includeHtmlBreaks else ''}")


### Routes ###

class Route:
	
	def __init__(
		self,
		id: int,
		groupId: int = None,
		groupColor: str = None,
		name: str = None,
		shortName: str = None,
		nameOrig: str = None,
		fullname: str = None,
		myid: int = None,
		mapApp: bool = None,
		archive: bool = None,
		goPrefixRouteName: bool = None,
		goShowSchedule: bool = None,
		outdated: bool = None,
		distance: int = None,
		latitude: float = None,
		longitude: float = None,
		timezone: str = None,
		serviceTime: str = None,
		serviceTimeShort: str = None,
		systemId: id = None,
		system: TransportationSystem = None,
	):
		self.id = id
		self.groupId = groupId
		self.groupColor = groupColor
		self.name = name
		self.shortName = shortName
		self.nameOrig = nameOrig
		self.fullname = fullname
		self.myid = myid
		self.mapApp = mapApp
		self.archive = archive
		self.goPrefixRouteName = goPrefixRouteName
		self.goShowSchedule = goShowSchedule
		self.outdated = outdated
		self.distance = distance
		self.latitude = latitude
		self.longitude = longitude
		self.serviceTime = serviceTime
		self.serviceTimeShort = serviceTimeShort
		self.systemId = systemId
		self.system = system
	
	
	def getStops(self):
		"""
		Gets the list of stops for this route and stores it as an argument
		"""
		stopsForRoute = []
		allStops = self.system.getStops()
		
		for stop in allStops:
			if \
				self.myid in list(stop.routesAndPositions.keys()) or \
				self.id in list(stop.routesAndPositions.keys()) or \
				self.groupId in list(stop.routesAndPositions.keys()):
				stopsForRoute.append(stop)
		
		return(stopsForRoute)


### Stops ###

class Stop:
	
	def __init__(
		self,
		id: str,
		routesAndPositions: dict = None,
		systemId: int = None,
		name: str = None,
		latitude: float = None,
		longitude: float = None,
		radius: int = None,
		system : TransportationSystem = None,
	):
		if routesAndPositions is None:
			routesAndPositions = {}
		
		self.id = id
		self.routesAndPositions = routesAndPositions
		self.systemId = systemId
		self.name = name
		self.latitude = latitude
		self.longitude = longitude
		self.radius = radius
		self.system = system
	

### System Alerts ###

class SystemAlert:
	
	def __init__(
		self,
		id: int,
		systemId: int = None,
		system: TransportationSystem = None,
		routeId: int = None,
		name: str = None,
		html: str = None,
		archive: bool = None,
		important: bool = None,
		dateTimeCreated: str = None,
		dateTimeFrom: str = None,
		dateTimeTo: str = None,
		asPush: bool = None,
		gtfs: bool = None,
		gtfsAlertCauseId: id = None,
		gtfsAlertEffectId: id = None,
		gtfsAlertUrl: str = None,
		gtfsAlertHeaderText: str = None,
		gtfsAlertDescriptionText: str = None,
		routeGroupId: int = None,
		createdUtc: str = None,
		authorId: int = None,
		author: str = None,
		updated: str = None,
		updateAuthorId: int = None,
		updateAuthor: str = None,
		createdF: str = None,
		fromF: str = None,
		fromOk: bool = None,
		toOk: bool = None,
	):
		self.id = id
		self.systemId = systemId
		self.system = system
		self.routeId = routeId
		self.name = name
		self.html = html
		self.archive = archive
		self.important = important
		self.dateTimeCreated = dateTimeCreated
		self.dateTimeFrom = dateTimeFrom
		self.dateTimeTo = dateTimeTo
		self.asPush = asPush
		self.gtfs = gtfs
		self.gtfsAlertCauseId = gtfsAlertCauseId
		self.gtfsAlertEffectId = gtfsAlertEffectId
		self.gtfsAlertUrl = gtfsAlertUrl
		self.gtfsAlertHeaderText = gtfsAlertHeaderText
		self.gtfsAlertDescriptionText = gtfsAlertDescriptionText
		self.routeGroupId = routeGroupId
		self.createdUtc = createdUtc
		self.authorId = authorId
		self.author = author
		self.updated = updated
		self.updateAuthorId = updateAuthorId
		self.updateAuthor = updateAuthor
		self.createdF = createdF
		self.fromF = fromF
		self.fromOk = fromOk
		self.toOk = toOk



### Vehicles ###

class Vehicle:

	def __init__(
		self,
		id: str = None,
		name: str = None,
		type: str = None,
		system: TransportationSystem = None,
		calculatedCourse: int = None,
		routeId: str = None,
		routeName: str = None,
		color: str = None,
		created: str = None,
		latitude: float = None,
		longitude: float = None,
		speed: float = None,
		paxLoad: float = None,
		outOfService: bool = None,
		more: str = None,
		tripId: str = None,
	):
		self.id = id
		self.name = name
		self.type = type
		self.system = system
		self.calculatedCourse = calculatedCourse
		self.routeId = routeId
		self.routeName = routeName
		self.color = color
		self.created = created
		self.longitude = longitude
		self.latitude = latitude
		self.speed = speed
		self.paxLoad = paxLoad
		self.outOfService = outOfService
		self.more = more
		self.tripId = tripId




### Live Timings ###
## Not Yet Supported! ##

# Launch WebSocket
def launchWS():
	uri = "wss://passio3.com/"
	
	
	websocket.enableTrace(False) # For Debugging
	wsapp = websocket.WebSocketApp(
		uri,
		on_open = subscribeWS,
		#on_message = ...,
		on_error = handleWsError,
		on_close = handleWsClose
	)
	wsapp.run_forever(
		ping_interval = 5,
		ping_timeout = 3,
	)
	
	
def handleWsError(wsapp, error):
	...


def handleWsClose(wsapp, close_status_code, close_msg):
	wsapp.close()


def subscribeWS(
	wsapp,
	userId
):
	
	subscriptionMsg = {
		"subscribe":"location",
		"userId":[userId],
		"field":[
			"busId",
			"latitude",
			"longitude",
			"course",
			"paxLoad",
			"more"
		]
	}
	wsapp.send(json.dumps(subscriptionMsg))
	


	