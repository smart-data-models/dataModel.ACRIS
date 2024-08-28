<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: PassengerQueue  
===================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/PassengerQueue/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **프로퍼티. 승객 대기열에 대한 정보입니다. 보안 검색대 통과를 위해 대기 중인 사람들의 줄입니다.  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `CheckpointFacility[object]`: 서비스 제공에 사용되는 공항 내 보안검색대에 대한 정보입니다. 체크포인트 시설은 고객과 승객이 여정의 다음 단계로 이동하기 전에 처리, 서비스 또는 검사가 필요한 모든 시설입니다.  	- `CheckpointAreaLocation[object]`: 체크포인트의 지리공간적 또는 지정학적 위치입니다.    
	- `CheckpointFacilityOperatorParty[object]`: 공항 내 검색대 운영에 대한 책임이 있는 당사자를 설명하는 정보입니다.    
	- `CheckpointFacilityType[object]`: 공항 내 검색대 분류를 설명하는 정보입니다. 값은 다음과 같습니다: 보안 검색, 세관.    
	- `ConcourseFacility[object]`: 서비스를 제공하는 데 사용되는 건물 또는 인프라로서의 공항 청사에 대한 정보입니다.    
	- `Description[string]`: 체크포인트 시설에 대한 설명입니다.    
	- `Identifier[string]`: 체크포인트 시설의 고유 식별자입니다. 식별자는 공항 내에서 고유해야 합니다.    
	- `Name[string]`: 검색대 시설의 고유 이름입니다. 이름은 공항 내에서 고유해야 합니다.    
	- `OperationTimePeriod[object]`: 체크포인트가 운영되는 기간입니다.    
- `Identifier[string]`: 승객 대기열의 고유 식별자입니다. 식별자는 공항 내에서 고유해야 합니다.  - `Name[string]`: 승객 대기열의 이름입니다. 이름은 공항 내에서 고유해야 합니다.  - `PassengerProcess[object]`: 승객 파티 절차에 대한 정보.  	- `Name[string]`: 승객 프로세스의 고유 이름입니다.    
	- `PassengerProcessType[object]`: 승객 파티 프로세스 유형에 대한 정보입니다.    
- `QueueLocation[object]`: 승객 대기열의 지리공간적 또는 지정학적 위치입니다.  	- `Name[string]`: 대기열 위치의 고유 이름입니다.    
- `QueueStatus[object]`: 승객 대기열의 상태에 대한 정보입니다. 값은 다음과 같습니다: 열림, 닫힘.  	- `Name[string]`: 승객 대기열 상태의 고유 이름입니다.    
- `QueueType[object]`: 승객 대기열의 유형에 대한 정보입니다. 값은 다음과 같습니다: 사전 체크인, 개인, 이코노미, 우선순위, 알려진 승무원.  	- `Code[string]`: 승객 대기열 유형에 대한 고유 코드입니다.    
	- `Description[string]`: 승객 대기열 유형에 대한 설명입니다.    
- `id[*]`: 엔티티의 고유 식별자  - `type[string]`: PassengerQueue와 같아야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
이 데이터 모델은 국제공항협의회(ACI) ACRIS 데이터 인터페이스 표준의 승객 대기 시간 표준 v1.6.0을 매핑한 것입니다. https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
PassengerQueue:    
  description: Property. Information about the Passenger Party Queue. A line of people waiting to pass through the security checkpoint process.    
  properties:    
    CheckpointFacility:    
      description: 'Information about a Checkpoint in an Airport used to provide services. A Checkpoint facility is any facility where customers and passengers turn up and need to be processed, serviced or screened before proceeding to the next stage of their journey. '    
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
              type: number    
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
                          type: integer    
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
      type: object    
      x-ngsi:    
        type: Property    
    Identifier:    
      description: Unique identifier for the Passenger Queue. The identifier should be unique within an Airport.    
      type: string    
      x-ngsi:    
        type: Property    
    Name:    
      description: Name of the Passenger Queue. The name should be unique within an Airport.    
      type: string    
      x-ngsi:    
        type: Property    
    PassengerProcess:    
      description: Information about the Passenger Party Process.    
      properties:    
        Name:    
          description: Unique name for the Passenger Process.    
          type: string    
          x-ngsi:    
            type: Property    
        PassengerProcessType:    
          description: Information about the type of Passenger Party Process.    
          properties:    
            Code:    
              description: Unique code for the type of Passenger Party Process.    
              type: string    
              x-ngsi:    
                type: Property    
            Description:    
              description: Description of the type of Passenger Party Process.    
              type: string    
              x-ngsi:    
                type: Property    
          type: object    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    QueueLocation:    
      description: The geospatial or geopolitical location of a Passenger Queue.    
      properties:    
        Name:    
          description: Unique name for the Queue Location.    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    QueueStatus:    
      description: 'Information about the status of a Passenger Queue. Values can be: Open, Closed.'    
      properties:    
        Name:    
          description: Unique name for the status of the Passenger Queue.    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    QueueType:    
      description: 'Information about the type of a Passenger Queue. Values can be: Pre-Check, Private, Economy, Priority, KnownCrewMember.'    
      properties:    
        Code:    
          description: Unique code for the type of Passenger Queue.    
          type: string    
          x-ngsi:    
            type: Property    
        Description:    
          description: Description of the type of Passenger Queue.    
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
      description: It must be equal to PassengerQueue.    
      enum:    
        - PassengerQueue    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/PassengerQueue/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/PassengerQueue/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### PassengerQueue NGSI-v2 키 값 예제  
다음은 키 값으로 JSON-LD 형식의 PassengerQueue의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:QueueMeasurement:id:IEQX:79193255",  
  "type": "PassengerQueue",  
  "Identifier": "1",  
  "Name": "1",  
  "CheckpointFacility": {  
    "Description": "",  
    "Identifier": "1bdaec90-7a42-11e7-bb31-be2e44b06b34",  
    "Name": "Checkpoint B",  
    "CheckpointAreaLocation": {  
      "Latitude": 43.02,  
      "longitude": 3.08  
    },  
    "CheckpointFacilityOperatorParty": {  
      "Name": ""  
    },  
    "CheckpointFacilityType": {  
      "Code": "",  
      "Description": ""  
    },  
    "ConcourseFacility": {  
      "Identifier": "BA/B",  
      "Name": "Boarding Area B",  
      "TerminalFacility": {  
        "Identifier": "T1",  
        "Name": "Terminal 1",  
        "AirportFacility": {  
          "IataCode": "SFO",  
          "IcaoCode": "KSFO",  
          "Name": "San Francisco InternationalAirport"  
        }  
      }  
    },  
    "OperationTimePeriod": {  
      "ClosingTime": "",  
      "OpeningTime": ""  
    }  
  },  
  "PassengerProcess": {  
    "Name": "",  
    "PassengerProcessType": {  
      "Code": "",  
      "Description": ""  
    }  
  },  
  "QueueLocation": {  
    "Name": ""  
  },  
  "QueueStatus": {  
    "Name": ""  
  },  
  "QueueType": {  
    "Code": "",  
    "Description": ""  
  }  
}  
```  
</details>  
#### PassengerQueue NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 PassengerQueue 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PassengerQueue:id:CFYG:74194684",  
  "type": "PassengerQueue",  
  "Identifier": {  
    "type": "Text",  
    "value": "1"  
  },  
  "Name": {  
    "type": "Text",  
    "value": "1"  
  },  
  "CheckpointFacility": {  
    "type": "StructuredValue",  
    "value": {  
      "Description": "",  
      "Identifier": "1bdaec90-7a42-11e7-bb31-be2e44b06b34",  
      "Name": "Checkpoint B",  
      "CheckpointAreaLocation": {  
        "Latitude": 40.42,  
        "Longitude": 3.708,  
        "Name": "",  
        "Srid": 0,  
        "AirportElevation": {  
          "Name": "",  
          "Value": 3.6,  
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
              "Name": "Barajas",  
              "Srid": 0  
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
        "Identifier": "BA/B",  
        "Name": "Boarding area B",  
        "TerminalFacility": {  
          "Identifier": "T1",  
          "Name": "Terminal 1",  
          "AirportFacility": {  
            "IataCode": "SFO",  
            "IcaoCode": "KSFO",  
            "Name": "San Francisco Internationl Airport"  
          }  
        }  
      },  
      "OperationTimePeriod": {  
        "ClosingTime": "",  
        "OpeningTime": ""  
      }  
    }  
  },  
  "PassengerProcess": {  
    "type": "StructuredValue",  
    "value": {  
      "Name": "",  
      "PassengerProcessType": {  
        "Code": "",  
        "Description": ""  
      }  
    }  
  },  
  "QueueLocation": {  
    "type": "StructuredValue",  
    "value": {  
      "Name": ""  
    }  
  },  
  "QueueStatus": {  
    "type": "StructuredValue",  
    "value": {  
      "Name": ""  
    }  
  },  
  "QueueType": {  
    "type": "StructuredValue",  
    "value": {  
      "Code": "",  
      "Description": ""  
    }  
  }  
}  
```  
</details>  
#### PassengerQueue NGSI-LD 키 값 예제  
다음은 키 값으로 JSON-LD 형식의 PassengerQueue의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:PassengerQueue:id:DLSH:49883369",  
  "type": "PassengerQueue",  
  "Identifier": "1",  
  "Name": "1",  
  "CheckpointFacility": {  
    "Description": "",  
    "Identifier": "1bdaec90-7a42-11e7-bb31-be2e44b06b34",  
    "Name": "Checkpoint B",  
    "CheckpointAreaLocation": {  
      "Latitude": 40.42,  
      "Longitude": 3.08,  
      "Name": "",  
      "$rid": 0  
    },  
    "CheckpointFacilityOperatorParty": {  
      "Name": ""  
    },  
    "CheckpointFacilityType": {  
      "Code": "",  
      "Description": ""  
    },  
    "ConcourseFacility": {  
      "Identifier": "BA/B",  
      "Name": "Boarding Area B",  
      "TerminalFacility": {  
        "Identifier": "T1",  
        "Name": "Terminal 1",  
        "AirportFacility": {  
          "IataCode": "SFO",  
          "IcaoCode": "KSFO",  
          "Name": "San Francisco International Airport"  
        }  
      }  
    },  
    "OperationTimePeriod": {  
      "ClosingTime": "",  
      "OpeningTime": ""  
    }  
  },  
  "PassengerProcess": {  
    "Name": "",  
    "PassengerProcessType": {  
      "Code": "",  
      "Description": ""  
    }  
  },  
  "QueueLocation": {  
    "Name": ""  
  },  
  "QueueStatus": {  
    "Name": ""  
  },  
  "QueueType": {  
    "Code": "",  
    "Description": ""  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### PassengerQueue NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 PassengerQueue 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PassengerQueue:id:CFYG:74194684",  
    "type": "PassengerQueue",  
    "Identifier": {  
        "type": "Property",  
        "value": "1"  
    },  
    "Name": {  
        "type": "Property",  
        "value": "1"  
    },  
    "CheckpointFacility": {  
        "type": "Property",  
        "value": {  
            "Description": "",  
            "Identifier": "1bdaec90-7a42-11e7-bb31-be2e44b06b34",  
            "Name": "Checkpoint B",  
            "CheckpointAreaLocation": {  
                "Latitude": 40.42,  
                "Longitude": 3.708,  
                "Name": "",  
                "Srid": 0,  
                "AirportElevation": {  
                    "Name": "",  
                    "Value": 3.6,  
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
                            "Name": "Barajas",  
                            "Srid": 0  
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
                "Identifier": "BA/B",  
                "Name": "Boarding area B",  
                "TerminalFacility": {  
                    "Identifier": "T1",  
                    "Name": "Terminal 1",  
                    "AirportFacility": {  
                        "IataCode": "SFO",  
                        "IcaoCode": "KSFO",  
                        "Name": "San Francisco Internationl Airport"  
                    }  
                }  
            },  
            "OperationTimePeriod": {  
                "ClosingTime": "",  
                "OpeningTime": ""  
            }  
        }  
    },  
    "PassengerProcess": {  
        "type": "Property",  
        "value": {  
            "Name": "",  
            "PassengerProcessType": {  
                "Code": "",  
                "Description": ""  
            }  
        }  
    },  
    "QueueLocation": {  
        "type": "Property",  
        "value": {  
            "Name": ""  
        }  
    },  
    "QueueStatus": {  
        "type": "Property",  
        "value": {  
            "Name": ""  
        }  
    },  
    "QueueType": {  
        "type": "Property",  
        "value": {  
            "Code": "",  
            "Description": ""  
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
규모 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
