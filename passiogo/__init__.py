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
	
	
	# Handle JSON Response
	response = response.json()
	
	
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
	
	def checkTypes(self) -> None:
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


def getSystems(
	appVersion = 2,
	sortMode = 1,
) -> list[TransportationSystem]:
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
		try:
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
		except Exception as e:
			print(e)
			print(system)
			return()
	
	
	return(allSystems)


def printAllSystemsMd(
	includeHtmlBreaks = True
):
	systems = getSystems()
	
	for system in systems:
		print(f"- {system.name}{'<br/>' if includeHtmlBreaks else ''}")



def getAllRoutes(
	systemSelected,
	paramDigit = 1,
	amount = 1
):
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
	url = BASE_URL+"/mapGetData.php?getRoutes="+str(paramDigit)
	body = {
			"systemSelected0" : str(systemSelected),
			"amount" : amount
			}
	routes = sendApiRequest(url, body)
	
	# Handle Request Error
	if(routes == None):
		return(None)
	
	# Handle Differing Response Format
	if "all" in routes:
		routes = routes["all"]
	
	
	return(routes)


def getAllStops(
	systemSelected,
	paramDigit = 2,
	sA = 1,
	debug = 0
):
	"""
	Obtains all stop for the selected system.
	=========
	systemSelected: system from which to get content
	paramDigit: No discernable change
	sA:
		0: error
		1: Returns all stops for the given system
		>=2: Returns unrelated stops as well
	"""
	
	
	# Initialize & Send Request
	url = BASE_URL+"/mapGetData.php?getStops="+str(paramDigit)
	body = {
		"s0" : str(systemSelected),
		"sA" : sA
	}
	stops = sendApiRequest(url, body)
	
	# Handle Request Error
	if(stops == None):
		return(None)
	
	return(stops)


def getSystemAlerts(
	systemSelected,
	paramDigit = 1
):
	"""
	Gets all system alerts for the selected system.
	=========
	systemSelected: system from which to get content
	paramDigit:
		0: Error
		>=1: Valid
	"""
	
	
	# Initialize & Send Request
	url = BASE_URL+"/goServices.php?getAlertMessages="+str(paramDigit)
	body = {
		"systemSelected0" : str(systemSelected),
		"amount" : 1,
		"routesAmount":0
	}
	errorMsg = sendApiRequest(url, body)
	
	
	# Handle Request Error
	if(errorMsg == None):
		return(None)
	
	
	return(errorMsg)


def getBuses(
	systemSelected,
	paramDigit = 2
):
	"""
	Gets all currently running buses.
	=========
	s0: system from which to get content
	paramDigit:
		0: Error
		>=1: Valid
	"""
	
	
	# Initialize & Send Request
	url = BASE_URL+"/mapGetData.php?getBuses="+str(paramDigit)
	body = {
		"s0" : str(systemSelected),
		"sA" : 1
	}
	buses = sendApiRequest(url, body)
	
	# Handle Request Error
	if(buses == None):
		return(None)
	
	return(buses)




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
	vars.errors.append(f"->WebSocketError: {error}")


def handleWsClose(wsapp, close_status_code, close_msg):
	wsapp.close()
	vars.logs.append("Closing WebSocket")


def subscribeWS(
	wsapp,
	userId = 1068
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
	


	