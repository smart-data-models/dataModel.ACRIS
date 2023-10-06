<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=======
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `AirportElevationUnitOfMeasurement[object]`: 机场距海平面高度的计量单位（FT 表示英尺，M 表示米）。  
- `Name[string]`: 机场海拔高度的名称。  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

AirportElevation:    
  description: 'Property. The height of an Airport, above sea level.'    
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
      description: It must be equal to AirportElevation.    
      enum:    
        - AirportElevation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/AirportElevation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/AirportElevation/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:AirportElevation:id:WOBQ:34953390",  
  "type": "AirportElevation",  
  "Name": "Agreement figure talk arrive responsibility popular. Election simple treat more next how speech.",  
  "Value": 502.8,  
  "AirportElevationUnitOfMeasurement": {  
    "Name": "Meters"  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:AirportElevation:id:BQPP:71138381",  
    "type": "AirportElevation",  
    "Name": {  
        "type": "Text",  
        "value": ""  
    },  
    "Value": {  
        "type": "Number",  
        "value": 400.6  
    },  
    "AirportElevationUnitOfMeasurement": {  
        "type": "StructuredValue",  
        "value": {  
            "Name": "meters"  
        }  
    }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:AirportElevation:id:WOBQ:34953390",  
  "type": "AirportElevation",  
  "Name": "",  
  "Value": 502.8,  
  "AirportElevationUnitOfMeasurement": {  
    "Name": "Meters"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:AirportElevation:id:BQPP:71138381",  
    "type": "AirportElevation",  
    "Name": {  
        "type": "Property",  
        "value": ""  
    },  
    "Value": {  
        "type": "Property",  
        "value": 400.6  
    },  
    "AirportElevationUnitOfMeasurement": {  
        "type": "Property",  
        "value": {  
            "Name": "Meters"  
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
