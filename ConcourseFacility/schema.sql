/* (Beta) Export of data model ConcourseFacility of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ConcourseFacility_type AS ENUM ('ConcourseFacility');
CREATE TABLE ConcourseFacility (Identifier TEXT, Name TEXT, TerminalFacility JSON, type ConcourseFacility_type);