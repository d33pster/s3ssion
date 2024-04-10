# <p align='center'>s3ssion</p>

[![codecov](https://codecov.io/gh/d33pster/s3ssion/graph/badge.svg?token=R08LSVN441)](https://codecov.io/gh/d33pster/s3ssion)
[![Build status](https://ci.appveyor.com/api/projects/status/c3lp95w65r360b1l?svg=true)](https://ci.appveyor.com/project/d33pster/s3ssion)


<p align='center'>
    <a href='#Installation'>Installation</a>
    &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
    <a href='#Usage'>Usage</a>
</p><br>

## About
Session helps creating login sessions.

## Installation
```console
## run
$ pip install s3ssion
```

## Usage

###### initialization
```console
>>> from s3ssion import s3ssion
>>> sess = s3ssion('password')
```
for help with session class initialization
```console
>>> from s3ssion import s3ssion
>>> help(s3ssion)
```

###### class functions
```console
>>> from s3ssion import s3ssion

# _login()_ function
>>> help(s3ssion._login_)

Help on function _login_ in module src.s3ssion:

_login_(self, username: str, password: str)
    login user

    Args:
        username (str): username to login
        password (str): password for username

    Returns:
        error (str | None): returns error text, if all good then error=None
```

```console
# _register_() function
>>> help(s3ssion._register_)

Help on function _register_ in module src.s3ssion:

_register_(self, **kwargs)
    register function.

    ARGS:
        NOTE: whatever field you entered during the class initialization, add them. default -> ['name', 'username', 'password'].
    Returns:
        error (str | None): returns error text if any, else None
```

```console
# _logout_() function
>>> help(s3ssion._logout_)

Help on function _logout_ in module src.s3ssion:

_logout_(self)
    logout currently logged in user

    Returns:
        error (str | None): returns error text or None
```

```console
# _change_password_() function
>>> help(s3ssion._change_password_)

Help on function _change_password_ in module src.s3ssion:

_change_password_(self, username: str, old_password: str, new_password: str)
    change user password.

    Args:
        username (str): username of the user
        old_password (str): old password
        new_password (str): new password

    Returns:
        error (str | None): returns error text or None
```

```console
# _login_who_() function
>>> help(s3ssion._login_who_)

Help on function _login_who_ in module src.s3ssion:

_login_who_(self)
    returns currently logged in user

    Returns:
        username (str): currently logged in user.
```

```console
# _login_status_() function
>>> help(s3ssion._login_function_)

Help on function _login_status_ in module src.s3ssion:

_login_status_(self)
    get login status

    Returns:
        status (bool): returns if anyone is currently logged in.
```

```console
# _user_count_() function
>>> help(s3ssion._user_count_)

Help on function _user_count_ in module src.s3ssion:

_user_count_(self)
    get registered user count

    Returns:
        usercount (int): Number of users currently registered.
```

```console
# _force_login_() function
>>> help(s3ssion._force_login_)

Help on function _force_login_ in module src.s3ssion:

_force_login_(self, username: str)
    forcefully login an user.

    Args:
        username (str): username to forcefully login.
```
