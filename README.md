### El Problema

La fuerza aérea nazi intenta transmitir números (quizás representando unidades militares o inventario disponible) por radio. El código Enigma acaba de ser descifrado, así que buscan una solución de lápiz y papel para enviar estos números de manera secreta. Deciden codificarlos en una base arbitraria usando símbolos arbitrarios para representar los números. Lo bueno es que solo nos importa el orden de magnitud de estos números y sus valores mínimos y máximos posibles.

Se te proporciona una cadena con caracteres de la `a` a la `z` que representa un número. No sabes con certeza en qué base está ni qué dígito representa cada carácter en esa base. Sin embargo, sabes que todos los dígitos de la base están presentes solo una vez en la cadena de entrada.

Tu tarea es calcular la diferencia entre los valores mínimo y máximo posibles. Ten en cuenta que los números nunca tienen ceros a la izquierda.

### Entrada

La primera línea contiene un entero, `T`, que indica el número de casos de prueba. Para cada caso, hay una línea con una cadena de caracteres en minúsculas, `S`.

### Salida

Para cada caso, imprime:  
`Case #x: ` seguido de la diferencia entre los valores mínimo y máximo posibles, como un valor decimal.

### Límites

- $$( 2 \leq \text{length}(S) \leq 26 \)$$


### Sample input
3
bfd
xwyz
qwerty

### Sample output
Case #1: 10
Case #2: 153
Case #3: 36445


### Ejemplo Explicado

En el primer caso (`bfd`), estas son todas las posibilidades y sus valores. Cada carácter de `bfd` representa un dígito en base 3, por lo que los dígitos posibles son 0, 1 y 2. Ahora sustituimos cada letra por un dígito (por ejemplo, `b->1`, `d->2`, `f->0`, lo que da como resultado `102`). Para convertir `102` de base 3 a base 10, el cálculo es:  

$$[1 \cdot 3^2 + 0 \cdot 3^1 + 2 \cdot 3^0 = 11\]$$

Siguiendo la misma lógica, podemos crear una tabla con todos los valores:  

| Número | Valor Decimal |
|--------|---------------|
| 102    | 11            |
| 120    | 15            |
| 210    | 21            |
| 201    | 19            |

El valor máximo es 21 y el mínimo es 11, por lo que la solución es $$( 21 - 11 = 10 )$$.  

Recuerda que los números con ceros a la izquierda no están permitidos, por lo que `012` y `021` no son válidos.  

## Requisitos

1. Usa Python 3.7.
2. Escribe código conforme a PEP8.
3. Escribe algunas pruebas (considera usar pytest o uniitest).
4. Documenta tu solución en un archivo.
