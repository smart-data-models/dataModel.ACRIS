<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティキュータイプ    
============<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/QueueType/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**プロパティ。パッセンジャーキューのタイプに関する情報。値は以下の通り：プレチェック、プライベート、エコノミー、プライオリティ、KnownCrewMember.**です。    
バージョン: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `Code[string]`: パッセンジャーキューのタイプを表すユニークなコード。  - `Description[string]`: 旅客キュータイプの説明。  - `id[*]`: エンティティの一意識別子  - `type[string]`: QueueTypeと等しくなければならない。  <!-- /30-PropertiesList -->    
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
QueueType:      
  description: 'Property. Information about the type of a Passenger Queue. Values can be: Pre-Check, Private, Economy, Priority, KnownCrewMember.'      
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
      description: It must be equal to QueueType.      
      enum:      
        - QueueType      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/QueueType/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/QueueType/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### キュータイプ NGSI-v2 キー値の例    
JSON-LD形式のQueueTypeのキー値の例を示します。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:QueueType:id:TFYE:17389668",  
  "type": "QueueType",  
  "Code": "type1",  
  "Description": ""  
}  
```  
</details>    
#### キュータイプ NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のQueueTypeの例です。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:QueueType:id:BCWB:56620437",  
  "type": "QueueType",  
  "Code": {  
    "type": "Text",  
    "value": "type1"  
  },  
  "Description": {  
    "type": "Text",  
    "value": ""  
  }  
}  
```  
</details>    
#### キュータイプ NGSI-LD キー値の例    
JSON-LD形式のQueueTypeのキー値の例です。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると、個々のエンティティのコンテキストデータを返す。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:QueueType:id:TFYE:17389668",  
  "type": "QueueType",  
  "Code": "type1",  
  "Description": "",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### キュータイプ NGSI-LD 正規化 例    
以下は、正規化されたJSON-LD形式のQueueTypeの例です。これは、オプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:QueueType:id:BCWB:56620437",  
    "type": "QueueType",  
    "Code": {  
        "type": "Property",  
        "value": "type1"  
    },  
    "Description": {  
        "type": "Property",  
        "value": ""  
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
