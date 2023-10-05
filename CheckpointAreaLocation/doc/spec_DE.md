<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: CheckpointAreaLocation  
===============================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/CheckpointAreaLocation/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Eigenschaft. Der geografische oder geopolitische Standort eines Kontrollpunkts**.  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `AirportElevation[object]`: Die Höhe eines Flughafens, über dem Meeresspiegel.  	- `AirportElevationUnitOfMeasurement[object]`: Die Maßeinheit für die Höhe eines Flughafens über dem Meeresspiegel (FT für Fuß oder M für Meter).    
	- `Name[string]`: Der Name eines Flughafens, der über dem Meeresspiegel liegt.    
	- `Value[number]`: Der Wert der Höhe eines Flughafens über dem Meeresspiegel.    
- `Latitude[number]`: Koordinate des Breitengrads des Kontrollpunkts.  - `Longitude[number]`: Koordinate des Längengrads der Lage des Kontrollpunktbereichs.  - `Name[string]`: Eindeutiger Name für den geografischen oder geopolitischen Standort eines Checkpoint Area Location.  - `Srid[number]`: Ein Spatial Reference System Identifier (SRID), um die Definitionen des räumlichen Koordinatensystems zu identifizieren  - `ZoneAreaLocation[object]`: Der geografische oder geopolitische Standort einer Warteschlangenzone in einem Terminal.  	- `Name[string]`: Eindeutiger Name für die Zone Area Location.    
	- `TerminalAreaLocation[object]`: Die geografische oder geopolitische Lage eines Flughafengebäudes.    
- `id[*]`: Eindeutiger Bezeichner der Entität  - `type[string]`: Sie muss gleich CheckpointAreaLocation sein.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Dieses Datenmodell ist ein Mapping des Passenger Wait Times Standard v1.6.0 des ACRIS-Datenschnittstellenstandards des Airports Council International (ACI). Verfügbar unter https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
CheckpointAreaLocation:    
  description: Property. The geospatial or geopolitical location of a Checkpoint.    
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
      type: number    
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
                  type: integer    
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
      description: It must be equal to CheckpointAreaLocation.    
      enum:    
        - CheckpointAreaLocation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/CheckpointAreaLocation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/CheckpointAreaLocation/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### CheckpointAreaLocation NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen CheckpointAreaLocation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CheckpointAreaLocation:id:BLBC:14665623",  
  "type": "CheckpointAreaLocation",  
  "Latitude": 40.42,  
  "Longitude": 3.708,  
  "Name": "As since dream public analysis clear one. Federal skill term court.",  
  "Srid": 4326,  
  "AirportElevation": {  
    "Name": "",  
    "Value": 777.7,  
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
        "Name": "Barajas",  
        "Srid": 4326  
      }  
    }  
  }  
}  
```  
</details>  
#### CheckpointAreaLocation NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen CheckpointAreaLocation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:CheckpointAreaLocation:id:KSRW:92816613",  
    "type": "CheckpointAreaLocation",  
    "Latitude": {  
        "type": "Number",  
        "value": 2.4  
    },  
    "Longitude": {  
        "type": "Number",  
        "value": 5.3  
    },  
    "Name": {  
        "type": "Text",  
        "value": ""  
    },  
    "Srid": {  
        "type": "Number",  
        "value": 4326  
    },  
    "AirportElevation": {  
        "type": "StructuredValue",  
        "value": {  
            "Name": "",  
            "Value": 487.8,  
            "AirportElevationUnitOfMeasurement": {  
                "Name": "Meters"  
            }  
        }  
    },  
    "ZoneAreaLocation": {  
        "type": "StructuredValue",  
        "value": {  
            "Name": "",  
            "TerminalAreaLocation": {  
                "Name": "Madrid",  
                "AirportLocation": {  
                    "Latitude": 40.41,  
                    "Longitude": 3.70,  
                    "Name": "",  
                    "Srid": 662  
                }  
            }  
        }  
    }  
}  
```  
</details>  
#### CheckpointAreaLocation NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen CheckpointAreaLocation im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:CheckpointAreaLocation:id:BLBC:14665623",  
  "type": "CheckpointAreaLocation",  
  "Latitude": 40.42,  
  "Longitude": 3.708,  
  "Name": "As since dream public analysis clear one. Federal skill term court.",  
  "Srid": 4326,  
  "AirportElevation": {  
    "Name": "",  
    "Value": 777.7,  
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
        "Name": "Barajas",  
        "Srid": 4326  
      }  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### CheckpointAreaLocation NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen CheckpointAreaLocation im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:CheckpointAreaLocation:id:KSRW:92816613",  
    "type": "CheckpointAreaLocation",  
    "Latitude": {  
        "type": "Property",  
        "value": 40.42  
    },  
    "Longitude": {  
        "type": "Property",  
        "value": 3.708  
    },  
    "Name": {  
        "type": "Property",  
        "value": "Madrid"  
    },  
    "Srid": {  
        "type": "Property",  
        "value": 4326  
    },  
    "AirportElevation": {  
        "type": "Property",  
        "value": {  
            "Name": "",  
            "Value": 487.8,  
            "AirportElevationUnitOfMeasurement": {  
                "Name": "Meters"  
            }  
        }  
    },  
    "ZoneAreaLocation": {  
        "type": "Property",  
        "value": {  
            "Name": "",  
            "TerminalAreaLocation": {  
                "Name": "Madrid",  
                "AirportLocation": {  
                    "Latitude": 40.42,  
                    "Longitude": 3.708,  
                    "Name": "",  
                    "Srid": 4326  
                }  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
