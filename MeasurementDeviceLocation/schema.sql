/* (Beta) Export of data model MeasurementDeviceLocation of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE MeasurementDeviceLocation_type AS ENUM ('MeasurementDeviceLocation');
CREATE TABLE MeasurementDeviceLocation (Name TEXT, type MeasurementDeviceLocation_type);