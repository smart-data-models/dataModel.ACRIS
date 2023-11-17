<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: QueueMeasurement    
=====================<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/QueueMeasurement/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **속성. 승객 대기열의 특정 측정값(관측값)에 대한 정보**입니다.    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `MeasurementDevice[object]`: 측정(관찰)에 사용된 장치(장비)에 대한 정보입니다.  	- `MeasurementDeviceLocation[object]`: 측정 장치의 지리적 공간 또는 지정학적 위치.      
	- `Name[string]`: 측정 장치의 고유 이름입니다.      
- `MeasurementTimePeriod[object]`: 측정이 수행되는 기간입니다.  	- `EndTime[string]`: 측정이 수행된 기간이 끝나는 날짜와 시간입니다. 날짜 시간은 ISO 8601 형식을 준수하는 UTC여야 합니다(예: 2023-04-20T11:54:59Z).      
- `Occupancy[number]`: 대기열에 있는 사람 수입니다.  측정 단위는 사람 수입니다. 이 메트릭은 5분마다 업데이트됩니다.  - `PassengerQueue[object]`: 승객 파티 대기열에 대한 정보입니다. 보안 검색대 통과를 위해 대기 중인 사람들의 줄입니다.  	- `CheckpointFacility[object]`: 서비스 제공에 사용되는 공항 내 보안 검색대에 대한 정보입니다. 체크포인트 시설은 고객과 승객이 도착하여 다음 단계로 이동하기 전에 처리, 서비스 또는 검색을 받아야 하는 모든 시설입니다.      
	- `Identifier[string]`: 승객 대기열의 고유 식별자입니다. 식별자는 공항 내에서 고유해야 합니다.      
	- `Name[string]`: 승객 대기열의 이름입니다. 이름은 공항 내에서 고유해야 합니다.      
	- `PassengerProcess[object]`: 승객 파티 절차에 대한 정보.      
	- `QueueLocation[object]`: 승객 대기열의 지리공간적 또는 지정학적 위치입니다.      
	- `QueueStatus[object]`: 승객 대기열의 상태에 대한 정보입니다. 값은 다음과 같습니다: 열림, 닫힘.      
	- `QueueType[object]`: 승객 대기열의 유형에 대한 정보입니다. 값은 다음과 같습니다: 사전 체크인, 개인, 이코노미, 우선순위, KnownCrewMember.      
- `ProjectedWaitTime[number]`: 대기열에 입장하는 사람이 대기할 것으로 예상되는 예상 시간입니다. 측정 단위는 초입니다. 예상 시간은 5분마다 업데이트해야 합니다.  - `Throughput[number]`: 지난 한 시간 동안 처리한 평균 승객 수입니다. 측정 단위는 시간당 승객 수입니다. 이 메트릭은 5분마다 업데이트됩니다.  - `WaitTime[number]`: 대기열에서 나가는 사람이 대기열에서 대기한 시간입니다. 측정 단위는 초입니다. 이 금액은 지난 5분 동안 대기열에서 퇴장하는 사람들이 대기열을 빠져나가는 데 걸린 평균 시간(초)을 나타냅니다. 이 금액은 5분마다 업데이트해야 합니다.  - `id[*]`: 엔티티의 고유 식별자  - `type[string]`: 이 값은 QueueMeasurement와 같아야 합니다.  <!-- /30-PropertiesList -->    
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
QueueMeasurement:      
  description: Property. Information about the measurements (observations) of particular Measures of a Passenger Queue.      
  properties:      
    MeasurementDevice:      
      description: Information about the device (equipment) used to take measurements (observations).      
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
      type: object      
      x-ngsi:      
        type: Property      
    MeasurementTimePeriod:      
      description: The time period over which a Measurement is taken.      
      properties:      
        EndTime:      
          description: 'The date and time at the end of the time period over which a Measurement is taken. Date time should be UTC, compliant with ISO 8601 format (e.g. 2023-04-20T11:54:59Z)'      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    Occupancy:      
      description: The count of people in the queue.  The unit of measure is number of people. This metric is updated every five minutes.      
      type: number      
      x-ngsi:      
        type: Property      
    PassengerQueue:      
      description: Information about the Passenger Party Queue. A line of people waiting to pass through the security checkpoint process.      
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
                        Name:      
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
                        IcaoCode:      
                        Name:      
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
      type: object      
      x-ngsi:      
        type: Property      
    ProjectedWaitTime:      
      description: The estimated time that a person entering the queue can expect to wait. The unit of measure is seconds. Estimates are required to be updated every five minutes.      
      type: number      
      x-ngsi:      
        type: Property      
    Throughput:      
      description: The average number of passengers processed over the past hour. The unit of measure is passengers per hour. This metric is updated every five minutes.      
      type: number      
      x-ngsi:      
        type: Property      
    WaitTime:      
      description: The duration that a person exiting the queue has experienced. The unit of measure is seconds. The amount represents the average number of seconds experienced by people exiting the queue in the last five minutes. The amounts are required to be updated every five minutes.      
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
      description: It must be equal to QueueMeasurement.      
      enum:      
        - QueueMeasurement      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/QueueMeasurement/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/QueueMeasurement/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### QueueMeasurement NGSI-v2 키-값 예제    
다음은 키-값으로 JSON-LD 형식의 QueueMeasurement의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:QueueMeasurement:id:IEQX:79193255",  
  "type": "QueueMeasurement",  
  "Occupancy": 58,  
  "ProjectedWaitTime": 544.4,  
  "Throughput": 384,  
  "WaitTime": 645.9,  
  "MeasurementDevice": {  
    "Name": "",  
    "MeasurementDeviceLocation": {  
      "Name": ""  
    }  
  },  
  "MeasurementTimePeriod": {  
    "EndTime": "2023-03-22T18:59:02Z"  
  },  
  "PassengerQueue": {  
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
}  
```  
</details>    
#### QueueMeasurement NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 QueueMeasurement의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:QueueMeasurement:id:IEQX:79193255",  
  "type": "QueueMeasurement",  
  "Occupancy": {  
    "type": "Number",  
    "value": 58  
  },  
  "ProjectedWaitTime": {  
    "type": "Number",  
    "value": 544.4  
  },  
  "Throughput": {  
    "type": "Number",  
    "value": 384  
  },  
  "WaitTime": {  
    "type": "Number",  
    "value": 645.9  
  },  
  "MeasurementDevice": {  
    "type": "StructuredValue",  
    "value": {  
      "Name": "",  
      "MeasurementDeviceLocation": {  
        "Name": ""  
      }  
    }  
  },  
  "MeasurementTimePeriod": {  
    "type": "StructuredValue",  
    "value": {  
      "EndTime": "2023-03-22T18:59:02Z"  
    }  
  },  
  "PassengerQueue": {  
    "type": "StructuredValue",  
    "value": {  
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
  }  
}  
```  
</details>    
#### QueueMeasurement NGSI-LD 키-값 예제    
다음은 키 값으로 JSON-LD 형식의 QueueMeasurement의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:QueueMeasurement:id:IEQX:79193255",  
  "type": "QueueMeasurement",  
  "Occupancy": 58,  
  "ProjectedWaitTime": 544.4,  
  "Throughput": 384,  
  "WaitTime": 645.9,  
  "MeasurementDevice": {  
    "Name": "",  
    "MeasurementDeviceLocation": {  
      "Name": ""  
    }  
  },  
  "MeasurementTimePeriod": {  
    "EndTime": "2023-03-22T18:59:02Z"  
  },  
  "PassengerQueue": {  
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
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### QueueMeasurement NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 QueueMeasurement의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:QueueMeasurement:id:IEQX:79193255",  
  "type": "QueueMeasurement",  
  "Occupancy": {  
    "type": "Property",  
    "value": 58  
  },  
  "ProjectedWaitTime": {  
    "type": "Property",  
    "value": 544.4  
  },  
  "Throughput": {  
    "type": "Property",  
    "value": 384  
  },  
  "WaitTime": {  
    "type": "Property",  
    "value": 645.9  
  },  
  "MeasurementDevice": {  
    "type": "Property",  
    "value": {  
      "Name": "",  
      "MeasurementDeviceLocation": {  
        "Name": ""  
      }  
    }  
  },  
  "MeasurementTimePeriod": {  
    "type": "Property",  
    "value": {  
      "EndTime": "2023-03-22T18:59:02Z"  
    }  
  },  
  "PassengerQueue": {  
    "type": "Property",  
    "value": {  
      "Identifier": "1",  
      "Name": "1",  
      "CheckpointFacility": {  
        "Description": "",  
        "Identifier": "1bdaec90-7a42-11e7-bb31-be2e44b06b34",  
        "Name": "Checkpoint B",  
        "CheckpointAreaLocation": "",  
        "CheckpointFacilityOperatorParty": "",  
        "CheckpointFacilityType": "",  
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
