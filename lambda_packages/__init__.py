import os

# A manifest of the included packages.
lambda_packages = {
    'bcrypt': {
        'python2.7': {
            'version': '3.1.1',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'bcrypt', 'python2.7-bcrypt-3.1.1.tar.gz')
        }
    },
    'cffi': {
        'python2.7': {
            'version': '1.7.0',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'cffi', 'python2.7-cffi-1.7.0.tar.gz')
        }
    },
    'cryptography': {
        'python2.7': {
            'version': '1.8.1',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'cryptography', 'python2.7-cryptography-1.8.1.tar.gz')
        }
    },
    'cv2': {
        'python2.7': {
            'version': '3.1.0',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'OpenCV', 'python2.7-OpenCV-3.1.0.tar.gz')
        }
    },
    'datrie_extended': {
        'python2.7': {
            'version': '0.7.3',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'datrie_extended', 'python2.7-datrie_extended-0.7.3.tar.gz')
        }
    },
    'lxml': {
        'python2.7': {
            'version': '3.6.0',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'lxml', 'python2.7-lxml-3.6.0.tar.gz')
        }
    },
    'misaka': {
        'python2.7': {
            'version': '2.0.0',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'misaka', 'python2.7-misaka-2.0.0.tar.gz')
        }
    },
    'MySQL-Python': {
        'python2.7': {
            'version': '1.2.5',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'MySQL-Python', 'python2.7-MySQL-Python-1.2.5.tar.gz')
        }
    },
    'numpy': {
        'python2.7': {
            'version': '1.10.4',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'numpy', 'python2.7-numpy-1.10.4.tar.gz')
        }
    },
    'Pillow': {
        'python2.7': {
            'version': '3.4.2',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'Pillow', 'python2.7-Pillow-3.4.2.tar.gz')
        }
    },
    'psycopg2': {
        'python2.7': {
            'version': '2.6.1',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'psycopg2', 'python2.7-psycopg2-2.6.1.tar.gz')
        }
    },
    'pycrypto': {
        'python2.7': {
            'version': '2.6.1',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'pycrypto', 'python2.7-pycrypto-2.6.1.tar.gz')
        },
        'python3.6': {
            'version': '2.6.1',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'pycrypto', 'python3.6-pycrypto-2.6.1.tar.gz')
        }
    },
    'pynacl': {
        'python2.7': {
            'version': '1.0.1',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'PyNaCl', 'python2.7-PyNaCl-1.0.1.tar.gz')
        }
    },
    'pyproj': {
        'python2.7': {
            'version': '1.9.5',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'pyproj', 'python2.7-pyproj.4-4.9.2.tar.gz')
        }
    },
    'python-ldap': {
        'python2.7': {
            'version': '2.4.29',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'python-ldap', 'python2.7-python-ldap-2.4.29.tar.gz')
        }
    },
    'python-Levenshtein': {
        'python2.7': {
            'version': '0.12.0',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'python-Levenshtein', 'python2.7-python-Levenshtein-0.12.0.tar.gz'),
        }
    },
    'regex': {
        'python2.7': {
            'version': '2016.8.27',
            'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'regex', 'python2.7-regex-2016.8.27.tar.gz')
        }
    }
}
