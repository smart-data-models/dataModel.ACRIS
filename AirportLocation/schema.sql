/* (Beta) Export of data model AirportLocation of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE AirportLocation_type AS ENUM ('AirportLocation');
CREATE TABLE AirportLocation (Latitude NUMERIC, Longitude NUMERIC, Name TEXT, Srid NUMERIC, id TEXT PRIMARY KEY, type AirportLocation_type);