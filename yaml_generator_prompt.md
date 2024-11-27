# OpenAPI 3.1 YAML Specification Guide

Generate a comprehensive OpenAPI 3.1 YAML specification using the following information:

## 1. cURL Request
```bash
# Paste the cURL command for the API endpoint:
{PASTE_CURL_HERE}
```

## 2. Parameter Documentation

### Query Parameters
| Name | Data Type | Required/Optional | Description | Possible Enum Values |
|------|-----------|------------------|-------------|---------------------|
| _example_ | string | Required | Description here | enum1, enum2 |

### Path Parameters
| Name | Data Type | Description | Format or Pattern |
|------|-----------|-------------|-------------------|
| _example_ | integer | Description here | ^[0-9]+$ |

### Headers and Body Parameters
| Name | Data Type | Description | Validation Rules |
|------|-----------|-------------|------------------|
| _example_ | string | Description here | Max length: 255, Pattern: ^[A-Za-z0-9]+$ |

## 3. Response Documentation

### Expected Response
```json
{PASTE_RESPONSE_JSON_HERE}
```

### Additional Response States

#### Success Response
```json
{PASTE_SUCCESS_RESPONSE}
```

#### Error Response
```json
{PASTE_ERROR_RESPONSE}
```

#### Validation Error
```json
{PASTE_VALIDATION_ERROR}
```

## 4. Requirements Checklist

- [ ] **Schemas**: Extract and define schemas from both request and response bodies
- [ ] **Validation Rules**: Include all possible validation rules based on response data patterns
- [ ] **Status Codes**: Document all status codes with their exact response structures
- [ ] **Security Schemes**: Define security schemes based on authentication method
- [ ] **Examples**: Generate meaningful examples using actual request/response data
- [ ] **Field-Level Documentation**: Include field-level descriptions and validations
- [ ] **Enums**: Define enums for fields with fixed values
- [ ] **Pagination**: Include pagination details if present
- [ ] **Rate Limiting**: Document rate limiting based on response headers
- [ ] **Error Schemas**: Generate detailed error schemas based on error responses

## 5. Quality Assurance Checklist

- [ ] All fields have appropriate data types and formats
- [ ] Required fields are accurately marked based on response structure
- [ ] Patterns and validations align with actual data
- [ ] Examples use real data from request/response
- [ ] Error responses cover all possible validation scenarios
