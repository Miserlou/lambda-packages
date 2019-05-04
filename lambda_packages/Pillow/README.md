##Preperation

If you want the finished Pillow `3.1.1.tar.gz` and `test.zip` sent to a bucket after it is created, please set the `bucket` and `region` variables at the top of the script:

```

dir="pillow-build"
bucket="<YOUR BUCKET>"
region="<YOUR REGION>"

```
Optionally, you can also set a directory.
The EC2 instance will need the correct IAM role to perform this action.


##Build

Report from `pip install --verbose pillow`

```

PIL SETUP SUMMARY
--------------------------------------------------------------------
version      Pillow 3.1.1
platform     linux2 2.7.10 (default, Dec  8 2015, 18:25:23)
             [GCC 4.8.3 20140911 (Red Hat 4.8.3-9)]
--------------------------------------------------------------------
*** TKINTER support not available
--- JPEG support available
*** OPENJPEG (JPEG2000) support not available
--- ZLIB (PNG/ZIP) support available
--- LIBTIFF support available
--- FREETYPE2 support available
--- LITTLECMS2 support available
--- WEBP support available
*** WEBPMUX support not available
--------------------------------------------------------------------

```

You can build your own by adding `build.sh` to Instance Details > Advanced Details > User Data field in the EC2 launch dashboard.

##Unit Test

The `build.sh` will also build a `test.zip` including `test.py` and `test.jpg` for unit testing on Lambda.

Create a Lambda function using your prefered method.

Exectuting the default test event should return the following:

```json

{
  "size": {
    "width": 864,
    "height": 648
  },
  "mode": "RGB",
  "format": "JPEG"
}

```

##About

Authored by [James MacDonald](https://github.com/jDmacD)

The MIT License (MIT)

Copyright (c) 2016 James MacDonald

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
