# psycopg2

postgreSQL 9.5.1
psycopg2 python2.7: 2.6.1 and python3.6: 2.7.1

Instructions (via [jkehler](https://github.com/jkehler/awslambda-psycopg2)):

* Downloaded the Postgresql 9.4.3 source code and extracted it.
* Downloaded the psycopg2 source and extracted it.
* Went into the Postgresql source directory and did "./configure --prefix {path_to_pg_source_dir} --without-readline --without-zlib" followed by "make" followed by "make install". This generated a pg_config file in a bin directory.
* I then went into the psycopg2 directory and edited the setup.cfg file and set pg_config={path_to_pg_source/bin/pg_config} and static_libpq=1
* Then execute python setup.py build and copied the resulting psycopg2 package from the build directory into my local machine and bundle it inside the AWS package.
