/* (Beta) Export of data model CheckpointFacilityType of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE CheckpointFacilityType_type AS ENUM ('CheckpointFacilityType');
CREATE TABLE CheckpointFacilityType (Code TEXT, Description TEXT, type CheckpointFacilityType_type);