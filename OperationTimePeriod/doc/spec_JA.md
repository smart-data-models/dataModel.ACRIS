<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ操作時間  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/OperationTimePeriod/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**プロパティ。チェックポイントが動作している期間。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティのリスト  

<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。  
- `ClosingTime[string]`: チェックポイント施設が閉鎖された日時。日付時刻はISO 8601フォーマットに準拠したUTCでなければなりません（例：2023-04-20T11:54:59Z）。  - `OpeningTime[string]`: チェックポイント施設がオープンした日時。日付時刻はISO 8601フォーマットに準拠したUTCでなければなりません（例：2023-04-20T11:54:59Z）。  - `id[*]`: エンティティの一意識別子  - `type[string]`: OperationTimePeriodと等しくなければならない。  <!-- /30-PropertiesList -->  
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
## ペイロードの例  
#### OperationTimePeriod NGSI-v2 キー値の例  
JSON-LD形式のOperationTimePeriodのkey-valuesの例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると個々のエンティティのコンテキストデータを返す。  
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
#### 操作時間 NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の OperationTimePeriod の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:OperationTimePeriod:id:BCTN:53140922",  
  "type": "OperationTimePeriod",  
  "ClosingTime": {  
    "type": "date-time",  
    "value": "23:59:02Z"  
  },  
  "OpeningTime": {  
    "type": "date-time",  
    "@value": "00:00:02Z"  
  }  
}  
```  
</details>  
#### OperationTimePeriod NGSI-LD キー値の例  
以下は、JSON-LD形式のOperationTimePeriodをkey-valuesとした例である。options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返す。  
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
#### NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の OperationTimePeriod の例である。これは、オプションを使用しない場合のNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
