/* (Beta) Export of data model QueueLocation of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE QueueLocation_type AS ENUM ('QueueLocation');
CREATE TABLE QueueLocation (Name TEXT, id TEXT PRIMARY KEY, type QueueLocation_type);