<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 공항 위치  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/AirportLocation/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **속성. 공항의 지리공간적 또는 지정학적 위치**입니다.  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `Latitude[number]`: 공항의 위도 좌표입니다.  - `Longitude[number]`: 공항의 경도에 대한 좌표입니다.  - `Name[string]`: 공항 위치의 고유 이름입니다.  - `Srid[number]`: 공간 좌표계 정의를 식별하기 위한 공간 참조 시스템 식별자(SRID)입니다.  - `id[*]`: 엔티티의 고유 식별자  - `type[string]`: 이 값은 AirportLocation과 같아야 합니다.  <!-- /30-PropertiesList -->  
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
AirportLocation:    
  description: Property. The geospatial or geopolitical location of an Airport.    
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
      description: It must be equal to AirportLocation.    
      enum:    
        - AirportLocation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/AirportLocation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/AirportLocation/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 페이로드 예시  
#### AirportLocation NGSI-v2 키-값 예시  
다음은 JSON-LD 형식의 AirportLocation을 키값으로 사용하는 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirportLocation:id:DSZW:70034143",  
  "type": "AirportLocation",  
  "Latitude": 40.41,  
  "Longitude": 3.708,  
  "Name": "Madrid",  
  "Srid": 4326  
}  
```  
</details>  
#### AirportLocation NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 AirportLocation의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AirportLocation:id:LCGI:88743541",  
    "type": "AirportLocation",  
    "Latitude": {  
        "type": "Number",  
        "value": 40.41  
    },  
    "Longitude": {  
        "type": "Number",  
        "value": 3.702  
    },  
    "Name": {  
        "type": "Number",  
        "value": "Madrid"  
    },  
    "Srid": {  
        "type": "Number",  
        "value": 4326  
    }  
}  
```  
</details>  
#### AirportLocation NGSI-LD 키-값 예시  
다음은 JSON-LD 형식의 AirportLocation을 키 값으로 사용하는 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:AirportLocation:id:DSZW:70034143",  
  "type": "AirportLocation",  
  "Latitude": 40.42,  
  "Longitude": 3.704,  
  "Name": "Madrid",  
  "Srid": 4326,  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### AirportLocation NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 AirportLocation 예제입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AirportLocation:id:LCGI:88743541",  
    "type": "AirportLocation",  
    "Latitude": {  
        "type": "Property",  
        "value": 3.8  
    },  
    "Longitude": {  
        "type": "control",  
        "value": 1.6  
    },  
    "Name": {  
        "type": "Property",  
        "value": ""  
    },  
    "Srid": {  
        "type": "Property",  
        "value": 4326  
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
