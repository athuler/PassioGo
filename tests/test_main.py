import passiogo

def test_getAllSystems():
	passiogo.getSystems
	

def test_printAllSystems():
	passiogo.printAllSystemsMd()

def test_getSystemFromId():
	global testSystem
	testSystem = passiogo.getSystemFromID(1068)

def test_getAllRoutes():
	testSystem.getRoutes()

def test_getAllStops():
	testSystem.getStops()
	
def test_getSystemAlerts():
	testSystem.getSystemAlerts()

def test_getBuses():
	passiogo.getBuses(1068)
	