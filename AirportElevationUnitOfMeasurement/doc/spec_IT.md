<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: AeroportoUnitOfMeasurement  
==================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/AirportElevationUnitOfMeasurement/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Proprietà. L'unità di misura dell'altezza di un aeroporto sul livello del mare (FT per piede o M per metro)**.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `Name[string]`: Il nome dell'unità di misura dell'altitudine dell'aeroporto sul livello del mare.  - `id[*]`: Identificatore univoco dell'entità  - `type[string]`: Deve essere uguale a AirportElevationUnitOfMeasurement.  <!-- /30-PropertiesList -->  
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
## Esempi di payload  
#### Valori chiave NGSI-v2 di AirportElevationUnitOfMeasurement Esempio  
Ecco un esempio di AirportElevationUnitOfMeasurement in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:AirportElevationUnitOfMeasurement:id:PPBL:76921497",  
    "type": "AirportElevationUnitOfMeasurement",  
    "Name": "Meters"  
}  
```  
</details>  
#### AirportElevationUnitOfMeasurement NGSI-v2 normalizzato Esempio  
Ecco un esempio di AirportElevationUnitOfMeasurement in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano le opzioni e restituisce i dati di contesto di una singola entità.  
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
#### AirportElevationUnitOfMeasurement Valori chiave NGSI-LD Esempio  
Ecco un esempio di AirportElevationUnitOfMeasurement in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### AirportElevationUnitOfMeasurement NGSI-LD normalizzato Esempio  
Ecco un esempio di AirportElevationUnitOfMeasurement in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
