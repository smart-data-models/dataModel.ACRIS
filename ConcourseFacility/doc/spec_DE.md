<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: ConcourseFacility  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/ConcourseFacility/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Eigenschaft. Informationen über einen Airport Concourse als Gebäude oder Infrastruktur, die zur Erbringung von Dienstleistungen genutzt werden.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `Identifier[string]`: Eindeutiger Identifikator für die Concourse Facility.  - `Name[string]`: Eindeutiger Name für die Concourse Facility.  - `TerminalFacility[object]`: Informationen über ein Flughafenterminal als Gebäude oder Infrastruktur, die zur Erbringung von Dienstleistungen genutzt werden.  	- `AirportFacility[object]`: Informationen über einen Flughafen in Form von Gebäuden oder Infrastruktur, die zur Erbringung von Dienstleistungen genutzt werden.    
	- `Identifier[string]`: Eindeutiger Identifikator für die Terminaleinrichtung.    
	- `Name[string]`: Eindeutiger Name für die Terminaleinrichtung.    
- `id[*]`: Eindeutiger Bezeichner der Entität  - `type[string]`: Sie muss gleich ConcourseFacility sein.  <!-- /30-PropertiesList -->  
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
ConcourseFacility:    
  description: Property. Information about an Airport Concourse as buildings or infrastructure used to provide services.    
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
      description: It must be equal to ConcourseFacility.    
      enum:    
        - ConcourseFacility    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/ConcourseFacility/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/ConcourseFacility/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### ConcourseFacility NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine ConcourseFacility im JSON-LD Format als Key-Values. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ConcourseFacility:id:XFOJ:43820676",  
  "type": "ConcourseFacility",  
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
}  
```  
</details>  
#### ConcourseFacility NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine ConcourseFacility im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ConcourseFacility:id:XFOJ:43820676",  
  "type": "ConcourseFacility",  
  "Identifier": {  
    "type": "Text",  
    "value": "BA/B"  
  },  
  "Name": {  
    "type": "Text",  
    "value": "Boarding Area B"  
  },  
  "TerminalFacility": {  
    "type": "StructuredValue",  
    "value": {  
      "Identifier": "T1",  
      "Name": "Terminal 1",  
      "AirportFacility": {  
        "IataCode": "SFO",  
        "IcaoCode": "KSFO",  
        "Name": "San Francisco International Airport"  
      }  
    }  
  }  
}  
```  
</details>  
#### ConcourseFacility NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine ConcourseFacility im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ConcourseFacility:id:XFOJ:43820676",  
  "type": "ConcourseFacility",  
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
  },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### ConcourseFacility NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine ConcourseFacility im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:ConcourseFacility:id:XFOJ:43820676",  
  "type": "ConcourseFacility",  
  "Identifier": {  
    "type": "Property",  
    "value": "BA/B"  
  },  
  "Name": {  
    "type": "Property",  
    "value": "Boarding Area B"  
  },  
  "TerminalFacility": {  
    "type": "Property",  
    "value": {  
      "Identifier": "T1",  
      "Name": "Terminal 1",  
      "AirportFacility": {  
        "IataCode": "SFO",  
        "IcaoCode": "KSFO",  
        "Name": "San Francisco International Airport"  
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
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
