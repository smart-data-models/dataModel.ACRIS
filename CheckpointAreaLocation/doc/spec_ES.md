<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: CheckpointAreaLocation    
===============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/CheckpointAreaLocation/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Propiedad. La ubicación geoespacial o geopolítica de un Punto de Control.**    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `AirportElevation[object]`: Altura de un aeropuerto sobre el nivel del mar.  	- `AirportElevationUnitOfMeasurement[object]`: Unidad de medida de la altura de un Aeropuerto sobre el nivel del mar (FT para pie o M para metro).      
	- `Name[string]`: Nombre de la elevación de un Aeropuerto sobre el nivel del mar.      
	- `Value[number]`: Valor de la elevación de un Aeropuerto sobre el nivel del mar.      
- `Latitude[number]`: Coordenada de la latitud de la ubicación del área del punto de control.  - `Longitude[number]`: Coordenada de la longitud de la ubicación del área del punto de control.  - `Name[string]`: Nombre único para la ubicación geoespacial o geopolítica de una Localización de Área de Control.  - `Srid[number]`: Un Identificador del Sistema de Referencia Espacial (SRID), para identificar las definiciones del sistema de coordenadas espaciales.  - `ZoneAreaLocation[object]`: La ubicación geoespacial o geopolítica de una Zona de Cola en una Terminal.  	- `Name[string]`: Nombre único para la Ubicación del Área de Zona.      
	- `TerminalAreaLocation[object]`: La ubicación geoespacial o geopolítica del edificio de una terminal aeroportuaria.      
- `id[*]`: Identificador único de la entidad  - `type[string]`: Debe ser igual a CheckpointAreaLocation.  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
Este modelo de datos es un mapeo del Estándar de Tiempos de Espera de Pasajeros v1.6.0 del estándar de interfaz de datos ACRIS del Consejo Internacional de Aeropuertos (ACI). Disponible en https://acris.aero/static/documents/waittimes/ACI-Wait-Times-Standard-API-v1.6.0.12b34cd0213e.pdf    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
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
## Ejemplo de carga útil    
#### CheckpointAreaLocation NGSI-v2 key-values Ejemplo    
Este es un ejemplo de un CheckpointAreaLocation en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### CheckpointAreaLocation NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de CheckpointAreaLocation en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
#### CheckpointAreaLocation NGSI-LD key-values Ejemplo    
Este es un ejemplo de un CheckpointAreaLocation en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### CheckpointAreaLocation NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de CheckpointAreaLocation en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
