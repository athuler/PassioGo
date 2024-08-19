import passiogo
import pytest

def pytest_namespace():
    return {'allSystems': None}

def test_getAllSystems():
	global allSystems
	allSystems = passiogo.getSystems()
	pytest.allSystems = allSystems
	assert True

test_getAllSystems()
ids = [f"{element.name} (#{element.id})" for element in pytest.allSystems]

def test_printAllSystems():
	passiogo.printAllSystemsMd()
	assert True


def test_getSystemFromId():
	global testSystem
	testSystem = passiogo.getSystemFromID(1068)
	assert True

def test_getRouteById():
	testSystem.getRouteById(133007)
	pass

@pytest.mark.parametrize("system", pytest.allSystems, ids=ids)
def test_getAllRoutes(system):
	system.getRoutes()

def test_getStopById():
	testSystem.getStopById(140059)
	pass

@pytest.mark.parametrize("system", pytest.allSystems, ids=ids)
def test_getAllStops(system):
	system.getStops()


@pytest.mark.parametrize("system", pytest.allSystems, ids=ids)
def test_getSystemAlerts(system):
	system.getSystemAlerts()

@pytest.mark.parametrize("system", pytest.allSystems, ids=ids)
def test_getVehicles(system):
	system.getVehicles()
	
