# WeirdText encoding

---
## How to deploy

---
## REST API endpoints

---
### Encode
Returns encoded text in WeirdText encoding and original words that got shuffled.

`POST /v1/encode`

**Parameters**


| Name | Type   | In   | Description                          |
| ---- | ------ | -----| -------------------------------------|
| text | string | body | text to encode in WeirdText encoding |

**Response**

`Status: 200 OK`
```
{
    "encoded_text": "\n—weird—\nThis is a long lonoog tset scnnetee,\nwtih some big (biiiiig) wrdos!\n—weird—\n",
    "original_words": [
        "looong",
        "sentence",
        "test",
        "with",
        "words"
    ]
}
```


### Decode
Returns decoded text.

`POST /v1/decode`

**Parameters**


| Name           | Type   | In   | Description                        |
| :------------: | :----: | :---:| :----------------------------------:|
| text           | string | body | text encoded in WeirdText encoding |
| original_words | list   | body | original words that got shuffled   |

**Response**

`Status: 200 OK`
```
{
    "decoded_text": "This is a long looong test sentence,\nwith some big (biiiiig) words!"
}
```