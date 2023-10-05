/* (Beta) Export of data model AirportElevationUnitOfMeasurement of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AirportElevationUnitOfMeasurement_type AS ENUM ('AirportElevationUnitOfMeasurement');
CREATE TABLE AirportElevationUnitOfMeasurement (Name TEXT, type AirportElevationUnitOfMeasurement_type);