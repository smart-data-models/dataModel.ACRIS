<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=========================
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `AirportFacility[object]`: Información sobre un Aeropuerto como edificios o infraestructuras utilizadas para prestar servicios.  
	- `IcaoCode[string]`: Código OACI de cuatro caracteres del aeropuerto.    
	- `Name[string]`: Nombre común del aeropuerto.    
- `Identifier[string]`: Identificador único de la instalación terminal.  
<!-- 35-RequiredProperties -->

- `id`  
<!-- 40-RequiredProperties -->

<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

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



<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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


<details><summary><strong>show/hide example</strong></summary>    


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

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
