<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：机场标高    
=======<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/AirportElevation/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**属性。机场海拔高度。    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `AirportElevationUnitOfMeasurement[object]`: 机场距海平面高度的计量单位（FT 表示英尺，M 表示米）。  	- `Name[string]`: 机场海拔高度的度量单位名称。      
- `Name[string]`: 机场海拔高度的名称。  - `Value[number]`: 机场海拔高度值。  - `id[*]`: 实体的唯一标识符  - `type[string]`: 它必须等于 AirportElevation。  <!-- /30-PropertiesList -->    
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
## 有效载荷示例    
#### AirportElevation NGSI-v2 关键值 示例    
下面是一个以 JSON-LD 格式作为键值的 AirportElevation 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
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
#### AirportElevation NGSI-v2 归一化示例    
下面是一个规范化 JSON-LD 格式的 AirportElevation 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
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
#### AirportElevation NGSI-LD 关键值 示例    
下面是一个以 JSON-LD 格式作为键值的 AirportElevation 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
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
#### 机场高程 NGSI-LD 归一化示例    
下面是一个规范化 JSON-LD 格式的 AirportElevation 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
