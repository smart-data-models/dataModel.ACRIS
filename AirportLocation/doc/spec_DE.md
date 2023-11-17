<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entität: FlughafenStandort    
==========================<!-- /10-Header -->    
<!-- 15-License -->    
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/AirportLocation/LICENSE.md)    
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Globale Beschreibung: **Eigenschaft. Der geografische oder geopolitische Standort eines Flughafens.**    
Version: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste der Eigenschaften    
<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.    
- `Latitude[number]`: Koordinate für den Breitengrad des Flughafens.  - `Longitude[number]`: Koordinate für den Längengrad des Flughafens.  - `Name[string]`: Eindeutiger Name für den Flughafenstandort.  - `Srid[number]`: Ein Spatial Reference System Identifier (SRID), um die Definitionen des räumlichen Koordinatensystems zu identifizieren.  - `id[*]`: Eindeutiger Bezeichner der Entität  - `type[string]`: Sie muss gleich AirportLocation sein.  <!-- /30-PropertiesList -->    
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
## Beispiel-Nutzlasten    
#### AirportLocation NGSI-v2 key-values Beispiel    
Hier ist ein Beispiel für einen AirportLocation im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### AirportLocation NGSI-v2 normalisiert Beispiel    
Hier ist ein Beispiel eines AirportLocation im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
    "type": "Text",  
    "value": "Madrid"  
  },  
  "Srid": {  
    "type": "Number",  
    "value": 4326  
  }  
}  
```  
</details>    
#### AirportLocation NGSI-LD Schlüsselwerte Beispiel    
Hier ist ein Beispiel eines AirportLocation im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.    
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
#### AirportLocation NGSI-LD normalisiert Beispiel    
Hier ist ein Beispiel für einen AirportLocation im JSON-LD-Format in normalisierter Form. Dies ist mit NGSI-LD kompatibel, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.    
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
