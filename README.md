# ili2c-bindings

This repository provides Node.js and Python bindings for the [ili2c](https://github.com/claeis/ili2c) compiler, enabling users to interact with the ili2c compiler directly from JavaScript and Python applications. 

In this repository, some of the ili2c compiler's Java methods are compiled into a native shared library using GraalVM, making it accessible to both Node.js and Python environments.

## Project Structure

The repository is organized into three main directories:

- `java-lib/`: Contains the Java code and methods that interact with the ili2c compiler. These methods are compiled to a native shared library using GraalVM.
- `nodejs/`: Contains the Node.js bindings for the native shared library.
- `python/`: Contains the Python bindings for the native shared library.

## Usage Examples

### Node.js Examples

Here are basic examples of how to use the ili2c compiler via the Node.js bindings:

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

```python
# Compile model
from ili2c import Ili2c
result = Ili2c.compile_model("test/Test1.ili", log_file)
print(result)

# Pretty print model
from ili2c import Ili2c
result = Ili2c.pretty_print("test/Test1.ili")
print(result)

# Generate model as IlisMeta16 INTERLIS transfer
from ili2c import Ili2c
xtf_file = os.path.join(tmpdir, 'Test1.xtf')
result = Ili2c.create_ilismetas16("test/Test1.ili", xtf_file)
```