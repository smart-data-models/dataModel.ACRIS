<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=======
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `Name[string]`: 区域位置的唯一名称。  
	- `Name[string]`: 终端区域位置的唯一名称。    
- `id[*]`: 实体的唯一标识符  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

ZoneAreaLocation:    
  description: Property. The geospatial or geopolitical location of a Queuing Zone in a Terminal.    
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
      description: It must be equal to ZoneAreaLocation.    
      enum:    
        - ZoneAreaLocation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/ZoneAreaLocation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/ZoneAreaLocation/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:ZoneAreaLocation:id:IFIF:16457773",  
    "type": "ZoneAreaLocation",  
    "Name": "East are terminal 1 Madrid",  
    "TerminalAreaLocation": {  
        "Name": "East side",  
        "AirportLocation": {  
            "Latitude": 40.42,  
            "Longitude": 3.708,  
            "Name": "Madrid",  
            "Srid": 4326  
        }  
    }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:ZoneAreaLocation:id:EBXR:29001296",  
    "type": "ZoneAreaLocation",  
    "Name": {  
        "type": "Text",  
        "value": "East are terminal 1 Madrid"  
    },  
    "TerminalAreaLocation": {  
        "type": "StructuredValue",  
        "value": {  
            "Name": "Change more ground law television. Its fire such see.",  
            "AirportLocation": {  
                "Latitude": 40.42,  
                "Longitude": 3.708,  
                "Name": "East Side",  
                "Srid": 4326  
            }  
        }  
    }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:ZoneAreaLocation:id:IFIF:16457773",  
  "type": "ZoneAreaLocation",  
  "Name": "East are terminal 1 Madrid",  
  "TerminalAreaLocation": {  
    "Name": "East side",  
    "AirportLocation": {  
      "Latitude": 40.42,  
      "Longitude": 3.708,  
      "Name": "Madrid",  
      "Srid": 4326  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:ZoneAreaLocation:id:EBXR:29001296",  
    "type": "ZoneAreaLocation",  
    "Name": {  
        "type": "Property",  
        "value": "East are terminal 1 Madrid"  
    },  
    "TerminalAreaLocation": {  
        "type": "Property",  
        "value": {  
            "Name": "Change more ground law television. Its fire such see.",  
            "AirportLocation": {  
                "Latitude": 40.42,  
                "Longitude": 3.708,  
                "Name": "East Side",  
                "Srid": 4326  
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
