/* (Beta) Export of data model QueueType of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE QueueType_type AS ENUM ('QueueType');
CREATE TABLE QueueType (Code TEXT, Description TEXT, id TEXT PRIMARY KEY, type QueueType_type);