/* (Beta) Export of data model PassengerProcessType of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE PassengerProcessType_type AS ENUM ('PassengerProcessType');
CREATE TABLE PassengerProcessType (Code TEXT, Description TEXT, type PassengerProcessType_type);