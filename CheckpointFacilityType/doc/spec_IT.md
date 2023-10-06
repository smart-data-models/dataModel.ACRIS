<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

==============================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `Code[string]`: Codice univoco per il tipo di struttura del punto di controllo.  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

CheckpointFacilityType:    
  description: 'Property. Information that describes the classification for a Checkpoint in an Airport. Values are: Security Screening, Customs.'    
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
      description: It must be equal to CheckpointFacilityType.    
      enum:    
        - CheckpointFacilityType    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/CheckpointFacilityType/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/CheckpointFacilityType/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:CheckpointFacilityType:id:DBOZ:17389826",  
    "type": "CheckpointFacilityType",  
    "Code": "code3",  
    "Description": ""  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:CheckpointFacilityType:id:UCGJ:56843368",  
    "type": "CheckpointFacilityType",  
    "Code": {  
        "type": "Text",  
        "value": "code3"  
    },  
    "Description": {  
        "type": "Text",  
        "value": ""  
    }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:CheckpointFacilityType:id:DBOZ:17389826",  
    "type": "CheckpointFacilityType",  
    "Code": "code3",  
    "Description": "",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
    ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:CheckpointFacilityType:id:UCGJ:56843368",  
    "type": "CheckpointFacilityType",  
    "Code": {  
        "type": "Property",  
        "value": "code3"  
    },  
    "Description": {  
        "type": "Property",  
        "value": ""  
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
