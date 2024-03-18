#!/usr/bin/env python3

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import urlsafe_b64encode

class s3ssion:
    def __init__(self, enc_pass:str, register_fields=['name', 'username', 'password'] , enc_salt='session', login_type='default'):
        """
        initialize session class.
        
        Args:
            enc_pass (str): password text to use to encrypt the passwords
            register_fields (list, optional): fields to be entered for registration. Defaults to ['name', 'username', 'password'].
            enc_salt (str, optional): salt text to use to strengthen the password. Defaults to 'session'.
            login_type (str, optional): possible -> ['default', 'auto-login']. Defaults to 'default'. 'auto-login' automatically logs in the user just registered.
        """
        self._userdata = []
        self._sessionuser = ''
        self._islogin = False
        self._reg_f = register_fields
        self._type = login_type
        
        self._kdf = PBKDF2HMAC(
            algorithm=SHA256(),
            length=32,
            salt=enc_salt.encode('ascii'),
            iterations=480000,
        )
        
        self._key = urlsafe_b64encode(self._kdf.derive(enc_pass.encode('ascii')))
        
        self._fernet = Fernet(self._key)
    
    def _login_(self, username:str, password:str):
        """
        login user
        
        Args:
            username (str): username to login
            password (str): password for username

        Returns:
            error (str | None): returns error text, if all good then error=None
        """
        if self._islogin:
            return f'{self._sessionuser} is currently logged in'
        else:
            for entry in self._userdata:
                if entry['name'] == username:
                    if self._fernet.decrypt(entry['password'].encode('ascii')) == password.encode('ascii'):
                        self._islogin = True
                        self._sessionuser = username
                        return None
                    else:
                        return 'password incorrect.'
                else:
                    return 'user not found.'
    
    def _register_(self, **kwargs):
        """
        register function.
        
        ARGS:
            NOTE: whatever field you entered during the class initialization, add them. default -> ['name', 'username', 'password'].
        Returns:
            error (str | None): returns error text if any, else None
        """
        data = {}
        for field in self._reg_f:
            try:
                if field=='password':
                    data[f'{field}'] = self._fernet.encrypt(kwargs[f'{field}'].encode('ascii')).decode('ascii')
                    continue
                data[f'{field}'] = kwargs[f'{field}']
            except KeyError:
                return f'Enter field {field}'
        
        self._userdata.append(data)
        
        if self._type=='auto-login':
            self._islogin = True
            self._sessionuser = kwargs['username']
        
        return None
    
    def _force_login_(self, username:str):
        """forcefully login an user.

        Args:
            username (str): username to forcefully login.
        """
        self._islogin = True
        self._sessionuser = username
    
    def _user_count_(self):
        """get registered user count

        Returns:
            usercount (int): Number of users currently registered.
        """
        return len(self._userdata)
    
    def _login_status_(self):
        """get login status

        Returns:
            status (bool): returns if anyone is currently logged in.
        """
        return self._islogin
    
    def _logout_(self):
        """logout currently logged in user

        Returns:
            error (str | None): returns error text or None
        """
        if not self._islogin:
            return 'no one is currently logged in.'
        else:
            self._islogin = False
            self._sessionuser = ''
            return None
    
    def _login_who_(self):
        """returns currently logged in user

        Returns:
            username (str): currently logged in user.
        """
        return self._sessionuser
    
    def _change_password_(self, username: str, old_password: str, new_password: str):
        """change user password.

        Args:
            username (str): username of the user
            old_password (str): old password
            new_password (str): new password

        Returns:
            error (str | None): returns error text or None
        """
        for user in self._userdata:
            if user['username'] == username:
                if self._fernet.decrypt(user['password'].encode('ascii')) == old_password.encode('ascii'):
                    self._userdata[self._userdata.index(user)]['password'] = self._fernet.encrypt(new_password.encode('ascii')).decode('ascii')
                    return None
                else:
                    return 'incorrect password.'
            else:
                return 'user not found.'
    