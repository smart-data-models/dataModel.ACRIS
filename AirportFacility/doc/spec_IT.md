<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: AeroportoStabilimento    
=============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/AirportFacility/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Proprietà. Informazioni su un aeroporto come edifici o infrastrutture utilizzate per fornire servizi **.    
versione: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `IataCode[string]`: Codice IATA a tre caratteri dell'aeroporto.  - `IcaoCode[string]`: Codice ICAO a quattro caratteri dell'aeroporto.  - `Name[string]`: Nome comune dell'aeroporto.  - `id[*]`: Identificatore univoco dell'entità  - `type[string]`: Deve essere uguale a AirportFacility.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Questo modello di dati è una mappatura del Passenger Wait Times Standard v1.6.0 dell'Airports Council International (ACI) ACRIS data interface standard. Disponibile su https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
AirportFacility:      
  description: Property. Information about an Airport as buildings or infrastructure used to provide services.      
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
      description: It must be equal to AirportFacility.      
      enum:      
        - AirportFacility      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/AirportFacility/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/AirportFacility/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Esempi di payload    
#### AirportFacility Valori-chiave NGSI-v2 Esempio    
Ecco un esempio di AirportFacility in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirportFacility:id:IUXP:30337114",  
  "type": "AirportFacility",  
  "IataCode": "BMA",  
  "IcaoCode": "ESSB",  
  "Name": "control"  
}  
```  
</details>    
#### AirportFacility NGSI-v2 normalizzato Esempio    
Ecco un esempio di AirportFacility in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirportFacility:id:CJKH:90684356",  
  "type": "AirportFacility",  
  "IataCode": {  
    "type": "Text",  
    "value": "YYT."  
  },  
  "IcaoCode": {  
    "type": "Text",  
    "value": "LE"  
  },  
  "Name": {  
    "type": "Text",  
    "value": "control"  
  }  
}  
```  
</details>    
#### AirportFacility Valori chiave NGSI-LD Esempio    
Ecco un esempio di AirportFacility in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirportFacility:id:IUXP:30337114",  
  "type": "AirportFacility",  
  "IataCode": "BMA",  
  "IcaoCode": "ESSB",  
  "Name": "control",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AeroportoFacoltà NGSI-LD normalizzato Esempio    
Ecco un esempio di AirportFacility in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:AirportFacility:id:CJKH:90684356",  
    "type": "AirportFacility",  
    "IataCode": {  
        "type": "Property",  
        "value": "BMA"  
    },  
    "IcaoCode": {  
        "type": "Property",  
        "value": "ESSB"  
    },  
    "Name": {  
        "type": "Property",  
        "value": "control"  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
