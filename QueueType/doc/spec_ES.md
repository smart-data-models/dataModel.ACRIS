<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: QueueType  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/QueueType/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Propiedad. Información sobre el tipo de una cola de pasajeros. Los valores pueden ser: Pre-Check, Private, Economy, Priority, KnownCrewMember.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `Code[string]`: Código único para el tipo de cola de pasajeros.  - `Description[string]`: Descripción del tipo de cola de pasajeros.  - `id[*]`: Identificador único de la entidad  - `type[string]`: Debe ser igual a QueueType.  <!-- /30-PropertiesList -->  
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
QueueType:    
  description: 'Property. Information about the type of a Passenger Queue. Values can be: Pre-Check, Private, Economy, Priority, KnownCrewMember.'    
  properties:    
    Code:    
      description: Unique code for the type of Passenger Queue.    
      type: string    
      x-ngsi:    
        type: Property    
    Description:    
      description: Description of the type of Passenger Queue.    
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
      description: It must be equal to QueueType.    
      enum:    
        - QueueType    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/QueueType/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/QueueType/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### QueueType NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un QueueType en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:QueueType:id:TFYE:17389668",  
    "type": "QueueType",  
    "Code": "type1",  
    "Description": ""  
}  
```  
</details>  
#### QueueType NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de un QueueType en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:QueueType:id:BCWB:56620437",  
    "type": "QueueType",  
    "Code": {  
        "type": "Text",  
        "value": "type1"  
    },  
    "Description": {  
        "type": "Text",  
        "value": ""  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### QueueType NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un QueueType en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:QueueType:id:TFYE:17389668",  
    "type": "QueueType",  
    "Code": "type1",  
    "Description": "",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### QueueType NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un QueueType en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:QueueType:id:BCWB:56620437",  
    "type": "QueueType",  
    "Code": {  
        "type": "Property",  
        "value": "type1"  
    },  
    "Description": {  
        "type": "Property",  
        "value": ""  
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
