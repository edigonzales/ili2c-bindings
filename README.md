# ili2c-bindings

This repository provides Node.js and Python bindings for the [ili2c](https://github.com/claeis/ili2c) compiler, enabling users to interact with the ili2c compiler directly from JavaScript and Python applications. 

In this repository, some of the ili2c compiler's Java methods are compiled into a native shared library using GraalVM, making it accessible to both Node.js and Python environments.

## Project Structure

The repository is organized into three main directories:

- `java-lib/`: Contains the Java code and methods that interact with the ILI2C compiler. These methods are compiled to a native shared library using GraalVM.
- `nodejs/`: Contains the Node.js bindings for the native shared library.
- `python/`: Contains the Python bindings for the native shared library.

## Usage Examples

### Node.js Example

Here is a basic example of how to use the ILI2C compiler via the Node.js bindings:

```javascript
const ili2c = require('ili2c'); // Import the ili2c binding

// Example function to run the compiler
async function compileILI2C() {
    try {
        const result = await ili2c.compile('/path/to/ili/file.ili');
        console.log('Compilation Result:', result);
    } catch (error) {
        console.error('Error during compilation:', error);
    }
}

compileILI2C();
