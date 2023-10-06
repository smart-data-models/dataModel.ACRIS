<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: CheckpointFacility  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/CheckpointFacility/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Proprietà. Informazioni su un punto di controllo in un aeroporto utilizzato per fornire servizi. Un Checkpoint è una struttura in cui i clienti e i passeggeri si presentano e devono essere trattati, assistiti o controllati prima di procedere alla fase successiva del loro viaggio. **  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `CheckpointAreaLocation[object]`: La posizione geospaziale o geopolitica di un Checkpoint.  	- `AirportElevation[object]`: L'altezza di un aeroporto, sopra il livello del mare.    
	- `Latitude[number]`: Coordinata della latitudine della posizione dell'area del checkpoint.    
	- `Longitude[number]`: Coordinata della longitudine della posizione dell'area del checkpoint.    
	- `Name[string]`: Nome univoco per la posizione geospaziale o geopolitica di un'area di controllo.    
	- `Srid[integer]`: Un identificatore del sistema di riferimento spaziale (SRID), per identificare le definizioni del sistema di coordinate spaziali.    
	- `ZoneAreaLocation[object]`: La posizione geospaziale o geopolitica di una zona di accodamento in un terminale.    
- `CheckpointFacilityOperatorParty[object]`: Informazioni che descrivono la parte responsabile della gestione di un punto di controllo in un aeroporto.  	- `Name[string]`: Nome univoco dell'Operator Party per la Checkpoint Facility.    
- `CheckpointFacilityType[object]`: Informazioni che descrivono la classificazione di un punto di controllo in un aeroporto. I valori sono: Controllo di sicurezza, Dogana.  	- `Code[string]`: Codice univoco per il tipo di struttura del punto di controllo.    
	- `Description[string]`: Descrizione del tipo di struttura del checkpoint.    
- `ConcourseFacility[object]`: Informazioni su un Concourse aeroportuale come edifici o infrastrutture utilizzate per fornire servizi.  	- `Identifier[string]`: Identificatore unico per l'impianto dell'atrio.    
	- `Name[string]`: Nome univoco per la struttura dell'atrio.    
	- `TerminalFacility[object]`: Informazioni su un Terminal aeroportuale come edifici o infrastrutture utilizzate per fornire servizi.    
- `Description[string]`: Descrizione della struttura Checkpoint.  - `Identifier[string]`: Identificatore univoco per la struttura del punto di controllo. L'identificativo deve essere unico all'interno di un aeroporto.  - `Name[string]`: Nome univoco per la struttura del checkpoint. Il nome deve essere unico all'interno di un aeroporto.  - `OperationTimePeriod[object]`: Il periodo di tempo in cui il Checkpoint è in funzione.  	- `ClosingTime[string]`: La data e l'ora di chiusura della Struttura di controllo. L'ora della data deve essere UTC, conforme al formato ISO 8601 (ad esempio, 2023-04-20T11:54:59Z).    
	- `OpeningTime[string]`: La data e l'ora di apertura della Struttura di controllo. L'ora della data deve essere UTC, conforme al formato ISO 8601 (ad esempio, 2023-04-20T11:54:59Z).    
- `id[*]`: Identificatore univoco dell'entità  - `type[string]`: Deve essere uguale a CheckpointFacility.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Questo modello di dati è una mappatura del Passenger Wait Times Standard v1.6.0 dell'Airports Council International (ACI) ACRIS data interface standard. Disponibile su https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CheckpointFacility:    
  description: 'Property. Information about a Checkpoint in an Airport used to provide services. A Checkpoint facility is any facility where customers and passengers turn up and need to be processed, serviced or screened before proceeding to the next stage of their journey. '    
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
      description: It must be equal to CheckpointFacility.    
      enum:    
        - CheckpointFacility    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/CheckpointFacility/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/CheckpointFacility/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### Valori delle chiavi di CheckpointFacility NGSI-v2 Esempio  
Ecco un esempio di CheckpointFacility in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CheckpointFacility:id:MMJG:16938337",  
  "type": "CheckpointFacility",  
  "Description": "control",  
  "Identifier": "control-1",  
  "Name": "",  
  "CheckpointAreaLocation": {  
    "Latitude": 40.42,  
    "Longitude": 3.708,  
    "Name": "gate 23",  
    "Srid": 0,  
    "AirportElevation": {  
      "Name": "",  
      "Value": 571.3,  
      "AirportElevationUnitOfMeasurement": {  
        "Name": "Mater"  
      }  
    },  
    "ZoneAreaLocation": {  
      "Name": "",  
      "TerminalAreaLocation": {  
        "Name": "",  
        "AirportLocation": {  
          "Latitude": 40.42,  
          "Longitude": 3.708,  
          "Name": "gate 23",  
          "Srid": 534  
        }  
      }  
    }  
  },  
  "CheckpointFacilityOperatorParty": {  
    "Name": ""  
  },  
  "CheckpointFacilityType": {  
    "Code": "",  
    "Description": ""  
  },  
  "ConcourseFacility": {  
    "Identifier": "",  
    "Name": "",  
    "TerminalFacility": {  
      "Identifier": "terminal 1",  
      "Name": "",  
      "AirportFacility": {  
        "IataCode": "BMA",  
        "IcaoCode": "ESSB",  
        "Name": ""  
      }  
    }  
  },  
  "OperationTimePeriod": {  
    "ClosingTime": "23:59:00Z",  
    "OpeningTime": "00:00:00Z"  
  }  
}  
```  
</details>  
#### CheckpointFacility NGSI-v2 normalizzato Esempio  
Ecco un esempio di CheckpointFacility in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CheckpointFacility:id:MGZO:29576657",  
  "type": "CheckpointFacility",  
  "Description": {  
    "type": "Text",  
    "value": "control"  
  },  
  "Identifier": {  
    "type": "Text",  
    "value": "Ba/B"  
  },  
  "Name": {  
    "type": "Text",  
    "value": ""  
  },  
  "CheckpointAreaLocation": {  
    "type": "Text",  
    "value": {  
      "Latitude": 8.0,  
      "Longitude": 5.1,  
      "Name": "gate 23",  
      "Srid": 441,  
      "AirportElevation": {  
        "Name": "",  
        "Value": 125.3,  
        "AirportElevationUnitOfMeasurement": {  
          "Name": "Meters"  
        }  
      },  
      "ZoneAreaLocation": {  
        "Name": "",  
        "TerminalAreaLocation": {  
          "Name": "",  
          "AirportLocation": {  
            "Latitude": 0.9,  
            "Longitude": 5.3,  
            "Name": "gate 23",  
            "Srid": 175  
          }  
        }  
      }  
    }  
  },  
  "CheckpointFacilityOperatorParty": {  
    "type": "StructuredValue",  
    "value": {  
      "Name": ""  
    }  
  },  
  "CheckpointFacilityType": {  
    "type": "StructuredValue",  
    "value": {  
      "Code": "",  
      "Description": ""  
    }  
  },  
  "ConcourseFacility": {  
    "type": "StructuredValue",  
    "value": {  
      "Identifier": "",  
      "Name": "",  
      "TerminalFacility": {  
        "Identifier": "terminal 1",  
        "Name": "",  
        "AirportFacility": {  
          "IataCode": "BMA",  
          "IcaoCode": "ESSB",  
          "Name": ""  
        }  
      }  
    }  
  },  
  "OperationTimePeriod": {  
    "type": "StructuredValue",  
    "value": {  
      "ClosingTime": "23:59:00Z",  
      "OpeningTime": "00:00:00Z"  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### CheckpointFacility Valori chiave NGSI-LD Esempio  
Ecco un esempio di CheckpointFacility in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CheckpointFacility:id:MMJG:16938337",  
  "type": "CheckpointFacility",  
  "Description": "control",  
  "Identifier": "control-1",  
  "Name": "",  
  "CheckpointAreaLocation": {  
    "Latitude": 40.42,  
    "Longitude": 3.708,  
    "Name": "gate 23",  
    "Srid": 0,  
    "AirportElevation": {  
      "Name": "",  
      "Value": 571.3,  
      "AirportElevationUnitOfMeasurement": {  
        "Name": "Mater"  
      }  
    },  
    "ZoneAreaLocation": {  
      "Name": "",  
      "TerminalAreaLocation": {  
        "Name": "",  
        "AirportLocation": {  
          "Latitude": 40.42,  
          "Longitude": 3.708,  
          "Name": "gate 23",  
          "Srid": 534  
        }  
      }  
    }  
  },  
  "CheckpointFacilityOperatorParty": {  
    "Name": ""  
  },  
  "CheckpointFacilityType": {  
    "Code": "",  
    "Description": ""  
  },  
  "ConcourseFacility": {  
    "Identifier": "",  
    "Name": "",  
    "TerminalFacility": {  
      "Identifier": "terminal 1",  
      "Name": "",  
      "AirportFacility": {  
        "IataCode": "BMA",  
        "IcaoCode": "ESSB",  
        "Name": ""  
      }  
    }  
  },  
  "OperationTimePeriod": {  
    "ClosingTime": "23:59:00Z",  
    "OpeningTime": "00:00:00Z"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### CheckpointFacility NGSI-LD normalizzato Esempio  
Ecco un esempio di CheckpointFacility in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CheckpointFacility:id:MGZO:29576657",  
  "type": "CheckpointFacility",  
  "Description": {  
    "type": "Property",  
    "value": "control"  
  },  
  "Identifier": {  
    "type": "Property",  
    "value": "control-1"  
  },  
  "Name": {  
    "type": "Property",  
    "value": ""  
  },  
  "CheckpointAreaLocation": {  
    "type": "Property",  
    "value": {  
      "Latitude": 8.0,  
      "Longitude": 5.1,  
      "Name": "gate 23",  
      "Srid": 0,  
      "AirportElevation": {  
        "Name": "",  
        "Value": 125.3,  
        "AirportElevationUnitOfMeasurement": {  
          "Name": "Meters"  
        }  
      },  
      "ZoneAreaLocation": {  
        "Name": "",  
        "TerminalAreaLocation": {  
          "Name": "",  
          "AirportLocation": {  
            "Latitude": 40.42,  
            "Longitude": 3.708,  
            "Name": "gate 23",  
            "Srid": 534  
          }  
        }  
      }  
    }  
  },  
  "CheckpointFacilityOperatorParty": {  
    "type": "Property",  
    "value": {  
      "Name": ""  
    }  
  },  
  "CheckpointFacilityType": {  
    "type": "Property",  
    "value": {  
      "Code": "",  
      "Description": ""  
    }  
  },  
  "ConcourseFacility": {  
    "type": "Property",  
    "value": {  
      "Identifier": "",  
      "Name": "",  
      "TerminalFacility": {  
        "Identifier": "terminal-1",  
        "Name": "",  
        "AirportFacility": {  
          "IataCode": "BMA",  
          "IcaoCode": "ESSB",  
          "Name": ""  
        }  
      }  
    }  
  },  
  "OperationTimePeriod": {  
    "type": "Property",  
    "value": {  
      "ClosingTime": "23:59:00Z",  
      "OpeningTime": "00:00:00Z"  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
