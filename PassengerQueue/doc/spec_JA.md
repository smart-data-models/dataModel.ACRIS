<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティPassengerQueue    
====================<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/PassengerQueue/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**プロパティ。Passenger Party Queueに関する情報。保安検査場通過待ちの列。    
バージョン: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `CheckpointFacility[object]`: サービスを提供するために使用される空港内のチェックポイントに関する情報。チェックポイント施設とは、顧客や旅客が出頭し、次の旅程に進む前に手続きやサービス、審査を受ける必要がある施設を指します。  	- `CheckpointAreaLocation[object]`: チェックポイントの地理空間的または地政学的位置。      
	- `CheckpointFacilityOperatorParty[object]`: 空港内のチェックポイントの運営に責任を持つ当事者について説明する情報。      
	- `CheckpointFacilityType[object]`: 空港内のチェックポイントの分類を表す情報。値は以下の通り：保安検査、税関。      
	- `ConcourseFacility[object]`: サービスを提供するために使用される建物やインフラとしての空港コンコースに関する情報。      
	- `Description[string]`: チェックポイント施設の説明      
	- `Identifier[string]`: チェックポイント施設の固有の識別子。この識別子は空港内で一意でなければならない。      
	- `Name[string]`: チェックポイント施設の固有の名称。空港内でユニークな名称でなければならない。      
	- `OperationTimePeriod[object]`: チェックポイントが作動している期間。      
- `Identifier[string]`: 旅客キュー用の一意の識別子。この識別子は空港内で一意でなければなりません。  - `Name[string]`: 旅客キューの名前。空港内でユニークな名前である必要があります。  - `PassengerProcess[object]`: パッセンジャー・パーティー・プロセスに関する情報。  	- `Name[string]`: パッセンジャー・プロセスのユニークな名前。      
	- `PassengerProcessType[object]`: パッセンジャー・パーティ・プロセスのタイプに関する情報。      
- `QueueLocation[object]`: 旅客キュー（Passenger Queue）の地理的または地政学的な位置。  	- `Name[string]`: キューロケーションの固有名。      
- `QueueStatus[object]`: 旅客キューのステータスに関する情報。値は次のとおりです：オープン、クローズ。  	- `Name[string]`: パッセンジャーキューのステータスを表すユニークな名前。      
- `QueueType[object]`: 旅客キューのタイプに関する情報。値は以下のとおりです：Pre-Check、Private、Economy、Priority、KnownCrewMember。  	- `Code[string]`: パッセンジャーキューのタイプを表すユニークなコード。      
	- `Description[string]`: 旅客キュータイプの説明。      
- `id[*]`: エンティティの一意識別子  - `type[string]`: PassengerQueueと等しくなければならない。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
このデータモデルは、国際空港評議会（ACRIS）データインターフェース標準の旅客待ち時間標準v1.6.0をマッピングしたものである。https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
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
                        Longitude:      
                        Name:      
                        Srid:      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
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
## ペイロードの例    
#### PassengerQueue NGSI-v2 キー値の例    
JSON-LD形式のPassengerQueueのkey-valuesの例です。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:QueueMeasurement:id:IEQX:79193255",  
  "type": "PassengerQueue",  
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
  }  
}  
```  
</details>    
#### PassengerQueue NGSI-v2 正規化例    
正規化されたJSON-LD形式のPassengerQueueの例です。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
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
#### PassengerQueue NGSI-LD キー値の例    
JSON-LD形式のPassengerQueueのkey-valuesの例です。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。    
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
#### PassengerQueue NGSI-LD 正規化例    
正規化されたJSON-LD形式のPassengerQueueの例です。これは、オプションを使用しない場合はNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
