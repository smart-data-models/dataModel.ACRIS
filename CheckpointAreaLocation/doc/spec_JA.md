<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティチェックポイント・エリア・ロケーション    
=========================<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/CheckpointAreaLocation/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**プロパティ。チェックポイントの地理空間的または地政学的位置。    
バージョン: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `AirportElevation[object]`: 空港の海面からの高さ。  	- `AirportElevationUnitOfMeasurement[object]`: 空港の海抜の高さを表す単位（FTはフィート、Mはメートル）。      
	- `Name[string]`: 空港の海抜高度の名称。      
	- `Value[number]`: 空港の海抜値。      
- `Latitude[number]`: チェックポイントエリアの位置の緯度の座標。  - `Longitude[number]`: チェックポイントエリアの位置の経度の座標。  - `Name[string]`: チェックポイント・エリア・ロケーションの地理空間的または地政学的位置の固有名。  - `Srid[number]`: 空間座標系の定義を識別するための空間参照系識別子 （Spatial Reference System Identifier：SRID）。  - `ZoneAreaLocation[object]`: ターミナル内のキューイングゾーンの地理的または地政学的な位置。  	- `Name[string]`: ゾーン・エリア・ロケーションの固有名。      
	- `TerminalAreaLocation[object]`: 空港ターミナルビルの地理空間的または地政学的位置。      
- `id[*]`: エンティティの一意識別子  - `type[string]`: CheckpointAreaLocation と等しくなければならない。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
このデータモデルは、国際空港評議会（ACRIS）データインタフェース標準の旅客待ち時間標準v1.6.0をマッピングしたものである。https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
CheckpointAreaLocation:      
  description: Property. The geospatial or geopolitical location of a Checkpoint.      
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
      description: It must be equal to CheckpointAreaLocation.      
      enum:      
        - CheckpointAreaLocation      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/CheckpointAreaLocation/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/CheckpointAreaLocation/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### CheckpointAreaLocation NGSI-v2 キー値の例    
JSON-LD形式のCheckpointAreaLocationのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CheckpointAreaLocation:id:BLBC:14665623",  
  "type": "CheckpointAreaLocation",  
  "Latitude": 40.42,  
  "Longitude": 3.708,  
  "Name": "As since dream public analysis clear one. Federal skill term court.",  
  "Srid": 4326,  
  "AirportElevation": {  
    "Name": "",  
    "Value": 777.7,  
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
        "Srid": 4326  
      }  
    }  
  }  
}  
```  
</details>    
#### CheckpointAreaLocation NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のCheckpointAreaLocationの例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CheckpointAreaLocation:id:KSRW:92816613",  
  "type": "CheckpointAreaLocation",  
  "Latitude": {  
    "type": "Number",  
    "value": 2.4  
  },  
  "Longitude": {  
    "type": "Number",  
    "value": 5.3  
  },  
  "Name": {  
    "type": "Text",  
    "value": ""  
  },  
  "Srid": {  
    "type": "Number",  
    "value": 4326  
  },  
  "AirportElevation": {  
    "type": "StructuredValue",  
    "value": {  
      "Name": "",  
      "Value": 487.8,  
      "AirportElevationUnitOfMeasurement": {  
        "Name": "Meters"  
      }  
    }  
  },  
  "ZoneAreaLocation": {  
    "type": "StructuredValue",  
    "value": {  
      "Name": "",  
      "TerminalAreaLocation": {  
        "Name": "Madrid",  
        "AirportLocation": {  
          "Latitude": 40.41,  
          "Longitude": 3.7,  
          "Name": "",  
          "Srid": 662  
        }  
      }  
    }  
  }  
}  
```  
</details>    
#### CheckpointAreaLocation NGSI-LD キー値の例    
以下はCheckpointAreaLocationをJSON-LD形式でkey-valuesとした例である。これはNGSI-LDと互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CheckpointAreaLocation:id:BLBC:14665623",  
  "type": "CheckpointAreaLocation",  
  "Latitude": 40.42,  
  "Longitude": 3.708,  
  "Name": "As since dream public analysis clear one. Federal skill term court.",  
  "Srid": 4326,  
  "AirportElevation": {  
    "Name": "",  
    "Value": 777.7,  
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
        "Srid": 4326  
      }  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### チェックポイント・エリア・ロケーション NGSI-LD 正規化例    
以下は、正規化された JSON-LD 形式の CheckpointAreaLocation の例である。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:CheckpointAreaLocation:id:KSRW:92816613",  
    "type": "CheckpointAreaLocation",  
    "Latitude": {  
        "type": "Property",  
        "value": 40.42  
    },  
    "Longitude": {  
        "type": "Property",  
        "value": 3.708  
    },  
    "Name": {  
        "type": "Property",  
        "value": "Madrid"  
    },  
    "Srid": {  
        "type": "Property",  
        "value": 4326  
    },  
    "AirportElevation": {  
        "type": "Property",  
        "value": {  
            "Name": "",  
            "Value": 487.8,  
            "AirportElevationUnitOfMeasurement": {  
                "Name": "Meters"  
            }  
        }  
    },  
    "ZoneAreaLocation": {  
        "type": "Property",  
        "value": {  
            "Name": "",  
            "TerminalAreaLocation": {  
                "Name": "Madrid",  
                "AirportLocation": {  
                    "Latitude": 40.42,  
                    "Longitude": 3.708,  
                    "Name": "",  
                    "Srid": 4326  
                }  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
