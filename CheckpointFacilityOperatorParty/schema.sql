/* (Beta) Export of data model CheckpointFacilityOperatorParty of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE CheckpointFacilityOperatorParty_type AS ENUM ('CheckpointFacilityOperatorParty');
CREATE TABLE CheckpointFacilityOperatorParty (Name TEXT, type CheckpointFacilityOperatorParty_type);