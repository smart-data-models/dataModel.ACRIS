<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
实体：检查站设施    
========<!-- /10-Header -->    
<!-- 15-License -->    
[开放许可](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/CheckpointFacility/LICENSE.md)    
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
全局描述：**属性。机场内用于提供服务的检查站信息。安检站设施是指顾客和乘客在进入下一行程之前，需要在此接受处理、服务或检查的任何设施。**    
版本： 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 属性列表    
<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。    
- `CheckpointAreaLocation[object]`: 检查站的地理空间或地缘政治位置。  	- `AirportElevation[object]`: 机场海拔高度。      
	- `Latitude[number]`: 检查站区域位置的纬度坐标。      
	- `Longitude[number]`: 检查站区域位置的经度坐标。      
	- `Name[string]`: 检查站区域位置的地理空间或地理政治位置的唯一名称。      
	- `Srid[integer]`: 空间参照系统标识符（SRID），用于标识空间坐标系定义      
	- `ZoneAreaLocation[object]`: 航站楼内排队区的地理空间或地理政治位置。      
- `CheckpointFacilityOperatorParty[object]`: 描述负责机场检查站运行的一方的信息。  	- `Name[string]`: 检查站设施操作方的唯一名称。      
- `CheckpointFacilityType[object]`: 描述机场检查站分类的信息。值为安检、海关。  	- `Code[string]`: 检查站设施类型的唯一代码。      
	- `Description[string]`: 检查站设施类型说明。      
- `ConcourseFacility[object]`: 机场航站楼作为用于提供服务的建筑物或基础设施的信息。  	- `Identifier[string]`: 大堂设施的唯一标识符。      
	- `Name[string]`: 大堂设施的唯一名称。      
	- `TerminalFacility[object]`: 机场航站楼的信息，如用于提供服务的建筑物或基础设施。      
- `Description[string]`: 检查站设施说明。  - `Identifier[string]`: 检查站设施的唯一标识符。该标识符在机场内应是唯一的。  - `Name[string]`: 检查站设施的唯一名称。该名称在机场内应是唯一的。  - `OperationTimePeriod[object]`: 检查点运行的时间段。  	- `ClosingTime[string]`: 检查站设施关闭的日期和时间。日期时间应为 UTC，符合 ISO 8601 格式（例如 2023-04-20T11:54:59Z）      
	- `OpeningTime[string]`: 检查站设施开放的日期和时间。日期时间应为 UTC，符合 ISO 8601 格式（例如 2023-04-20T11:54:59Z）      
- `id[*]`: 实体的唯一标识符  - `type[string]`: 它必须等于 CheckpointFacility。  <!-- /30-PropertiesList -->    
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
CheckpointFacility:      
  description: 'Property. Information about a Checkpoint in an Airport used to provide services. A Checkpoint facility is any facility where customers and passengers turn up and need to be processed, serviced or screened before proceeding to the next stage of their journey. '      
  properties:      
    CheckpointAreaLocation:      
      description: The geospatial or geopolitical location of a Checkpoint.      
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
          type: integer      
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
          type: object      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    CheckpointFacilityOperatorParty:      
      description: Information that describes the Party responsible for the operation of a Checkpoint in an Airport.      
      properties:      
        Name:      
          description: Unique name of the Operator Party for the Checkpoint Facility.      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    CheckpointFacilityType:      
      description: 'Information that describes the classification for a Checkpoint in an Airport. Values are: Security Screening, Customs.'      
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
      type: object      
      x-ngsi:      
        type: Property      
    ConcourseFacility:      
      description: Information about an Airport Concourse as buildings or infrastructure used to provide services.      
      properties:      
        Identifier:      
          description: Unique identifier for the Concourse Facility.      
          type: string      
          x-ngsi:      
            type: Property      
        Name:      
          description: Unique name for the Concourse Facility.      
          type: string      
          x-ngsi:      
            type: Property      
        TerminalFacility:      
          description: Information about an Airport Terminal as buildings or infrastructure used to provide services.      
          properties:      
            AirportFacility:      
              description: Information about an Airport as buildings or infrastructure used to provide services.      
              properties:      
                IataCode:      
                  description: Three character IATA code for the Airport.      
                  type: string      
                  x-ngsi:      
                    type: Property      
                IcaoCode:      
                  description: Four character ICAO code for the Airport.      
                  type: string      
                  x-ngsi:      
                    type: Property      
                Name:      
                  description: Common name of the Airport.      
                  type: string      
                  x-ngsi:      
                    type: Property      
              type: object      
              x-ngsi:      
                type: Property      
            Identifier:      
              description: Unique identifier for the Terminal Facility.      
              type: string      
              x-ngsi:      
                type: Property      
            Name:      
              description: Unique name for the Terminal Facility.      
              type: string      
              x-ngsi:      
                type: Property      
          type: object      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    Description:      
      description: Description of the Checkpoint Facility.      
      type: string      
      x-ngsi:      
        type: Property      
    Identifier:      
      description: Unique identifier for the Checkpoint Facility. The identifier should be unique within an Airport.      
      type: string      
      x-ngsi:      
        type: Property      
    Name:      
      description: Unique name for the Checkpoint Facility. The name should be unique within an Airport.      
      type: string      
      x-ngsi:      
        type: Property      
    OperationTimePeriod:      
      description: The time period over which the Checkpoint is operating.      
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
      description: It must be equal to CheckpointFacility.      
      enum:      
        - CheckpointFacility      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/CheckpointFacility/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/CheckpointFacility/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 有效载荷示例    
#### CheckpointFacility NGSI-v2 密钥值示例    
下面是一个以 JSON-LD 格式作为键值的 CheckpointFacility 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CheckpointFacility:id:MMJG:16938337",  
  "type": "CheckpointFacility",  
  "Description": "control",  
  "Identifier": "control-1",  
  "Name": "",  
  "CheckpointAreaLocation": {  
    "Latitude": 40.42,  
    "Longitude": 3.708,  
    "Name": "gate 23",  
    "Srid": 0,  
    "AirportElevation": {  
      "Name": "",  
      "Value": 571.3,  
      "AirportElevationUnitOfMeasurement": {  
        "Name": "Mater"  
      }  
    },  
    "ZoneAreaLocation": {  
      "Name": "",  
      "TerminalAreaLocation": {  
        "Name": "",  
        "AirportLocation": {  
          "Latitude": 40.42,  
          "Longitude": 3.708,  
          "Name": "gate 23",  
          "Srid": 534  
        }  
      }  
    }  
  },  
  "CheckpointFacilityOperatorParty": {  
    "Name": ""  
  },  
  "CheckpointFacilityType": {  
    "Code": "",  
    "Description": ""  
  },  
  "ConcourseFacility": {  
    "Identifier": "",  
    "Name": "",  
    "TerminalFacility": {  
      "Identifier": "terminal 1",  
      "Name": "",  
      "AirportFacility": {  
        "IataCode": "BMA",  
        "IcaoCode": "ESSB",  
        "Name": ""  
      }  
    }  
  },  
  "OperationTimePeriod": {  
    "ClosingTime": "23:59:00Z",  
    "OpeningTime": "00:00:00Z"  
  }  
}  
```  
</details>    
#### CheckpointFacility NGSI-v2 标准化示例    
下面是一个以 JSON-LD 格式规范化的 CheckpointFacility 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CheckpointFacility:id:MGZO:29576657",  
  "type": "CheckpointFacility",  
  "Description": {  
    "type": "Text",  
    "value": "control"  
  },  
  "Identifier": {  
    "type": "Text",  
    "value": "Ba/B"  
  },  
  "Name": {  
    "type": "Text",  
    "value": ""  
  },  
  "CheckpointAreaLocation": {  
    "type": "StructuredValue",  
    "value": {  
      "Latitude": 8.0,  
      "Longitude": 5.1,  
      "Name": "gate 23",  
      "Srid": 441,  
      "AirportElevation": {  
        "Name": "",  
        "Value": 125.3,  
        "AirportElevationUnitOfMeasurement": {  
          "Name": "Meters"  
        }  
      },  
      "ZoneAreaLocation": {  
        "Name": "",  
        "TerminalAreaLocation": {  
          "Name": "",  
          "AirportLocation": {  
            "Latitude": 0.9,  
            "Longitude": 5.3,  
            "Name": "gate 23",  
            "Srid": 175  
          }  
        }  
      }  
    }  
  },  
  "CheckpointFacilityOperatorParty": {  
    "type": "StructuredValue",  
    "value": {  
      "Name": ""  
    }  
  },  
  "CheckpointFacilityType": {  
    "type": "StructuredValue",  
    "value": {  
      "Code": "",  
      "Description": ""  
    }  
  },  
  "ConcourseFacility": {  
    "type": "StructuredValue",  
    "value": {  
      "Identifier": "",  
      "Name": "",  
      "TerminalFacility": {  
        "Identifier": "terminal 1",  
        "Name": "",  
        "AirportFacility": {  
          "IataCode": "BMA",  
          "IcaoCode": "ESSB",  
          "Name": ""  
        }  
      }  
    }  
  },  
  "OperationTimePeriod": {  
    "type": "StructuredValue",  
    "value": {  
      "ClosingTime": "23:59:00Z",  
      "OpeningTime": "00:00:00Z"  
    }  
  }  
}  
```  
</details>    
#### 检查点设施 NGSI-LD 键值示例    
下面是一个以 JSON-LD 格式作为键值的 CheckpointFacility 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CheckpointFacility:id:MMJG:16938337",  
  "type": "CheckpointFacility",  
  "Description": "control",  
  "Identifier": "control-1",  
  "Name": "",  
  "CheckpointAreaLocation": {  
    "Latitude": 40.42,  
    "Longitude": 3.708,  
    "Name": "gate 23",  
    "Srid": 0,  
    "AirportElevation": {  
      "Name": "",  
      "Value": 571.3,  
      "AirportElevationUnitOfMeasurement": {  
        "Name": "Mater"  
      }  
    },  
    "ZoneAreaLocation": {  
      "Name": "",  
      "TerminalAreaLocation": {  
        "Name": "",  
        "AirportLocation": {  
          "Latitude": 40.42,  
          "Longitude": 3.708,  
          "Name": "gate 23",  
          "Srid": 534  
        }  
      }  
    }  
  },  
  "CheckpointFacilityOperatorParty": {  
    "Name": ""  
  },  
  "CheckpointFacilityType": {  
    "Code": "",  
    "Description": ""  
  },  
  "ConcourseFacility": {  
    "Identifier": "",  
    "Name": "",  
    "TerminalFacility": {  
      "Identifier": "terminal 1",  
      "Name": "",  
      "AirportFacility": {  
        "IataCode": "BMA",  
        "IcaoCode": "ESSB",  
        "Name": ""  
      }  
    }  
  },  
  "OperationTimePeriod": {  
    "ClosingTime": "23:59:00Z",  
    "OpeningTime": "00:00:00Z"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### 检查点设施 NGSI-LD 标准化示例    
下面是一个检查点设施（CheckpointFacility）的 JSON-LD 格式规范化示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CheckpointFacility:id:MGZO:29576657",  
  "type": "CheckpointFacility",  
  "Description": {  
    "type": "Property",  
    "value": "control"  
  },  
  "Identifier": {  
    "type": "Property",  
    "value": "control-1"  
  },  
  "Name": {  
    "type": "Property",  
    "value": ""  
  },  
  "CheckpointAreaLocation": {  
    "type": "Property",  
    "value": {  
      "Latitude": 8.0,  
      "Longitude": 5.1,  
      "Name": "gate 23",  
      "Srid": 0,  
      "AirportElevation": {  
        "Name": "",  
        "Value": 125.3,  
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
            "Name": "gate 23",  
            "Srid": 534  
          }  
        }  
      }  
    }  
  },  
  "CheckpointFacilityOperatorParty": {  
    "type": "Property",  
    "value": {  
      "Name": ""  
    }  
  },  
  "CheckpointFacilityType": {  
    "type": "Property",  
    "value": {  
      "Code": "",  
      "Description": ""  
    }  
  },  
  "ConcourseFacility": {  
    "type": "Property",  
    "value": {  
      "Identifier": "",  
      "Name": "",  
      "TerminalFacility": {  
        "Identifier": "terminal-1",  
        "Name": "",  
        "AirportFacility": {  
          "IataCode": "BMA",  
          "IcaoCode": "ESSB",  
          "Name": ""  
        }  
      }  
    }  
  },  
  "OperationTimePeriod": {  
    "type": "Property",  
    "value": {  
      "ClosingTime": "23:59:00Z",  
      "OpeningTime": "00:00:00Z"  
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
