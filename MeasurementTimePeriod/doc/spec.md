<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entity: MeasurementTimePeriod    
=============================<!-- /10-Header -->    
<!-- 15-License -->    
[Open License](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/MeasurementTimePeriod/LICENSE.md)    
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Global description: **Property. The time period over which a Measurement is taken.**    
version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## List of properties    
<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>    
- `EndTime[string]`: The date and time at the end of the time period over which a Measurement is taken. Date time should be UTC, compliant with ISO 8601 format (e.g. 2023-04-20T11:54:59Z)  - `id[*]`: Unique identifier of the entity  - `type[string]`: It must be equal to MeasurementTimePeriod.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Required properties    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
This data model is a mapping of the Passenger Wait Times Standard v1.6.0 of the Airports Council International (ACI) ACRIS data interface standard. Available at https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Data Model description of properties    
Sorted alphabetically (click for details)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
MeasurementTimePeriod:      
  description: Property. The time period over which a Measurement is taken.      
  properties:      
    EndTime:      
      description: 'The date and time at the end of the time period over which a Measurement is taken. Date time should be UTC, compliant with ISO 8601 format (e.g. 2023-04-20T11:54:59Z)'      
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
      description: It must be equal to MeasurementTimePeriod.      
      enum:      
        - MeasurementTimePeriod      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/MeasurementTimePeriod/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/MeasurementTimePeriod/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Example payloads      
#### MeasurementTimePeriod NGSI-v2 key-values Example      
Here is an example of a MeasurementTimePeriod in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MeasurementTimePeriod:id:SDGV:22291046",  
  "type": "MeasurementTimePeriod",  
  "EndTime": "2023-03-22T18:59:02Z"  
}  
```  
</details>    
#### MeasurementTimePeriod NGSI-v2 normalized Example      
Here is an example of a MeasurementTimePeriod in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MeasurementTimePeriod:id:RKKY:28707515",  
  "type": "MeasurementTimePeriod",  
  "EndTime": {  
    "type": "DateTime",  
    "value": "2023-03-22T18:59:02Z"  
  }  
}  
```  
</details>    
#### MeasurementTimePeriod NGSI-LD key-values Example      
Here is an example of a MeasurementTimePeriod in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MeasurementTimePeriod:id:SDGV:22291046",  
  "type": "MeasurementTimePeriod",  
  "EndTime": "2023-03-22T18:59:02Z",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### MeasurementTimePeriod NGSI-LD normalized Example      
Here is an example of a MeasurementTimePeriod in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MeasurementTimePeriod:id:RKKY:28707515",  
  "type": "MeasurementTimePeriod",  
  "EndTime": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2023-03-22T18:59:02Z"  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
