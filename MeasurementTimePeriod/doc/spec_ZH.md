<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：测量时间段    
========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/MeasurementTimePeriod/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**属性。测量的时间段。    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `EndTime[string]`: 测量时间段结束时的日期和时间。日期时间应为 UTC，符合 ISO 8601 格式（例如 2023-04-20T11:54:59Z）  - `id[*]`: 实体的唯一标识符  - `type[string]`: 它必须等于 MeasurementTimePeriod。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
所需属性    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
该数据模型是国际机场协会 (ACI) ACRIS 数据接口标准的乘客等候时间标准 v1.6.0 的映射。可登录 https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf 查阅。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 属性的数据模型描述    
按字母顺序排列（点击查看详情）    
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
## 有效载荷示例    
#### MeasurementTimePeriod NGSI-v2 关键值 示例    
下面是一个以 JSON-LD 格式作为键值的 MeasurementTimePeriod 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MeasurementTimePeriod:id:SDGV:22291046",  
  "type": "MeasurementTimePeriod",  
  "EndTime": "2023-03-22T18:59:02Z"  
}  
```  
</details>    
#### MeasurementTimePeriod NGSI-v2 normalized 示例    
下面是一个规范化 JSON-LD 格式的 MeasurementTimePeriod 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
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
#### MeasurementTimePeriod NGSI-LD 关键值 示例    
下面是一个以 JSON-LD 格式作为键值的 MeasurementTimePeriod 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
#### MeasurementTimePeriod NGSI-LD normalized 示例    
下面是一个规范化 JSON-LD 格式的 MeasurementTimePeriod 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
