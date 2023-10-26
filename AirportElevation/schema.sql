/* (Beta) Export of data model AirportElevation of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AirportElevation_type AS ENUM ('AirportElevation');
CREATE TABLE AirportElevation (AirportElevationUnitOfMeasurement JSON, Name TEXT, Value NUMERIC, id TEXT PRIMARY KEY, type AirportElevation_type);