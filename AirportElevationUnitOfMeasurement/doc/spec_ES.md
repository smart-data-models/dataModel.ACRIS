<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: AirportElevationUnitOfMeasurement    
==========================================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/AirportElevationUnitOfMeasurement/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Propiedad. Unidad de medida de la altura de un Aeropuerto sobre el nivel del mar (FT para pie o M para metro)**.    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `Name[string]`: Nombre de la unidad de medida de la elevación de un Aeropuerto sobre el nivel del mar.  - `id[*]`: Identificador único de la entidad  - `type[string]`: Debe ser igual a AirportElevationUnitOfMeasurement.  <!-- /30-PropertiesList -->    
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
## Ejemplo de carga útil    
#### AirportElevationUnitOfMeasurement NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de AirportElevationUnitOfMeasurement en formato JSON-LD como valores clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:AirportElevationUnitOfMeasurement:id:PPBL:76921497",  
  "type": "AirportElevationUnitOfMeasurement",  
  "Name": "Meters"  
}  
```  
</details>    
#### AirportElevationUnitOfMeasurement NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de AirportElevationUnitOfMeasurement en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos contextuales de una entidad individual.    
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
#### AirportElevationUnitOfMeasurement NGSI-LD key-values Ejemplo    
He aquí un ejemplo de AirportElevationUnitOfMeasurement en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### AirportElevationUnitOfMeasurement NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de AirportElevationUnitOfMeasurement en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
