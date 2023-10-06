/* (Beta) Export of data model PassengerProcess of the subject dataModel.ACRIS for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE PassengerProcess_type AS ENUM ('PassengerProcess');
CREATE TABLE PassengerProcess (Name TEXT, PassengerProcessType JSON, type PassengerProcess_type);