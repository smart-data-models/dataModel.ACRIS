<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
엔티티: 승객 프로세스    
============<!-- /10-Header -->    
<!-- 15-License -->    
[오픈 라이선스](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/PassengerProcess/LICENSE.md)    
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
글로벌 설명: **속성. 승객 파티 프로세스에 대한 정보입니다.**    
버전: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## 속성 목록    
<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.    
- `Name[string]`: 승객 프로세스의 고유 이름입니다.  - `PassengerProcessType[object]`: 승객 파티 프로세스 유형에 대한 정보입니다.  	- `Code[string]`: 승객 파티 프로세스 유형에 대한 고유 코드입니다.      
	- `Description[string]`: 승객 파티 프로세스 유형에 대한 설명입니다.      
- `id[*]`: 엔티티의 고유 식별자  - `type[string]`: PassengerProcess와 같아야 합니다.  <!-- /30-PropertiesList -->    
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
PassengerProcess:      
  description: Property. Information about the Passenger Party Process.      
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
      description: It must be equal to PassengerProcess.      
      enum:      
        - PassengerProcess      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/PassengerProcess/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/PassengerProcess/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## 페이로드 예시    
#### PassengerProcess NGSI-v2 키-값 예시    
다음은 키 값으로 JSON-LD 형식의 PassengerProcess의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PassengerProcess:id:HARF:66129232",  
  "type": "PassengerProcess",  
  "Name": "",  
  "PassengerProcessType": {  
    "Code": "code1",  
    "Description": ""  
  }  
}  
```  
</details>    
#### PassengerProcess NGSI-v2 정규화 예제    
다음은 정규화된 JSON-LD 형식의 PassengerProcess의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PassengerProcess:id:YOUE:15643415",  
  "type": "PassengerProcess",  
  "Name": {  
    "type": "Text",  
    "value": ""  
  },  
  "PassengerProcessType": {  
    "type": "StructuredValue",  
    "value": {  
      "Code": "code1",  
      "Description": ""  
    }  
  }  
}  
```  
</details>    
#### PassengerProcess NGSI-LD 키-값 예시    
다음은 키 값으로 JSON-LD 형식의 PassengerProcess의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:PassengerProcess:id:HARF:66129232",  
  "type": "PassengerProcess",  
  "Name": "",  
  "PassengerProcessType": {  
    "Code": "code1",  
    "Description": ""  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### PassengerProcess NGSI-LD 정규화 예제    
다음은 정규화된 JSON-LD 형식의 PassengerProcess의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:PassengerProcess:id:YOUE:15643415",  
    "type": "PassengerProcess",  
    "Name": {  
        "type": "Property",  
        "value": ""  
    },  
    "PassengerProcessType": {  
        "type": "Property",  
        "value": {  
            "Code": "code1",  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
