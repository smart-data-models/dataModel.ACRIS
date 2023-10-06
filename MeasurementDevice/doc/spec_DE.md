<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

==========================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->
<!-- /20-Description -->
<!-- 30-PropertiesList -->




<!-- /30-PropertiesList -->
<!-- 35-RequiredProperties -->

- Keine erforderlichen Eigenschaften  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

MeasurementDevice:    
  description: Property. Information about the device (equipment) used to take measurements (observations).    
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
      description: It must be equal to MeasurementDevice.    
      enum:    
        - MeasurementDevice    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/MeasurementDevice/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/MeasurementDevice/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:MeasurementDevice:id:TKHP:61060694",  
    "type": "MeasurementDevice",  
    "Name": "MeasurementDevice1",  
    "MeasurementDeviceLocation": {  
        "Name": "Gate23"  
    }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:MeasurementDevice:id:VGWX:01135533",  
    "type": "MeasurementDevice",  
    "Name": {  
        "type": "Text",  
        "value": "MeasurementDevice1"  
    },  
    "MeasurementDeviceLocation": {  
        "type": "Text",  
        "value": {  
            "Name": "Gate23"  
        }  
    }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:MeasurementDevice:id:TKHP:61060694",  
  "type": "MeasurementDevice",  
  "Name": "MeasurementDevice1",  
  "MeasurementDeviceLocation": {  
    "Name": "Gate23"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:MeasurementDevice:id:VGWX:01135533",  
    "type": "MeasurementDevice",  
    "Name": {  
        "type": "Property",  
        "value": "MeasurementDevice1"  
    },  
    "MeasurementDeviceLocation": {  
        "type": "Property",  
        "value": {  
            "Name": "Gate23"  
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
