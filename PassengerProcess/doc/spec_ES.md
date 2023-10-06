<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: PassengerProcess  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.ACRIS/blob/master/PassengerProcess/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Propiedad. Información sobre el proceso de la parte pasajera.**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.  
- `Name[string]`: Nombre único para el proceso de pasajeros.  - `PassengerProcessType[object]`: Información sobre el tipo de Proceso de la Parte Pasajera.  	- `Code[string]`: Código único para el tipo de Proceso de Parte Pasajera.    
	- `Description[string]`: Descripción del tipo de Proceso de la Parte Pasajera.    
- `id[*]`: Identificador único de la entidad  - `type[string]`: Debe ser igual a PassengerProcess.  <!-- /30-PropertiesList -->  
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
PassengerProcess:    
  description: Property. Information about the Passenger Party Process.    
  properties:    
    Name:    
      description: Unique name for the Passenger Process.    
      type: string    
      x-ngsi:    
        type: Property    
    PassengerProcessType:    
      description: Information about the type of Passenger Party Process.    
      properties:    
        Code:    
          description: Unique code for the type of Passenger Party Process.    
          type: string    
          x-ngsi:    
            type: Property    
        Description:    
          description: Description of the type of Passenger Party Process.    
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
      description: It must be equal to PassengerProcess.    
      enum:    
        - PassengerProcess    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: https://acris.aero/static/documents/waittimes/ACI-Wait-Times-API-Specification-v1.6.0.1c4ec122da9a.yaml    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ACRIS/blob/master/PassengerProcess/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ACRIS/PassengerProcess/schema.json    
  x-model-tags: ACRIS    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### PassengerProcess NGSI-v2 key-values Ejemplo  
He aquí un ejemplo de un PassengerProcess en formato JSON-LD como valores clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PassengerProcess:id:HARF:66129232",  
    "type": "PassengerProcess",  
    "Name": "",  
    "PassengerProcessType": {  
        "Code": "code1",  
        "Description": ""  
    }  
}  
```  
</details>  
#### PassengerProcess NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de un PassengerProcess en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PassengerProcess:id:YOUE:15643415",  
    "type": "PassengerProcess",  
    "Name": {  
        "type": "Text",  
        "value": ""  
    },  
    "PassengerProcessType": {  
        "type": "StructuredValue",  
        "value": {  
            "Code": "code1",  
            "Description": ""  
        }  
    }  
}  
```  
</details>  
#### PassengerProcess NGSI-LD key-values Ejemplo  
He aquí un ejemplo de un PassengerProcess en formato JSON-LD como valores clave. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PassengerProcess:id:HARF:66129232",  
    "type": "PassengerProcess",  
    "Name": "",  
    "PassengerProcessType": {  
        "Code": "code1",  
        "Description": ""  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.ACRIS/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### PassengerProcess NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de un PassengerProcess en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:PassengerProcess:id:YOUE:15643415",  
    "type": "PassengerProcess",  
    "Name": {  
        "type": "Property",  
        "value": ""  
    },  
    "PassengerProcessType": {  
        "type": "Property",  
        "value": {  
            "Code": "code1",  
            "Description": ""  
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
