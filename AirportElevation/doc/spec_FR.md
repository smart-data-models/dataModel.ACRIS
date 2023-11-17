<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : Altitude de l'aéroport    
===============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ACRIS/blob/master/AirportElevation/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Propriété. Hauteur d'un aéroport au-dessus du niveau de la mer.    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `AirportElevationUnitOfMeasurement[object]`: L'unité de mesure de la hauteur d'un aéroport au-dessus du niveau de la mer (FT pour foot ou M pour metre).  	- `Name[string]`: Nom de l'unité de mesure de l'altitude d'un aéroport par rapport au niveau de la mer.      
- `Name[string]`: Nom de l'altitude d'un aéroport par rapport au niveau de la mer.  - `Value[number]`: Valeur de l'altitude d'un aéroport par rapport au niveau de la mer.  - `id[*]`: Identifiant unique de l'entité  - `type[string]`: Il doit être égal à AirportElevation.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propriétés requises    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Ce modèle de données est un mappage de la norme sur les temps d'attente des passagers v1.6.0 de la norme d'interface de données ACRIS du Conseil international des aéroports (ACI). Disponible à l'adresse suivante : https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modèle de données description des propriétés    
Classés par ordre alphabétique (cliquez pour plus de détails)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
AirportElevation:      
  description: 'Property. The height of an Airport, above sea level.'      
  properties:      
    AirportElevationUnitOfMeasurement:      
      description: The unit of measure of the height of an Airport above sea level (FT for foot or M for metre).      
      properties:      
        Name:      
          description: The name of the unit of measure for an Airport elevation above sea level.      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        type: Property      
    Name:      
      description: The name of an Airport elevation above sea level.      
      type: string      
      x-ngsi:      
        type: Property      
    Value:      
      description: The value of an Airport elevation above sea level.      
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
      description: It must be equal to AirportElevation.      
      enum:      
        - AirportElevation      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/AirportElevation/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/AirportElevation/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### AirportElevation Valeurs clés de l'INSIG-v2 Exemple    
Voici un exemple d'altitude d'aéroport au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirportElevation:id:WOBQ:34953390",  
  "type": "AirportElevation",  
  "Name": "Agreement figure talk arrive responsibility popular. Election simple treat more next how speech.",  
  "Value": 502.8,  
  "AirportElevationUnitOfMeasurement": {  
    "Name": "Meters"  
  }  
}  
```  
</details>    
#### AirportElevation NGSI-v2 normalisé Exemple    
Voici un exemple de l'altitude d'un aéroport au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirportElevation:id:BQPP:71138381",  
  "type": "AirportElevation",  
  "Name": {  
    "type": "Text",  
    "value": ""  
  },  
  "Value": {  
    "type": "Number",  
    "value": 400.6  
  },  
  "AirportElevationUnitOfMeasurement": {  
    "type": "StructuredValue",  
    "value": {  
      "Name": "meters"  
    }  
  }  
}  
```  
</details>    
#### AirportElevation Valeurs clés NGSI-LD Exemple    
Voici un exemple d'altitude d'aéroport au format JSON-LD sous forme de valeurs clés. Ce format est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirportElevation:id:WOBQ:34953390",  
  "type": "AirportElevation",  
  "Name": "",  
  "Value": 502.8,  
  "AirportElevationUnitOfMeasurement": {  
    "Name": "Meters"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### AirportElevation NGSI-LD normalisé Exemple    
Voici un exemple d'altitude d'aéroport au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:AirportElevation:id:BQPP:71138381",  
    "type": "AirportElevation",  
    "Name": {  
        "type": "Property",  
        "value": ""  
    },  
    "Value": {  
        "type": "Property",  
        "value": 400.6  
    },  
    "AirportElevationUnitOfMeasurement": {  
        "type": "Property",  
        "value": {  
            "Name": "Meters"  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
