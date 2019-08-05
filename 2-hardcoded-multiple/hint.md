To represent user credentials, try one of:

* A dictionary where the keys are usernames and the values are passwords

```
{
  'robert': 'password123',
  'anoosh': 'snuffles456',
  'juan': 'happyland'
}
```

* A list where each element is a dictionary with 2 keys: username and password

```
[
  {
    'username': 'robert',
    'password': 'password123`
  },
  {
    'username': 'anoosh',
    'password': 'snuffles456`
  },
 {
    'username': 'juan',
    'password': 'happyland`
  }
]
```

In each case, think about how, given a username, you can verify an associated password.
