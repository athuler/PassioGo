# Changelog


## 0.3.0 (Unreleased)

### Added

- `TransportationSystem.getRouteById()` method to get a Route object by its ID
- `TransportationSystem.getStopById()` method to get a Stop object by its ID

### Changed

- `Route.id` is now handled as a string

### Removed


## 0.2.2 (2024-09-10)

### Added


### Changed

- Fixed key error while fetching systems. (#22)

### Removed


## 0.2.1 (2024-08-18)

### Added

- Testing for every transportation system
- `Vehicle` object
- `TransportationSystem.getVehicles()` which returns a list of `Vehicle` objects

### Changed

- Fixed `AttributeError: 'list' object has no attribute 'items'` error thrown in `TransportationSystem.getRoutes()`

### Removed


## 0.2.0 (2024-07-31)

### Added

- `TransportationSystem` class with the following methods: `getRoutes()`, `getStops()`, `getSystemAlerts()`
- `Route` class with the following method: `getStops()`
- `Stop` class
- `getSystems()`
- `getSystemsFromID()`
- `printAllSystemsMd()`

### Changed

### Removed


## 0.1.2 (2024-07-14)

### Added

- Added License

### Changed

- Fixed Documentation Build
- All 
- Fixed PyPi long description type
- `printAllSystemsMd()` has the new parameter `includeHtml` with a default of `True` to render HTML breaks after each line

### Removed

- Removed obsolete `debug` parameters


## 0.1.1 (2024-07-12)

### Added

- Create Documentation With ReadTheDocs.io
- Create Changelog
- New `getSystems()` Method
- New `printAllSystemsMd()` Method
- Added PyPi Project Links

### Changed

- Change Project Description

### Removed

- None


## 0.1.0 (2024-07-12)

- Initial Commit