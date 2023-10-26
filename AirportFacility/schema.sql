/* (Beta) Export of data model AirportFacility of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AirportFacility_type AS ENUM ('AirportFacility');
CREATE TABLE AirportFacility (IataCode TEXT, IcaoCode TEXT, Name TEXT, id TEXT PRIMARY KEY, type AirportFacility_type);