<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: QueueMeasurement  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/QueueMeasurement/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Propiedad. Información sobre las medidas (observaciones) de determinadas Medidas de una Cola de Pasajeros.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `MeasurementDevice[object]`: Información sobre el dispositivo (equipo) utilizado para realizar las mediciones (observaciones).  	- `MeasurementDeviceLocation[object]`: La ubicación geoespacial o geopolítica de un Dispositivo de Medición.    
	- `Name[string]`: Nombre único para el dispositivo de medición.    
- `MeasurementTimePeriod[object]`: Periodo de tiempo en el que se toma una medida.  	- `EndTime[string]`: La fecha y la hora al final del periodo de tiempo sobre el que se realiza una medición. La fecha y la hora deben ser UTC, de conformidad con el formato ISO 8601 (por ejemplo, 2023-04-20T11:54:59Z).    
- `Occupancy[number]`: El recuento de personas en la cola.  La unidad de medida es el número de personas. Esta métrica se actualiza cada cinco minutos.  - `PassengerQueue[object]`: Información sobre la cola de pasajeros. Una fila de personas que esperan para pasar por el proceso de control de seguridad.  	- `CheckpointFacility[object]`: Información sobre un puesto de control en un aeropuerto utilizado para prestar servicios. Un puesto de control es cualquier instalación a la que acuden clientes y pasajeros y que necesita ser procesada, atendida o controlada antes de pasar a la siguiente etapa de su viaje.    
	- `Identifier[string]`: Identificador único para la cola de pasajeros. El identificador debe ser único dentro de un aeropuerto.    
	- `Name[string]`: Nombre de la cola de pasajeros. El nombre debe ser único dentro de un aeropuerto.    
	- `PassengerProcess[object]`: Información sobre el proceso de partes pasajeras.    
	- `QueueLocation[object]`: La ubicación geoespacial o geopolítica de una cola de pasajeros.    
	- `QueueStatus[object]`: Información sobre el estado de una cola de pasajeros. Los valores pueden ser: Abierta, Cerrada.    
	- `QueueType[object]`: Información sobre el tipo de cola de pasajeros. Los valores pueden ser: Pre-Check, Private, Economy, Priority, KnownCrewMember.    
- `ProjectedWaitTime[number]`: El tiempo estimado que una persona que entra en la cola puede esperar. La unidad de medida son los segundos. Las estimaciones deben actualizarse cada cinco minutos.  - `Throughput[number]`: Número medio de pasajeros procesados durante la última hora. La unidad de medida es pasajeros por hora. Esta métrica se actualiza cada cinco minutos.  - `WaitTime[number]`: La duración que ha experimentado una persona que sale de la cola. La unidad de medida son los segundos. La cantidad representa el número medio de segundos experimentados por las personas que salen de la cola en los últimos cinco minutos. Las cantidades deben actualizarse cada cinco minutos.  - `id[*]`: Identificador único de la entidad  - `type[string]`: Debe ser igual a QueueMeasurement.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
Este modelo de datos es un mapeo del Estándar de Tiempos de Espera de Pasajeros v1.6.0 del estándar de interfaz de datos ACRIS del Consejo Internacional de Aeropuertos (ACI). Disponible en https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
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
## Ejemplo de carga útil  
#### QueueMeasurement NGSI-v2 key-values Ejemplo  
He aquí un ejemplo de una QueueMeasurement en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### QueueMeasurement NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de una QueueMeasurement en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### QueueMeasurement NGSI-LD key-values Ejemplo  
He aquí un ejemplo de una QueueMeasurement en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### QueueMeasurement NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de una QueueMeasurement en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
