
#         # This code allows you to install a orion-ld broker in a linux system
#         # The manuals are here https://github.com/FIWARE/context.Orion-LD/tree/develop/doc/manuals-ld
#         
#         # INSTALL NGSI LD broker (OrionLD)
#         sudo docker pull mongo:3.6
#         sudo docker pull fiware/orion-ld
#         sudo docker network create fiware_default
#         sudo docker run -d --name=mongo-db --network=fiware_default --expose=27017 mongo:3.6 --bind_ip_all --smallfiles
#         sudo docker run -d --name fiware-orionld -h orion --network=fiware_default -p 1026:1026  fiware/orion-ld -dbhost mongo-db
#         
#         # TO RELAUNCH (only if you have already installed a broker in the same machine)
#         sudo docker stop fiware-orionld
#         sudo docker rm fiware-orionld
#         sudo docker stop mongo-db
#         sudo docker rm mongo-db
#         sudo docker network rm fiware_default
#         
#         # CHECK INSTANCES
#         # Check the broker is running
#         curl -X GET 'http://localhost:1026/version'
#         
#         # Check what entities are in the broker
#         curl -X GET http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000
#         
#         # now the python code you can use to insert some value in the context broker according to the data model
#         
from pysmartdatamodels import pysmartdatamodels as sdm
import subprocess
serverUrl = "http://localhost:1026" # supposed that your broker is installed in localhost. Edit to match your configuration
dataModel = "PassengerQueue"
subject = "dataModel.ACRIS"
Identifier = "{'type': 'Property', 'value': '1'}"
attribute = "Identifier"
value = Identifier
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

Name = "{'type': 'Property', 'value': '1'}"
attribute = "Name"
value = Name
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

CheckpointFacility = {'type': 'Property', 'value': {'Description': '', 'Identifier': '1bdaec90-7a42-11e7-bb31-be2e44b06b34', 'Name': 'Checkpoint B', 'CheckpointAreaLocation': {'Latitude': 40.42, 'Longitude': 3.708, 'Name': '', 'Srid': 0, 'AirportElevation': {'Name': '', 'Value': 3.6, 'AirportElevationUnitOfMeasurement': {'Name': 'Meters'}}, 'ZoneAreaLocation': {'Name': '', 'TerminalAreaLocation': {'Name': '', 'AirportLocation': {'Latitude': 40.42, 'Longitude': 3.708, 'Name': 'Barajas', 'Srid': 0}}}}, 'CheckpointFacilityOperatorParty': {'Name': ''}, 'CheckpointFacilityType': {'Code': '', 'Description': ''}, 'ConcourseFacility': {'Identifier': 'BA/B', 'Name': 'Boarding area B', 'TerminalFacility': {'Identifier': 'T1', 'Name': 'Terminal 1', 'AirportFacility': {'IataCode': 'SFO', 'IcaoCode': 'KSFO', 'Name': 'San Francisco Internationl Airport'}}}, 'OperationTimePeriod': {'ClosingTime': '', 'OpeningTime': ''}}}
attribute = "CheckpointFacility"
value = CheckpointFacility
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

PassengerProcess = {'type': 'Property', 'value': {'Name': '', 'PassengerProcessType': {'Code': '', 'Description': ''}}}
attribute = "PassengerProcess"
value = PassengerProcess
# The next line creates the query for inserting this attribute in a NGSI-LD context broker if the attribute does not exist it creates it
print(sdm.update_broker(dataModel, subject, attribute, value, serverUrl=serverUrl, updateThenCreate=True))

print(" In case you have installed the orion-ld broker (see comments on the header of this program)")
print(" Execute this instruction to check that the entities has been inserted")
command = ['curl', '-X', 'GET', 'http://localhost:1026/ngsi-ld/v1/entities?local=true&limit=1000']
result = subprocess.run(command, capture_output=True, text=True)
print(result.stdout)