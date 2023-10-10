/* (Beta) Export of data model ZoneAreaLocation of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ZoneAreaLocation_type AS ENUM ('ZoneAreaLocation');
CREATE TABLE ZoneAreaLocation (Name TEXT, TerminalAreaLocation JSON, type ZoneAreaLocation_type);