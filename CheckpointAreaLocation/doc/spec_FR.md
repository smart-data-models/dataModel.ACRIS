<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entité : CheckpointAreaLocation    
===============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ACRIS/blob/master/CheckpointAreaLocation/LICENSE.md)    
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Description globale : **Propriété. Emplacement géospatial ou géopolitique d'un point de contrôle.    
version : 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Liste des propriétés    
<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il peut avoir plusieurs types ou différents formats/modèles</sub></sup>.    
- `AirportElevation[object]`: Hauteur d'un aéroport au-dessus du niveau de la mer.  	- `AirportElevationUnitOfMeasurement[object]`: L'unité de mesure de la hauteur d'un aéroport au-dessus du niveau de la mer (FT pour foot ou M pour metre).      
	- `Name[string]`: Nom de l'altitude d'un aéroport par rapport au niveau de la mer.      
	- `Value[number]`: Valeur de l'altitude d'un aéroport par rapport au niveau de la mer.      
- `Latitude[number]`: Coordonnées de la latitude de la zone du point de contrôle.  - `Longitude[number]`: Coordonnées de la longitude de l'emplacement de la zone de contrôle.  - `Name[string]`: Nom unique de l'emplacement géospatial ou géopolitique d'une zone de contrôle.  - `Srid[number]`: un identificateur de système de référence spatiale (SRID), pour identifier les définitions du système de coordonnées spatiales  - `ZoneAreaLocation[object]`: Emplacement géospatial ou géopolitique d'une zone d'attente dans un terminal.  	- `Name[string]`: Nom unique de l'emplacement de la zone.      
	- `TerminalAreaLocation[object]`: Emplacement géospatial ou géopolitique d'un terminal d'aéroport.      
- `id[*]`: Identifiant unique de l'entité  - `type[string]`: Il doit être égal à CheckpointAreaLocation.  <!-- /30-PropertiesList -->    
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
CheckpointAreaLocation:      
  description: Property. The geospatial or geopolitical location of a Checkpoint.      
  properties:      
    AirportElevation:      
      description: 'The height of an Airport, above sea level.'      
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
      type: object      
      x-ngsi:      
        type: Property      
    Latitude:      
      description: Coordinate of the latitude of the checkpoint area location.      
      type: number      
      x-ngsi:      
        type: Property      
    Longitude:      
      description: Coordinate of the longitude of the checkpoint area location.      
      type: number      
      x-ngsi:      
        type: Property      
    Name:      
      description: Unique name for geospatial or geopolitical location of a Checkpoint Area Location.      
      type: string      
      x-ngsi:      
        type: Property      
    Srid:      
      description: 'A Spatial Reference System Identifier (SRID), to identify the spatial coordinate system definitions'      
      type: number      
      x-ngsi:      
        type: Property      
    ZoneAreaLocation:      
      description: The geospatial or geopolitical location of a Queuing Zone in a Terminal.      
      properties:      
        Name:      
          description: Unique name for the Zone Area Location.      
          type: string      
          x-ngsi:      
            type: Property      
        TerminalAreaLocation:      
          description: The geospatial or geopolitical location of an Airport Terminal building.      
          properties:      
            AirportLocation:      
              description: The geospatial or geopolitical location of an Airport.      
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
                  type: integer      
                  x-ngsi:      
                    type: Property      
              type: object      
              x-ngsi:      
                type: Property      
            Name:      
              description: Unique name for the Terminal Area Location.      
              type: string      
              x-ngsi:      
                type: Property      
          type: object      
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
      description: It must be equal to CheckpointAreaLocation.      
      enum:      
        - CheckpointAreaLocation      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/CheckpointAreaLocation/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/CheckpointAreaLocation/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Exemples de charges utiles    
#### CheckpointAreaLocation Valeurs clés NGSI-v2 Exemple    
Voici un exemple de CheckpointAreaLocation au format JSON-LD en tant que valeurs clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CheckpointAreaLocation:id:BLBC:14665623",  
  "type": "CheckpointAreaLocation",  
  "Latitude": 40.42,  
  "Longitude": 3.708,  
  "Name": "As since dream public analysis clear one. Federal skill term court.",  
  "Srid": 4326,  
  "AirportElevation": {  
    "Name": "",  
    "Value": 777.7,  
    "AirportElevationUnitOfMeasurement": {  
      "Name": "Meters"  
    }  
  },  
  "ZoneAreaLocation": {  
    "Name": "",  
    "TerminalAreaLocation": {  
      "Name": "",  
      "AirportLocation": {  
        "Latitude": 40.42,  
        "Longitude": 3.708,  
        "Name": "Barajas",  
        "Srid": 4326  
      }  
    }  
  }  
}  
```  
</details>    
#### CheckpointAreaLocation NGSI-v2 normalisé Exemple    
Voici un exemple de CheckpointAreaLocation au format JSON-LD tel que normalisé. Ce format est compatible avec la norme NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CheckpointAreaLocation:id:KSRW:92816613",  
  "type": "CheckpointAreaLocation",  
  "Latitude": {  
    "type": "Number",  
    "value": 2.4  
  },  
  "Longitude": {  
    "type": "Number",  
    "value": 5.3  
  },  
  "Name": {  
    "type": "Text",  
    "value": ""  
  },  
  "Srid": {  
    "type": "Number",  
    "value": 4326  
  },  
  "AirportElevation": {  
    "type": "StructuredValue",  
    "value": {  
      "Name": "",  
      "Value": 487.8,  
      "AirportElevationUnitOfMeasurement": {  
        "Name": "Meters"  
      }  
    }  
  },  
  "ZoneAreaLocation": {  
    "type": "StructuredValue",  
    "value": {  
      "Name": "",  
      "TerminalAreaLocation": {  
        "Name": "Madrid",  
        "AirportLocation": {  
          "Latitude": 40.41,  
          "Longitude": 3.7,  
          "Name": "",  
          "Srid": 662  
        }  
      }  
    }  
  }  
}  
```  
</details>    
#### CheckpointAreaLocation Valeurs clés NGSI-LD Exemple    
Voici un exemple de CheckpointAreaLocation au format JSON-LD sous forme de valeurs clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données de contexte d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:CheckpointAreaLocation:id:BLBC:14665623",  
  "type": "CheckpointAreaLocation",  
  "Latitude": 40.42,  
  "Longitude": 3.708,  
  "Name": "As since dream public analysis clear one. Federal skill term court.",  
  "Srid": 4326,  
  "AirportElevation": {  
    "Name": "",  
    "Value": 777.7,  
    "AirportElevationUnitOfMeasurement": {  
      "Name": "Meters"  
    }  
  },  
  "ZoneAreaLocation": {  
    "Name": "",  
    "TerminalAreaLocation": {  
      "Name": "",  
      "AirportLocation": {  
        "Latitude": 40.42,  
        "Longitude": 3.708,  
        "Name": "Barajas",  
        "Srid": 4326  
      }  
    }  
  },  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### CheckpointAreaLocation NGSI-LD normalisé Exemple    
Voici un exemple de CheckpointAreaLocation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:CheckpointAreaLocation:id:KSRW:92816613",  
    "type": "CheckpointAreaLocation",  
    "Latitude": {  
        "type": "Property",  
        "value": 40.42  
    },  
    "Longitude": {  
        "type": "Property",  
        "value": 3.708  
    },  
    "Name": {  
        "type": "Property",  
        "value": "Madrid"  
    },  
    "Srid": {  
        "type": "Property",  
        "value": 4326  
    },  
    "AirportElevation": {  
        "type": "Property",  
        "value": {  
            "Name": "",  
            "Value": 487.8,  
            "AirportElevationUnitOfMeasurement": {  
                "Name": "Meters"  
            }  
        }  
    },  
    "ZoneAreaLocation": {  
        "type": "Property",  
        "value": {  
            "Name": "",  
            "TerminalAreaLocation": {  
                "Name": "Madrid",  
                "AirportLocation": {  
                    "Latitude": 40.42,  
                    "Longitude": 3.708,  
                    "Name": "",  
                    "Srid": 4326  
                }  
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
Voir [FAQ 10] (https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse à la question de savoir comment traiter les unités de magnitude.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
