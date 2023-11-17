<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: OperationTimePeriod    
============================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/OperationTimePeriod/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Propiedad. Periodo de tiempo en el que opera el Punto de Control.**    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `ClosingTime[string]`: La fecha y hora a partir de la cual se cierra el Punto de Control. La fecha y la hora deben ser UTC, conforme al formato ISO 8601 (por ejemplo, 2023-04-20T11:54:59Z)  - `OpeningTime[string]`: La fecha y hora a partir de la cual está abierto el Punto de Control. La fecha y la hora deben ser UTC, conforme al formato ISO 8601 (por ejemplo, 2023-04-20T11:54:59Z).  - `id[*]`: Identificador único de la entidad  - `type[string]`: Debe ser igual a OperationTimePeriod.  <!-- /30-PropertiesList -->    
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
OperationTimePeriod:      
  description: Property. The time period over which the Checkpoint is operating.      
  properties:      
    ClosingTime:      
      description: 'The date and time from when the Checkpoint Facility is closed. Date time should be UTC, compliant with ISO 8601 format (e.g. 2023-04-20T11:54:59Z)'      
      type: string      
      x-ngsi:      
        type: Property      
    OpeningTime:      
      description: 'The date and time from when the Checkpoint Facility is open. Date time should be UTC, compliant with ISO 8601 format (e.g. 2023-04-20T11:54:59Z)'      
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
      description: It must be equal to OperationTimePeriod.      
      enum:      
        - OperationTimePeriod      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/OperationTimePeriod/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/OperationTimePeriod/schema.json      
  x-model-tags: ACRIS      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### OperationTimePeriod NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de OperationTimePeriod en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OperationTimePeriod:id:XCIN:24494142",  
  "type": "OperationTimePeriod",  
  "ClosingTime": "23:59:02Z",  
  "OpeningTime": "00:00:00Z"  
}  
```  
</details>    
#### OperationTimePeriod NGSI-v2 normalized Ejemplo    
He aquí un ejemplo de OperationTimePeriod en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OperationTimePeriod:id:BCTN:53140922",  
  "type": "OperationTimePeriod",  
  "ClosingTime": {  
    "type": "DateTime",  
    "value": "23:59:02Z"  
  },  
  "OpeningTime": {  
    "type": "DateTime",  
    "value": "00:00:02Z"  
  }  
}  
```  
</details>    
#### OperationTimePeriod NGSI-LD key-values Ejemplo    
He aquí un ejemplo de OperationTimePeriod en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OperationTimePeriod:id:XCIN:24494142",  
  "type": "OperationTimePeriod",  
  "ClosingTime": "23:59:02Z",  
  "OpeningTime": "00:00:00Z",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### OperationTimePeriod NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de OperationTimePeriod en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:OperationTimePeriod:id:BCTN:53140922",  
  "type": "OperationTimePeriod",  
  "ClosingTime": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "23:59:02Z"  
    }  
  },  
  "OpeningTime": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "00:00:02Z"  
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
