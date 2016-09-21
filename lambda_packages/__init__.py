import os

# A manifest of the included packages.
lambda_packages = {
    'cffi': {
        'version': '1.7.0',
        'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'cffi', 'cffi-1.7.0.tar.gz')
    },
    'cv2': {
        'version': '3.1.0',
        'path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'OpenCV', 'OpenCV-3.1.0.tar.gz')
    },
    'lxml': {
        'version': '3.6.0',
        'path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lxml', 'lxml-3.6.0.tar.gz')
    },
    'MySQL-Python': {
        'version': '1.2.5',
        'path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'MySQL-Python', 'MySQL-Python-1.2.5.tar.gz')
    },
    'numpy': {
        'version': '1.10.4',
        'path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'numpy', 'numpy-1.10.4.tar.gz')
    },
    'Pillow':{
    	'version':'3.1.1',
    	'path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Pillow', 'Pillow-3.1.1.tar.gz')
    },
    'psycopg2': {
        'version': '2.6.1',
        'path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'psycopg2', 'psycopg2-2.6.1.tar.gz')
    },
    'pycrypto': {
        'version': '2.6.1',
        'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'pycrypto', 'pycrypto-2.6.1.tar.gz')
    },
    'pynacl': {
        'version': '1.0.1',
        'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'PyNaCl', 'PyNaCl-1.0.1.tar.gz')
    },
    'cryptography': {
        'version': '1.4',
        'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'cryptography', 'cryptography-1.4.tar.gz')
    },
    'GDAL': {
        'version': '2.0.0',
        'path': os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'GDAL', 'gdal-2.0.0-amz1.tar.gz')
    }


}
