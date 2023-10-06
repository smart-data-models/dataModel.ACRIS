/* (Beta) Export of data model MeasurementTimePeriod of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE MeasurementTimePeriod_type AS ENUM ('MeasurementTimePeriod');
CREATE TABLE MeasurementTimePeriod (EndTime TEXT, type MeasurementTimePeriod_type);