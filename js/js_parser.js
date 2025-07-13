// js_autocomplete.js
const esprima = require('esprima');

const stdin = process.stdin;
let code = '';

stdin.setEncoding('utf8');
stdin.on('data', chunk => code += chunk);
stdin.on('end', () => {
    try {
        const ast = esprima.parseScript(code, { tolerant: true });

        const suggestions = new Set();

        function traverse(node) {
            if (!node || typeof node !== 'object') return;
            if (node.type === 'VariableDeclaration') {
                for (const decl of node.declarations) {
                    if (decl.id && decl.id.name) {
                        suggestions.add(decl.id.name);
                    }
                }
            }
            if (node.type === 'FunctionDeclaration' && node.id) {
                suggestions.add(node.id.name);
            }
            for (const key in node) {
                traverse(node[key]);
            }
        }

        traverse(ast);

        console.log(JSON.stringify(Array.from(suggestions)));
    } catch (e) {
        console.log('[]');
    }
});
