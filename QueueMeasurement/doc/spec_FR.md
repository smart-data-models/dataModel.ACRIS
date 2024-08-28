<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : QueueMeasurement  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ACRIS/blob/master/QueueMeasurement/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Propriété. Informations sur les mesures (observations) de mesures particulières d'une file d'attente de passagers**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `MeasurementDevice[object]`: Informations sur le dispositif (équipement) utilisé pour prendre des mesures (observations).  	- `MeasurementDeviceLocation[object]`: L'emplacement géospatial ou géopolitique d'un appareil de mesure.    
	- `Name[string]`: Nom unique de l'appareil de mesure.    
- `MeasurementTimePeriod[object]`: La période de temps au cours de laquelle une mesure est prise.  	- `EndTime[string]`: La date et l'heure à la fin de la période de temps au cours de laquelle une mesure est prise. La date et l'heure doivent être exprimées en UTC, conformément au format ISO 8601 (par exemple 2023-04-20T11:54:59Z).    
- `Occupancy[number]`: Le nombre de personnes dans la file d'attente.  L'unité de mesure est le nombre de personnes. Cette mesure est mise à jour toutes les cinq minutes.  - `PassengerQueue[object]`: Informations sur la file d'attente des passagers. Une file de personnes qui attendent de passer le contrôle de sécurité.  	- `CheckpointFacility[object]`: Informations sur un point de contrôle dans un aéroport utilisé pour fournir des services. Un point de contrôle est une installation où les clients et les passagers se présentent et doivent être traités, entretenus ou contrôlés avant de passer à l'étape suivante de leur voyage.    
	- `Identifier[string]`: Identifiant unique pour la file d'attente des passagers. Cet identifiant doit être unique au sein d'un aéroport.    
	- `Name[string]`: Nom de la file d'attente des passagers. Ce nom doit être unique au sein de l'aéroport.    
	- `PassengerProcess[object]`: Informations sur le processus de la partie passagère.    
	- `QueueLocation[object]`: Emplacement géospatial ou géopolitique d'une file d'attente de passagers.    
	- `QueueStatus[object]`: Informations sur l'état d'une file d'attente de passagers. Les valeurs peuvent être : Ouvert, Fermé.    
	- `QueueType[object]`: Informations sur le type de file d'attente des passagers. Les valeurs peuvent être : Pre-Check, Private, Economy, Priority, KnownCrewMember : Pre-Check, Private, Economy, Priority, KnownCrewMember.    
- `ProjectedWaitTime[number]`: Temps d'attente estimé pour une personne entrant dans la file d'attente. L'unité de mesure est la seconde. Les estimations doivent être mises à jour toutes les cinq minutes.  - `Throughput[number]`: Nombre moyen de passagers traités au cours de l'heure écoulée. L'unité de mesure est le nombre de passagers par heure. Cette mesure est mise à jour toutes les cinq minutes.  - `WaitTime[number]`: Durée vécue par une personne sortant de la file d'attente. L'unité de mesure est la seconde. Le montant représente le nombre moyen de secondes vécues par les personnes sortant de la file d'attente au cours des cinq dernières minutes. Les montants doivent être mis à jour toutes les cinq minutes.  - `id[*]`: Identifiant unique de l'entité  - `type[string]`: Il doit être égal à QueueMeasurement.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
Ce modèle de données est un mappage de la norme sur les temps d'attente des passagers v1.6.0 de la norme d'interface de données ACRIS du Conseil international des aéroports (ACI). Disponible à l'adresse suivante : https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Modèle de données description des propriétés  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
QueueMeasurement:    
  description: Property. Information about the measurements (observations) of particular Measures of a Passenger Queue.    
  properties:    
    MeasurementDevice:    
      description: Information about the device (equipment) used to take measurements (observations).    
      properties:    
        MeasurementDeviceLocation:    
          description: The geospatial or geopolitical location of a Measurement Device.    
          properties:    
            Name:    
              description: Unique name for the location of the Measurement Device.    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        Name:    
          description: Unique name for the Measurement Device.    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    MeasurementTimePeriod:    
      description: The time period over which a Measurement is taken.    
      properties:    
        EndTime:    
          description: 'The date and time at the end of the time period over which a Measurement is taken. Date time should be UTC, compliant with ISO 8601 format (e.g. 2023-04-20T11:54:59Z)'    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    Occupancy:    
      description: The count of people in the queue.  The unit of measure is number of people. This metric is updated every five minutes.    
      type: number    
      x-ngsi:    
        type: Property    
    PassengerQueue:    
      description: Information about the Passenger Party Queue. A line of people waiting to pass through the security checkpoint process.    
      properties:    
        CheckpointFacility:    
          description: 'Information about a Checkpoint in an Airport used to provide services. A Checkpoint facility is any facility where customers and passengers turn up and need to be processed, serviced or screened before proceeding to the next stage of their journey. '    
          properties:    
            CheckpointAreaLocation:    
              description: The geospatial or geopolitical location of a Checkpoint.    
              properties:    
                AirportElevation:    
                  description: 'The height of an Airport, above sea level.'    
                  properties:    
                    AirportElevationUnitOfMeasurement:    
                      description: The unit of measure of the height of an Airport above sea level (FT for foot or M for metre).    
                      properties:    
                        Name:    
                          description: The name of the unit of measure for an Airport elevation above sea level.    
                          type: string    
                          x-ngsi:    
                            type: Property    
                      type: object    
                      x-ngsi:    
                        type: Property    
                    Name:    
                      description: The name of an Airport elevation above sea level.    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    Value:    
                      description: The value of an Airport elevation above sea level.    
                      type: number    
                      x-ngsi:    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
                Latitude:    
                  description: Coordinate of the latitude of the checkpoint area location.    
                  type: number    
                  x-ngsi:    
                    type: Property    
                Longitude:    
                  description: Coordinate of the longitude of the checkpoint area location.    
                  type: number    
                  x-ngsi:    
                    type: Property    
                Name:    
                  description: Unique name for geospatial or geopolitical location of a Checkpoint Area Location.    
                  type: string    
                  x-ngsi:    
                    type: Property    
                Srid:    
                  description: 'A Spatial Reference System Identifier (SRID), to identify the spatial coordinate system definitions'    
                  type: integer    
                  x-ngsi:    
                    type: Property    
                ZoneAreaLocation:    
                  description: The geospatial or geopolitical location of a Queuing Zone in a Terminal.    
                  properties:    
                    Name:    
                      description: Unique name for the Zone Area Location.    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    TerminalAreaLocation:    
                      description: The geospatial or geopolitical location of an Airport Terminal building.    
                      properties:    
                        AirportLocation:    
                          description: The geospatial or geopolitical location of an Airport.    
                          properties:    
                            Latitude:    
                              description: Coordinate for latitude of the Airport.    
                              type: number    
                              x-ngsi:    
                                type: Property    
                            Longitude:    
                              description: Coordinate for longitude of the Airport.    
                              type: number    
                              x-ngsi:    
                                type: Property    
                            Name:    
                              description: Unique name for the Airport Location.    
                              type: string    
                              x-ngsi:    
                                type: Property    
                            Srid:    
                              description: 'A Spatial Reference System Identifier (SRID), to identify the spatial coordinate system definitions.'    
                              type: number    
                              x-ngsi:    
                                type: Property    
                          type: object    
                          x-ngsi:    
                            type: Property    
                        Name:    
                          description: Unique name for the Terminal Area Location.    
                          type: string    
                          x-ngsi:    
                            type: Property    
                      type: object    
                      x-ngsi:    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
            CheckpointFacilityOperatorParty:    
              description: Information that describes the Party responsible for the operation of a Checkpoint in an Airport.    
              properties:    
                Name:    
                  description: Unique name of the Operator Party for the Checkpoint Facility.    
                  type: string    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
            CheckpointFacilityType:    
              description: 'Information that describes the classification for a Checkpoint in an Airport. Values are: Security Screening, Customs.'    
              properties:    
                Code:    
                  description: Unique code for the Checkpoint Facility Type.    
                  type: string    
                  x-ngsi:    
                    type: Property    
                Description:    
                  description: Description of the Checkpoint Facility Type.    
                  type: string    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
            ConcourseFacility:    
              description: Information about an Airport Concourse as buildings or infrastructure used to provide services.    
              properties:    
                Identifier:    
                  description: Unique identifier for the Concourse Facility.    
                  type: string    
                  x-ngsi:    
                    type: Property    
                Name:    
                  description: Unique name for the Concourse Facility.    
                  type: string    
                  x-ngsi:    
                    type: Property    
                TerminalFacility:    
                  description: Information about an Airport Terminal as buildings or infrastructure used to provide services.    
                  properties:    
                    AirportFacility:    
                      description: Information about an Airport as buildings or infrastructure used to provide services.    
                      properties:    
                        IataCode:    
                          description: Three character IATA code for the Airport.    
                          type: string    
                          x-ngsi:    
                            type: Property    
                        IcaoCode:    
                          description: Four character ICAO code for the Airport.    
                          type: string    
                          x-ngsi:    
                            type: Property    
                        Name:    
                          description: Common name of the Airport.    
                          type: string    
                          x-ngsi:    
                            type: Property    
                      type: object    
                      x-ngsi:    
                        type: Property    
                    Identifier:    
                      description: Unique identifier for the Terminal Facility.    
                      type: string    
                      x-ngsi:    
                        type: Property    
                    Name:    
                      description: Unique name for the Terminal Facility.    
                      type: string    
                      x-ngsi:    
                        type: Property    
                  type: object    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
            Description:    
              description: Description of the Checkpoint Facility.    
              type: string    
              x-ngsi:    
                type: Property    
            Identifier:    
              description: Unique identifier for the Checkpoint Facility. The identifier should be unique within an Airport.    
              type: string    
              x-ngsi:    
                type: Property    
            Name:    
              description: Unique name for the Checkpoint Facility. The name should be unique within an Airport.    
              type: string    
              x-ngsi:    
                type: Property    
            OperationTimePeriod:    
              description: The time period over which the Checkpoint is operating.    
              properties:    
                ClosingTime:    
                  description: 'The date and time from when the Checkpoint Facility is closed. Date time should be UTC, compliant with ISO 8601 format (e.g. 2023-04-20T11:54:59Z)'    
                  type: string    
                  x-ngsi:    
                    type: Property    
                OpeningTime:    
                  description: 'The date and time from when the Checkpoint Facility is open. Date time should be UTC, compliant with ISO 8601 format (e.g. 2023-04-20T11:54:59Z)'    
                  type: string    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        Identifier:    
          description: Unique identifier for the Passenger Queue. The identifier should be unique within an Airport.    
          type: string    
          x-ngsi:    
            type: Property    
        Name:    
          description: Name of the Passenger Queue. The name should be unique within an Airport.    
          type: string    
          x-ngsi:    
            type: Property    
        PassengerProcess:    
          description: Information about the Passenger Party Process.    
          properties:    
            Name:    
              description: Unique name for the Passenger Process.    
              type: string    
              x-ngsi:    
                type: Property    
            PassengerProcessType:    
              description: Information about the type of Passenger Party Process.    
              properties:    
                Code:    
                  description: Unique code for the type of Passenger Party Process.    
                  type: string    
                  x-ngsi:    
                    type: Property    
                Description:    
                  description: Description of the type of Passenger Party Process.    
                  type: string    
                  x-ngsi:    
                    type: Property    
              type: object    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        QueueLocation:    
          description: The geospatial or geopolitical location of a Passenger Queue.    
          properties:    
            Name:    
              description: Unique name for the Queue Location.    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        QueueStatus:    
          description: 'Information about the status of a Passenger Queue. Values can be: Open, Closed.'    
          properties:    
            Name:    
              description: Unique name for the status of the Passenger Queue.    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
        QueueType:    
          description: 'Information about the type of a Passenger Queue. Values can be: Pre-Check, Private, Economy, Priority, KnownCrewMember.'    
          properties:    
            Code:    
              description: Unique code for the type of Passenger Queue.    
              type: string    
              x-ngsi:    
                type: Property    
            Description:    
              description: Description of the type of Passenger Queue.    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    ProjectedWaitTime:    
      description: The estimated time that a person entering the queue can expect to wait. The unit of measure is seconds. Estimates are required to be updated every five minutes.    
      type: number    
      x-ngsi:    
        type: Property    
    Throughput:    
      description: The average number of passengers processed over the past hour. The unit of measure is passengers per hour. This metric is updated every five minutes.    
      type: number    
      x-ngsi:    
        type: Property    
    WaitTime:    
      description: The duration that a person exiting the queue has experienced. The unit of measure is seconds. The amount represents the average number of seconds experienced by people exiting the queue in the last five minutes. The amounts are required to be updated every five minutes.    
      type: number    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    type:    
      description: It must be equal to QueueMeasurement.    
      enum:    
        - QueueMeasurement    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/QueueMeasurement/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/QueueMeasurement/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### QueueMeasurement Valeurs clés NGSI-v2 Exemple  
Voici un exemple de QueueMeasurement au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:QueueMeasurement:id:IEQX:79193255",  
  "type": "QueueMeasurement",  
  "Occupancy": 58,  
  "ProjectedWaitTime": 544.4,  
  "Throughput": 384,  
  "WaitTime": 645.9,  
  "MeasurementDevice": {  
    "Name": "",  
    "MeasurementDeviceLocation": {  
      "Name": ""  
    }  
  },  
  "MeasurementTimePeriod": {  
    "EndTime": "2023-03-22T18:59:02Z"  
  },  
  "PassengerQueue": {  
    "Identifier": "1",  
    "Name": "1",  
    "CheckpointFacility": {  
      "Description": "",  
      "Identifier": "1bdaec90-7a42-11e7-bb31-be2e44b06b34",  
      "Name": "Checkpoint B",  
      "CheckpointAreaLocation": {  
        "Latitude": 40.42,  
        "Longitude": 3.08,  
        "Name": "",  
        "$rid": 0  
      },  
      "CheckpointFacilityOperatorParty": {  
        "Name": ""  
      },  
      "CheckpointFacilityType": {  
        "Code": "",  
        "Description": ""  
      },  
      "ConcourseFacility": {  
        "Identifier": "BA/B",  
        "Name": "Boarding Area B",  
        "TerminalFacility": {  
          "Identifier": "T1",  
          "Name": "Terminal 1",  
          "AirportFacility": {  
            "IataCode": "SFO",  
            "IcaoCode": "KSFO",  
            "Name": "San Francisco InternationalAirport"  
          }  
        }  
      },  
      "OperationTimePeriod": {  
        "ClosingTime": "",  
        "OpeningTime": ""  
      }  
    },  
    "PassengerProcess": {  
      "Name": "",  
      "PassengerProcessType": {  
        "Code": "",  
        "Description": ""  
      }  
    },  
    "QueueLocation": {  
      "Name": ""  
    },  
    "QueueStatus": {  
      "Name": ""  
    },  
    "QueueType": {  
      "Code": "",  
      "Description": ""  
    }  
  }  
}  
```  
</details>  
#### QueueMeasurement NGSI-v2 normalisé Exemple  
Voici un exemple de QueueMeasurement au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:QueueMeasurement:id:IEQX:79193255",  
  "type": "QueueMeasurement",  
  "Occupancy": {  
    "type": "Number",  
    "value": 58  
  },  
  "ProjectedWaitTime": {  
    "type": "Number",  
    "value": 544.4  
  },  
  "Throughput": {  
    "type": "Number",  
    "value": 384  
  },  
  "WaitTime": {  
    "type": "Number",  
    "value": 645.9  
  },  
  "MeasurementDevice": {  
    "type": "StructuredValue",  
    "value": {  
      "Name": "",  
      "MeasurementDeviceLocation": {  
        "Name": ""  
      }  
    }  
  },  
  "MeasurementTimePeriod": {  
    "type": "StructuredValue",  
    "value": {  
      "EndTime": "2023-03-22T18:59:02Z"  
    }  
  },  
  "PassengerQueue": {  
    "type": "StructuredValue",  
    "value": {  
      "Identifier": "1",  
      "Name": "1",  
      "CheckpointFacility": {  
        "Description": "",  
        "Identifier": "1bdaec90-7a42-11e7-bb31-be2e44b06b34",  
        "Name": "Checkpoint B",  
        "CheckpointAreaLocation": {  
          "Latitude": 40.42,  
          "Longitude": 3.08,  
          "Name": "",  
          "$rid": 0  
        },  
        "CheckpointFacilityOperatorParty": {  
          "Name": ""  
        },  
        "CheckpointFacilityType": {  
          "Code": "",  
          "Description": ""  
        },  
        "ConcourseFacility": {  
          "Identifier": "BA/B",  
          "Name": "Boarding Area B",  
          "TerminalFacility": {  
            "Identifier": "T1",  
            "Name": "Terminal 1",  
            "AirportFacility": {  
              "IataCode": "SFO",  
              "IcaoCode": "KSFO",  
              "Name": "San Francisco InternationalAirport"  
            }  
          }  
        },  
        "OperationTimePeriod": {  
          "ClosingTime": "",  
          "OpeningTime": ""  
        }  
      },  
      "PassengerProcess": {  
        "Name": "",  
        "PassengerProcessType": {  
          "Code": "",  
          "Description": ""  
        }  
      },  
      "QueueLocation": {  
        "Name": ""  
      },  
      "QueueStatus": {  
        "Name": ""  
      },  
      "QueueType": {  
        "Code": "",  
        "Description": ""  
      }  
    }  
  }  
}  
```  
</details>  
#### QueueMeasurement Valeurs clés NGSI-LD Exemple  
Voici un exemple de QueueMeasurement au format JSON-LD sous forme de valeurs clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:QueueMeasurement:id:IEQX:79193255",  
  "type": "QueueMeasurement",  
  "Occupancy": 58,  
  "ProjectedWaitTime": 544.4,  
  "Throughput": 384,  
  "WaitTime": 645.9,  
  "MeasurementDevice": {  
    "Name": "",  
    "MeasurementDeviceLocation": {  
      "Name": ""  
    }  
  },  
  "MeasurementTimePeriod": {  
    "EndTime": "2023-03-22T18:59:02Z"  
  },  
  "PassengerQueue": {  
    "Identifier": "1",  
    "Name": "1",  
    "CheckpointFacility": {  
      "Description": "",  
      "Identifier": "1bdaec90-7a42-11e7-bb31-be2e44b06b34",  
      "Name": "Checkpoint B",  
      "CheckpointAreaLocation": {  
        "Latitude": 43.02,  
        "longitude": 3.08  
      },  
      "CheckpointFacilityOperatorParty": {  
        "Name": ""  
      },  
      "CheckpointFacilityType": {  
        "Code": "",  
        "Description": ""  
      },  
      "ConcourseFacility": {  
        "Identifier": "BA/B",  
        "Name": "Boarding Area B",  
        "TerminalFacility": {  
          "Identifier": "T1",  
          "Name": "Terminal 1",  
          "AirportFacility": {  
            "IataCode": "SFO",  
            "IcaoCode": "KSFO",  
            "Name": "San Francisco InternationalAirport"  
          }  
        }  
      },  
      "OperationTimePeriod": {  
        "ClosingTime": "",  
        "OpeningTime": ""  
      }  
    },  
    "PassengerProcess": {  
      "Name": "",  
      "PassengerProcessType": {  
        "Code": "",  
        "Description": ""  
      }  
    },  
    "QueueLocation": {  
      "Name": ""  
    },  
    "QueueStatus": {  
      "Name": ""  
    },  
    "QueueType": {  
      "Code": "",  
      "Description": ""  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### QueueMeasurement NGSI-LD normalisé Exemple  
Voici un exemple de QueueMeasurement au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:QueueMeasurement:id:IEQX:79193255",  
  "type": "QueueMeasurement",  
  "Occupancy": {  
    "type": "Property",  
    "value": 58  
  },  
  "ProjectedWaitTime": {  
    "type": "Property",  
    "value": 544.4  
  },  
  "Throughput": {  
    "type": "Property",  
    "value": 384  
  },  
  "WaitTime": {  
    "type": "Property",  
    "value": 645.9  
  },  
  "MeasurementDevice": {  
    "type": "Property",  
    "value": {  
      "Name": "",  
      "MeasurementDeviceLocation": {  
        "Name": ""  
      }  
    }  
  },  
  "MeasurementTimePeriod": {  
    "type": "Property",  
    "value": {  
      "EndTime": "2023-03-22T18:59:02Z"  
    }  
  },  
  "PassengerQueue": {  
    "type": "Property",  
    "value": {  
      "Identifier": "1",  
      "Name": "1",  
      "CheckpointFacility": {  
        "Description": "",  
        "Identifier": "1bdaec90-7a42-11e7-bb31-be2e44b06b34",  
        "Name": "Checkpoint B",  
        "CheckpointAreaLocation": "",  
        "CheckpointFacilityOperatorParty": "",  
        "CheckpointFacilityType": "",  
        "ConcourseFacility": {  
          "Identifier": "BA/B",  
          "Name": "Boarding Area B",  
          "TerminalFacility": {  
            "Identifier": "T1",  
            "Name": "Terminal 1",  
            "AirportFacility": {  
              "IataCode": "SFO",  
              "IcaoCode": "KSFO",  
              "Name": "San Francisco InternationalAirport"  
            }  
          }  
        },  
        "OperationTimePeriod": {  
          "ClosingTime": "",  
          "OpeningTime": ""  
        }  
      },  
      "PassengerProcess": {  
        "Name": "",  
        "PassengerProcessType": {  
          "Code": "",  
          "Description": ""  
        }  
      },  
      "QueueLocation": {  
        "Name": ""  
      },  
      "QueueStatus": {  
        "Name": ""  
      },  
      "QueueType": {  
        "Code": "",  
        "Description": ""  
      }  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
