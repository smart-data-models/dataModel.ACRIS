/* (Beta) Export of data model MeasurementDevice of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE MeasurementDevice_type AS ENUM ('MeasurementDevice');
CREATE TABLE MeasurementDevice (MeasurementDeviceLocation JSON, Name TEXT, type MeasurementDevice_type);