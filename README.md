# ili2c-bindings

This repository provides Node.js and Python bindings for the [ili2c](https://github.com/claeis/ili2c) compiler, enabling users to interact with the ili2c compiler directly from JavaScript and Python applications. 

In this repository, some of the ili2c compiler's Java methods are compiled into a native shared library using GraalVM, making it accessible to both Node.js and Python environments.

## Project Structure

The repository is organized into three main directories:

- `java-lib/`: Contains the Java code and methods that interact with the ili2c compiler. These methods are compiled to a native shared library using GraalVM.
- `nodejs/`: Contains the Node.js bindings for the native shared library.
- `python/`: Contains the Python bindings for the native shared library.

## Dependencies

The native shared library still relies on _libc_ and _zlib_:

```bash
ldd libili2c.so

	linux-vdso.so.1 (0x00007f5b53e24000)
	libz.so.1 => /lib/x86_64-linux-gnu/libz.so.1 (0x00007f5b51974000)
	libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f5b51600000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f5b53e26000)
```

But it should work on most (debian/ubuntu) Linux systems, macOS and Windows out of the box. See: https://www.graalvm.org/latest/reference-manual/native-image/guides/build-static-executables/

## Usage Examples

### Node.js Examples

Here are basic examples of how to use the ili2c compiler via the Node.js bindings:

```bash
npm install ili2c
```

```javascript
// Compile model
const ili2c = require('ili2c');
const result = ili2c.compileModel("test/Test1.ili", "ili2c.log");
console.log(result);

// Pretty print model
const ili2c = require('ili2c');
const result = ili2c.prettyPrint("test/Test1.ili");
console.log(result);
```

### Python Example

Here are basic examples of how to use the ili2c compiler via the Python bindings:

```bash
pip install ili2c
```

```python
# Compile model
from ili2c import Ili2c
result = Ili2c.compile_model("test/Test1.ili", "ili2c.log")
print(result)

# Pretty print model
from ili2c import Ili2c
result = Ili2c.pretty_print("test/Test1.ili")
print(result)

# Generate model as IlisMeta16 INTERLIS transfer
from ili2c import Ili2c
result = Ili2c.create_ilismetas16("test/Test1.ili", 'Test1.xtf')
```