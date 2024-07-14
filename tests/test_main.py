import passiogo

def test_getAllRoutes():
	passiogo.getAllRoutes(1068)

def test_getAllStops():
	passiogo.getAllStops(1068)
	
def test_getSystemAlerts():
	passiogo.getSystemAlerts(1068)

def test_getBuses():
	passiogo.getBuses(1068)

def test_getSystems():
	passiogo.getSystems()
	
def test_printAllSystems():
	passiogo.printAllSystemsMd()