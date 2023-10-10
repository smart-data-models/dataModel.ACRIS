/* (Beta) Export of data model TerminalAreaLocation of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE TerminalAreaLocation_type AS ENUM ('TerminalAreaLocation');
CREATE TABLE TerminalAreaLocation (AirportLocation JSON, Name TEXT, type TerminalAreaLocation_type);