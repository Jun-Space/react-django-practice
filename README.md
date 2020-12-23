# User

## User List 불러오기

### Request

| method | uri        |
| ------ | ---------- |
| GET    | /api/users |

### Response

**성공**

```json
{
  "users": [
    {
      "id": number,
      "name": string
    },
    {
      "id": number,
      "name": string
    }
    // ...
  ],
  "success": true
}
```

**실패**

```json
{
  "message": "", // 실패 메시지
  "success": false
}
```

## User 불러오기

### Request

| method | uri                |
| ------ | ------------------ |
| GET    | /api/users/:userId |

### Response

**성공**

```json
{
  "user": {
    "id": number,
    "name": string
  },
  "success": true
}
```

**실패**

```json
{
  "message": "", // 실패 메시지
  "success": false
}
```

## User 추가하기

### Repuest

| method | uri        |
| ------ | ---------- |
| POST   | /api/users |

**Body**

```json
{
  "name": string
}
```

### Response

**성공**

```json
{
 	users: [...]
  success: true
}
```

**실패**

```json
{
  "message": "", // 실패 메시지
  "success": false
}
```

## User 변경하기

### Repuest

| method | uri        |
| ------ | ---------- |
| PUT    | /api/users |

**Body**

```json
{
  "id": number,
  "name": string
}
```

### Response

**성공**

```json
{
  "success": true
}
```

**실패**

```json
{
  "message": "", // 실패 메시지
  "success": false
}
```

## User 삭제하기

### Repuest

| method | uri            |
| ------ | -------------- |
| DELETE | /api/users/:id |

### Response

**성공**

```json
{
  "success": true
}
```

**실패**

```json
{
  "message": "", // 실패 메시지
  "success": false
}
```
