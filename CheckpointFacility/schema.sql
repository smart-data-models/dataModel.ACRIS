/* (Beta) Export of data model CheckpointFacility of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE CheckpointFacility_type AS ENUM ('CheckpointFacility');
CREATE TABLE CheckpointFacility (CheckpointAreaLocation JSON, CheckpointFacilityOperatorParty JSON, CheckpointFacilityType JSON, ConcourseFacility JSON, Description TEXT, Identifier TEXT, Name TEXT, OperationTimePeriod JSON, id TEXT PRIMARY KEY, type CheckpointFacility_type);