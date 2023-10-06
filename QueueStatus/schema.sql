/* (Beta) Export of data model QueueStatus of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE QueueStatus_type AS ENUM ('QueueStatus');
CREATE TABLE QueueStatus (Name TEXT, type QueueStatus_type);