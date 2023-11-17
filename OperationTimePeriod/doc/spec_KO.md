<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 운영 시간 기간    
=============<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/OperationTimePeriod/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **속성. 체크포인트가 운영되는 기간입니다.    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `ClosingTime[string]`: 체크포인트 시설이 폐쇄된 날짜와 시간입니다. 날짜 시간은 ISO 8601 형식을 준수하는 UTC여야 합니다(예: 2023-04-20T11:54:59Z).  - `OpeningTime[string]`: 체크포인트 시설이 개방된 날짜와 시간입니다. 날짜 시간은 ISO 8601 형식을 준수하는 UTC여야 합니다(예: 2023-04-20T11:54:59Z).  - `id[*]`: 엔티티의 고유 식별자  - `type[string]`: 이 값은 OperationTimePeriod와 같아야 합니다.  <!-- /30-PropertiesList -->    
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
OperationTimePeriod:      
  description: Property. The time period over which the Checkpoint is operating.      
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
      description: It must be equal to OperationTimePeriod.      
      enum:      
        - OperationTimePeriod      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/OperationTimePeriod/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/OperationTimePeriod/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### OperationTimePeriod NGSI-v2 키-값 예제    
다음은 키 값으로 JSON-LD 형식의 OperationTimePeriod의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OperationTimePeriod:id:XCIN:24494142",  
  "type": "OperationTimePeriod",  
  "ClosingTime": "23:59:02Z",  
  "OpeningTime": "00:00:00Z"  
}  
```  
</details>    
#### OperationTimePeriod NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 OperationTimePeriod의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OperationTimePeriod:id:BCTN:53140922",  
  "type": "OperationTimePeriod",  
  "ClosingTime": {  
    "type": "DateTime",  
    "value": "23:59:02Z"  
  },  
  "OpeningTime": {  
    "type": "DateTime",  
    "value": "00:00:02Z"  
  }  
}  
```  
</details>    
#### OperationTimePeriod NGSI-LD 키-값 예제    
다음은 키 값으로 JSON-LD 형식의 OperationTimePeriod의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OperationTimePeriod:id:XCIN:24494142",  
  "type": "OperationTimePeriod",  
  "ClosingTime": "23:59:02Z",  
  "OpeningTime": "00:00:00Z",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### OperationTimePiod NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 OperationTimePeriod의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OperationTimePeriod:id:BCTN:53140922",  
  "type": "OperationTimePeriod",  
  "ClosingTime": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "23:59:02Z"  
    }  
  },  
  "OpeningTime": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "00:00:02Z"  
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
