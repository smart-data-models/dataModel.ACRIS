/* (Beta) Export of data model OperationTimePeriod of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE OperationTimePeriod_type AS ENUM ('OperationTimePeriod');
CREATE TABLE OperationTimePeriod (ClosingTime TEXT, OpeningTime TEXT, id TEXT PRIMARY KEY, type OperationTimePeriod_type);