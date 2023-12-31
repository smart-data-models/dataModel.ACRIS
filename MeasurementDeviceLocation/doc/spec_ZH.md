<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：测量设备位置    
=========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/MeasurementDeviceLocation/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**属性。测量设备的地理空间或地理政治位置。    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `Name[string]`: 测量设备位置的唯一名称。  - `id[*]`: 实体的唯一标识符  - `type[string]`: 它必须等于 MeasurementDeviceLocation。  <!-- /30-PropertiesList -->    
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
MeasurementDeviceLocation:      
  description: Property. The geospatial or geopolitical location of a Measurement Device.      
  properties:      
    Name:      
      description: Unique name for the location of the Measurement Device.      
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
      description: It must be equal to MeasurementDeviceLocation.      
      enum:      
        - MeasurementDeviceLocation      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/MeasurementDeviceLocation/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/MeasurementDeviceLocation/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### MeasurementDeviceLocation NGSI-v2 键值示例    
下面是一个以 JSON-LD 格式作为键值的 MeasurementDeviceLocation 示例。当使用 `options=keyValues` 时，这与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MeasurementDeviceLocation:id:KPXH:42031063",  
  "type": "MeasurementDeviceLocation",  
  "Name": "MeasurementDeviceLocation1"  
}  
```  
</details>    
#### 测量设备位置 NGSI-v2 标准化示例    
下面是一个以 JSON-LD 格式规范化的 MeasurementDeviceLocation 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MeasurementDeviceLocation:id:BQQB:32372072",  
  "type": "MeasurementDeviceLocation",  
  "Name": {  
    "type": "Text",  
    "value": "MeasurementDeviceLocation1"  
  }  
}  
```  
</details>    
#### MeasurementDeviceLocation NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 MeasurementDeviceLocation 示例。当使用 `options=keyValues` 时，这与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MeasurementDeviceLocation:id:KPXH:42031063",  
  "type": "MeasurementDeviceLocation",  
  "Name": "MeasurementDeviceLocation1",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 测量设备位置 NGSI-LD 归一化示例    
下面是一个以 JSON-LD 格式规范化的 MeasurementDeviceLocation 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:MeasurementDeviceLocation:id:BQQB:32372072",  
    "type": "MeasurementDeviceLocation",  
    "Name": {  
        "type": "Property",  
        "value": "MeasurementDeviceLocation1"  
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
