import os

PACKAGES_DIR = os.path.dirname(os.path.abspath(__file__))

# A manifest of the included packages.
lambda_packages = {
    'bcrypt': {
        'python2.7': {
            'version': '3.1.1',
            'path': os.path.join(PACKAGES_DIR, 'bcrypt', 'python2.7-bcrypt-3.1.1.tar.gz')
        }
    },
    'cffi': {
        'python2.7': {
            'version': '1.7.0',
            'path': os.path.join(PACKAGES_DIR, 'cffi', 'python2.7-cffi-1.7.0.tar.gz')
        }
    },
    'cryptography': {
        'python2.7': {
            'version': '2.3.1',
            'path': os.path.join(PACKAGES_DIR, 'cryptography', 'python2.7-cryptography-2.3.1.tar.gz')
        },
        'python3.6': {
            'version': '2.3.1',
            'path': os.path.join(PACKAGES_DIR, 'cryptography', 'python3.6-cryptography-2.3.1.tar.gz')
        }
    },
    'cv2': {
        'python2.7': {
            'version': '3.1.0',
            'path': os.path.join(PACKAGES_DIR, 'OpenCV', 'python2.7-OpenCV-3.1.0.tar.gz')
        },
        'python3.6': {
            'version': '3.3.0',
            'path': os.path.join(PACKAGES_DIR, 'OpenCV', 'python3.6-OpenCV-3.3.0.tar.gz')
        }
    },
    'datrie_extended': {
        'python2.7': {
            'version': '0.7.3',
            'path': os.path.join(PACKAGES_DIR, 'datrie_extended', 'python2.7-datrie_extended-0.7.3.tar.gz')
        }
    },
    'dlib': {
        'python2.7': {
            'version': '19.8.0',
            'path': os.path.join(PACKAGES_DIR, 'dlib', 'python2.7-dlib-19.8.tar.gz')
        },
        'python3.6': {
            'version': '19.8.0',
            'path': os.path.join(PACKAGES_DIR, 'dlib', 'python3.6-dlib-19.8.tar.gz')
        }
    },
    'lxml': {
        'python2.7': {
            'version': '3.6.0',
            'path': os.path.join(PACKAGES_DIR, 'lxml', 'python2.7-lxml-3.6.0.tar.gz')
        }
    },
    'misaka': {
        'python2.7': {
            'version': '2.0.0',
            'path': os.path.join(PACKAGES_DIR, 'misaka', 'python2.7-misaka-2.0.0.tar.gz')
        }
    },
    'MySQL-Python': {
        'python2.7': {
            'version': '1.2.5',
            'path': os.path.join(PACKAGES_DIR, 'MySQL-Python', 'python2.7-MySQL-Python-1.2.5.tar.gz')
        }
    },
    'mysqlclient': {
        'python2.7': {
            'version': '1.3.12',
            'path': os.path.join(PACKAGES_DIR, 'mysqlclient', 'python2.7-mysqlclient-1.3.12.tar.gz')
        },
        'python3.6': {
            'version': '1.3.12',
            'path': os.path.join(PACKAGES_DIR, 'mysqlclient', 'python3.6-mysqlclient-1.3.12.tar.gz')
        }
    },
    'numpy': {
        'python2.7': {
            'version': '1.10.4',
            'path': os.path.join(PACKAGES_DIR, 'numpy', 'python2.7-numpy-1.10.4.tar.gz')
        }
    },
    'Pillow': {
        'python2.7': {
            'version': '3.4.2',
            'path': os.path.join(PACKAGES_DIR, 'Pillow', 'python2.7-Pillow-3.4.2.tar.gz')
        }
    },
    'psycopg2': {
        'python2.7': {
            'version': '2.6.1',
            'path': os.path.join(PACKAGES_DIR, 'psycopg2', 'python2.7-psycopg2-2.6.1.tar.gz')
        }
    },
    'pycrypto': {
        'python2.7': {
            'version': '2.6.1',
            'path': os.path.join(PACKAGES_DIR, 'pycrypto', 'python2.7-pycrypto-2.6.1.tar.gz')
        },
        'python3.6': {
            'version': '2.6.1',
            'path': os.path.join(PACKAGES_DIR, 'pycrypto', 'python3.6-pycrypto-2.6.1.tar.gz')
        }
    },
    'pylibmc': {
        'python2.7': {
            'version': '1.5.2',
            'path': os.path.join(PACKAGES_DIR, 'pylibmc', 'python2.7-pylibmc-1.5.2.tar.gz')
        },
        'python3.6': {
            'version': '1.5.2',
            'path': os.path.join(PACKAGES_DIR, 'pylibmc', 'python3.6-pylibmc-1.5.2.tar.gz')
        }
    },
    'pynacl': {
        'python2.7': {
            'version': '1.0.1',
            'path': os.path.join(PACKAGES_DIR, 'PyNaCl', 'python2.7-PyNaCl-1.0.1.tar.gz')
        }
    },
    'pyodbc': {
        'python2.7': {
            'version': '4.0.21',
            'path': os.path.join(PACKAGES_DIR, 'pyodbc', 'python2.7-pyodbc-4.0.21.tar.gz')
        },
        'python3.6': {
            'version': '4.0.21',
            'path': os.path.join(PACKAGES_DIR, 'pyodbc', 'python3.6-pyodbc-4.0.21.tar.gz')
        }
    },
    'pyproj': {
        'python2.7': {
            'version': '1.9.5',
            'path': os.path.join(PACKAGES_DIR, 'pyproj', 'python2.7-pyproj.4-4.9.2.tar.gz')
        }
    },
    'python-ldap': {
        'python2.7': {
            'version': '3.0.0',
            'path': os.path.join(PACKAGES_DIR, 'python-ldap', 'python2.7-python-ldap-3.0.0.tar.gz')
        },
        'python3.6': {
            'version': '3.0.0',
            'path': os.path.join(PACKAGES_DIR, 'python-ldap', 'python3.6-python-ldap-3.0.0.tar.gz')
        }
    },
    'python-Levenshtein': {
        'python2.7': {
            'version': '0.12.0',
            'path': os.path.join(PACKAGES_DIR, 'python-Levenshtein', 'python2.7-python-Levenshtein-0.12.0.tar.gz'),
        }
    },
    'regex': {
        'python2.7': {
            'version': '2016.8.27',
            'path': os.path.join(PACKAGES_DIR, 'regex', 'python2.7-regex-2016.8.27.tar.gz')
        },
        'python3.6': {
            'version': '2016.8.27',
            'path': os.path.join(PACKAGES_DIR, 'regex', 'python3.6-regex-2016.8.27.tar.gz')
        }
    },
    'sqlite3': {
        'python3.6': {
            'version': '3.6.0',
            'path': os.path.join(PACKAGES_DIR, 'sqlite3', 'python3.6-sqlite3-3.6.0.tar.gz')
        }
    },
    'xmlsec': {
        'python2.7': {
            'version': '1.0.9',
            'path': os.path.join(PACKAGES_DIR, 'xmlsec', 'python2.7-xmlsec-1.0.9.tar.gz')
        },
        'python3.6': {
            'version': '1.0.9',
            'path': os.path.join(PACKAGES_DIR, 'xmlsec', 'python3.6-xmlsec-1.0.9.tar.gz')
        },
        'python3.7': {
            'version': '1.3.3',
            'path': os.path.join(PACKAGES_DIR, 'xmlsec', 'python3.7-xmlsec-1.3.3.tar.gz')
        }
    }
}
