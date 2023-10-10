<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : Installation terminale  
===============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ACRIS/blob/master/TerminalFacility/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Propriété. Informations sur un terminal d'aéroport sous forme de bâtiments ou d'infrastructures utilisés pour fournir des services**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `AirportFacility[object]`: Informations sur un aéroport telles que les bâtiments ou les infrastructures utilisés pour fournir des services.  	- `IataCode[string]`: Code IATA à trois caractères de l'aéroport.    
	- `IcaoCode[string]`: Code OACI à quatre caractères de l'aéroport.    
	- `Name[string]`: Nom commun de l'aéroport.    
- `Identifier[string]`: Identifiant unique de l'installation terminale.  - `Name[string]`: Nom unique de l'installation terminale.  - `id[*]`: Identifiant unique de l'entité  - `type[string]`: Il doit être égal à TerminalFacility.  <!-- /30-PropertiesList -->  
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
TerminalFacility:    
  description: Property. Information about an Airport Terminal as buildings or infrastructure used to provide services.    
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
      description: It must be equal to TerminalFacility.    
      enum:    
        - TerminalFacility    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/TerminalFacility/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/TerminalFacility/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Exemples de charges utiles  
#### TerminalFacility Valeurs clés de l'INS-v2 Exemple  
Voici un exemple d'une TerminalFacility au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TerminalFacility:id:HJCW:88401819",  
  "type": "TerminalFacility",  
  "Identifier": "T2",  
  "Name": "Terminal 2",  
  "AirportFacility": {  
    "IataCode": "SFO",  
    "IcaoCode": "KSFO",  
    "Name": "San Francisco International Airport"  
  }  
}  
```  
</details>  
#### TerminalFacility NGSI-v2 normalisée Exemple  
Voici un exemple de TerminalFacility au format JSON-LD tel qu'il a été normalisé. Ce format est compatible avec les NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:TerminalFacility:id:ACFX:01548511",  
    "type": "TerminalFacility",  
    "Identifier": {  
        "type": "Text",  
        "value": "BA/C"  
    },  
    "Name": {  
        "type": "Text",  
        "value": "Boarding Area C"  
    },  
    "AirportFacility": {  
        "type": "StructuredValue",  
        "value": {  
            "IataCode": "SFO",  
            "IcaoCode": "KSFO",  
            "Name": "San Francisco International Airport"  
        }  
    }  
}  
```  
</details>  
#### TerminalFacility Valeurs clés NGSI-LD Exemple  
Voici un exemple d'une TerminalFacility au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:TerminalFacility:id:HJCW:88401819",  
  "type": "TerminalFacility",  
  "Identifier": "T2",  
  "Name": "Terminal 2",  
  "AirportFacility": {  
    "IataCode": "SFO",  
    "IcaoCode": "KSFO",  
    "Name": "San Francisco International Airport"  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### TerminalFacility NGSI-LD normalisé Exemple  
Voici un exemple de TerminalFacility au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:TerminalFacility:id:ACFX:01548511",  
    "type": "TerminalFacility",  
    "Identifier": {  
        "type": "Property",  
        "value": "BA/C"  
    },  
    "Name": {  
        "type": "Property",  
        "value": "Boarding Area C"  
    },  
    "AirportFacility": {  
        "type": "Property",  
        "value": {  
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
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
