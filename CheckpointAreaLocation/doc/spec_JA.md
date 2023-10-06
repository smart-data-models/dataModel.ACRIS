<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=========================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `AirportElevation[object]`: 空港の海面からの高さ。  
	- `Name[string]`: 空港の海抜高度の名称。    
	- `Value[number]`: 空港の海抜値。    
- `Latitude[number]`: チェックポイントエリアの位置の緯度の座標。  
	- `TerminalAreaLocation[object]`: 空港ターミナルビルの地理空間的または地政学的位置。    
- `id[*]`: エンティティの一意識別子  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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



<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
