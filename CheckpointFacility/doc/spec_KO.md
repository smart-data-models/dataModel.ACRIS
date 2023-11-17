<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 체크포인트 시설    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/CheckpointFacility/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **속성. 서비스 제공에 사용되는 공항 내 보안 검색대에 대한 정보입니다. 체크포인트 시설은 고객과 승객이 다음 여정 단계로 진행하기 전에 처리, 서비스 또는 검색을 받아야 하는 모든 시설입니다. **    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `CheckpointAreaLocation[object]`: 체크포인트의 지리공간적 또는 지정학적 위치입니다.  	- `AirportElevation[object]`: 해발 기준 공항의 높이입니다.      
	- `Latitude[number]`: 체크포인트 지역 위치의 위도 좌표입니다.      
	- `Longitude[number]`: 체크포인트 지역 위치의 경도 좌표입니다.      
	- `Name[string]`: 체크포인트 영역 위치의 지리공간적 또는 지정학적 위치에 대한 고유 이름입니다.      
	- `Srid[integer]`: 공간 좌표계 정의를 식별하기 위한 공간 참조 시스템 식별자(SRID)      
	- `ZoneAreaLocation[object]`: 터미널 내 대기열 구역의 지리공간적 또는 지정학적 위치입니다.      
- `CheckpointFacilityOperatorParty[object]`: 공항 내 검색대 운영에 대한 책임이 있는 당사자를 설명하는 정보입니다.  	- `Name[string]`: 검문소 시설에 대한 운영자 파티의 고유 이름입니다.      
- `CheckpointFacilityType[object]`: 공항 내 체크포인트의 분류를 설명하는 정보입니다. 값은 다음과 같습니다: 보안 검색, 세관.  	- `Code[string]`: 체크포인트 시설 유형에 대한 고유 코드입니다.      
	- `Description[string]`: 체크포인트 시설 유형에 대한 설명입니다.      
- `ConcourseFacility[object]`: 서비스를 제공하는 데 사용되는 건물 또는 인프라로서의 공항 청사에 대한 정보입니다.  	- `Identifier[string]`: 중앙홀 시설의 고유 식별자입니다.      
	- `Name[string]`: 중앙 홀 시설의 고유 이름입니다.      
	- `TerminalFacility[object]`: 서비스를 제공하는 데 사용되는 건물 또는 인프라로서의 공항 터미널에 대한 정보입니다.      
- `Description[string]`: 체크포인트 시설에 대한 설명입니다.  - `Identifier[string]`: 검색대 시설의 고유 식별자입니다. 식별자는 공항 내에서 고유해야 합니다.  - `Name[string]`: 검색대 시설의 고유 이름입니다. 이름은 공항 내에서 고유해야 합니다.  - `OperationTimePeriod[object]`: 체크포인트가 운영되는 기간입니다.  	- `ClosingTime[string]`: 체크포인트 시설이 폐쇄된 날짜와 시간입니다. 날짜 시간은 ISO 8601 형식을 준수하는 UTC여야 합니다(예: 2023-04-20T11:54:59Z).      
	- `OpeningTime[string]`: 체크포인트 시설이 개방된 날짜와 시간입니다. 날짜 시간은 ISO 8601 형식을 준수하는 UTC여야 합니다(예: 2023-04-20T11:54:59Z).      
- `id[*]`: 엔티티의 고유 식별자  - `type[string]`: CheckpointFacility와 같아야 합니다.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
필수 속성    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
이 데이터 모델은 국제공항협의회(ACI) ACRIS 데이터 인터페이스 표준의 승객 대기 시간 표준 v1.6.0을 매핑한 것입니다. https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf 에서 확인 가능    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## 속성에 대한 데이터 모델 설명    
알파벳순으로 정렬(자세한 내용을 보려면 클릭)    
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
## 페이로드 예시    
#### CheckpointFacility NGSI-v2 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 체크포인트 시설의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### CheckpointFacility NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 체크포인트 시설의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### CheckpointFacility NGSI-LD 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 체크포인트 시설의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
#### CheckpointFacility NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 체크포인트 시설의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
