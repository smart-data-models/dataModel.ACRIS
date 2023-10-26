<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=============
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `ClosingTime[string]`: 체크포인트 시설이 폐쇄된 날짜와 시간입니다. 날짜 시간은 ISO 8601 형식을 준수하는 UTC여야 합니다(예: 2023-04-20T11:54:59Z).  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

OperationTimePeriod:    
  description: Property. The time period over which the Checkpoint is operating.    
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
      description: It must be equal to OperationTimePeriod.    
      enum:    
        - OperationTimePeriod    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/OperationTimePeriod/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/OperationTimePeriod/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:OperationTimePeriod:id:XCIN:24494142",  
    "type": "OperationTimePeriod",  
    "ClosingTime": "23:59:02Z",  
    "OpeningTime": "00:00:00Z"  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:OperationTimePeriod:id:BCTN:53140922",  
  "type": "OperationTimePeriod",  
  "ClosingTime": {  
    "type": "date-time",  
    "value": "23:59:02Z"  
  },  
  "OpeningTime": {  
    "type": "date-time",  
    "@value": "00:00:02Z"  
  }  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:OperationTimePeriod:id:XCIN:24494142",  
    "type": "OperationTimePeriod",  
    "ClosingTime": "23:59:02Z",  
    "OpeningTime": "00:00:00Z",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
    ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


  "id": "urn:ngsi-ld:OperationTimePeriod:id:BCTN:53140922",  
  "type": "OperationTimePeriod",  
  "ClosingTime": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "23:59:02Z"  
    }  
  },  
  "OpeningTime": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "00:00:02Z"  
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
