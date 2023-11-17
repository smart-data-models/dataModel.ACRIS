<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: AirportElevationUnitOfMeasurement    
==========================================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/AirportElevationUnitOfMeasurement/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Eigenschaft. Die Maßeinheit für die Höhe eines Flughafens über dem Meeresspiegel (FT für Fuß oder M für Meter).**    
Version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `Name[string]`: Der Name der Maßeinheit für die Höhe eines Flughafens über dem Meeresspiegel.  - `id[*]`: Eindeutiger Bezeichner der Entität  - `type[string]`: Sie muss gleich AirportElevationUnitOfMeasurement sein.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Erforderliche Eigenschaften    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Dieses Datenmodell ist ein Mapping des Passenger Wait Times Standard v1.6.0 des ACRIS-Datenschnittstellenstandards des Airports Council International (ACI). Verfügbar unter https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Datenmodell Beschreibung der Eigenschaften    
Alphabetisch sortiert (für Details anklicken)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
AirportElevationUnitOfMeasurement:      
  description: Property. The unit of measure of the height of an Airport above sea level (FT for foot or M for metre).      
  properties:      
    Name:      
      description: The name of the unit of measure for an Airport elevation above sea level.      
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
      description: It must be equal to AirportElevationUnitOfMeasurement.      
      enum:      
        - AirportElevationUnitOfMeasurement      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/AirportElevationUnitOfMeasurement/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/AirportElevationUnitOfMeasurement/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Beispiel-Nutzlasten    
#### AirportElevationUnitOfMeasurement NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für eine AirportElevationUnitOfMeasurement im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirportElevationUnitOfMeasurement:id:PPBL:76921497",  
  "type": "AirportElevationUnitOfMeasurement",  
  "Name": "Meters"  
}  
```  
</details>    
#### AirportElevationUnitOfMeasurement NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel für ein AirportElevationUnitOfMeasurement im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirportElevationUnitOfMeasurement:id:FUWV:30612468",  
  "type": "AirportElevationUnitOfMeasurement",  
  "Name": {  
    "type": "Text",  
    "value": "meters"  
  }  
}  
```  
</details>    
#### AirportElevationUnitOfMeasurement NGSI-LD key-values Beispiel    
Hier ist ein Beispiel für eine AirportElevationUnitOfMeasurement im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirportElevationUnitOfMeasurement:id:PPBL:76921497",  
  "type": "AirportElevationUnitOfMeasurement",  
  "Name": "Meters",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AirportElevationUnitOfMeasurement NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für ein AirportElevationUnitOfMeasurement im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:AirportElevationUnitOfMeasurement:id:FUWV:30612468",  
    "type": "AirportElevationUnitOfMeasurement",  
    "Name": {  
        "type": "Property",  
        "value": "Group policy somebody service growth many. A beat performance clear."  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
