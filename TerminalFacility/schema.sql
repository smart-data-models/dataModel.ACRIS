/* (Beta) Export of data model TerminalFacility of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE TerminalFacility_type AS ENUM ('TerminalFacility');
CREATE TABLE TerminalFacility (AirportFacility JSON, Identifier TEXT, Name TEXT, id TEXT PRIMARY KEY, type TerminalFacility_type);