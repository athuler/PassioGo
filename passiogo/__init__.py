import requests
import websocket
import json

__version__ = "0.1.0"
BASE_URL = "https://passiogo.com"


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


def getAllRoutes(
	systemSelected = 1068,
	paramDigit = 1,
	amount = 1,
	debug = 0
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
	paramDigit = 2,
	systemSelected = 1068,
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
	paramDigit = 1,
	systemSelected = 1068,
	debug = 0
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
	paramDigit = 2,
	s0 = 1068,
	debug = 0
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
		"s0" : str(s0),
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
	


	