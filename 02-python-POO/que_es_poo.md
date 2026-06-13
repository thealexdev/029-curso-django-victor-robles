## Resumen de la clase: Programación Orientada a Objetos (POO)

La **Programación Orientada a Objetos (POO)** es un paradigma de programación que consiste en representar los elementos del software como  **objetos** , similares a entidades del mundo real. Su principal objetivo es crear código más  **organizado, reutilizable, mantenible y escalable** .

### Conceptos principales

### 1. Clases

Una **clase** es una plantilla o molde que define cómo serán los objetos.

Ejemplo:

* Clase: `Coche`
* A partir de ella se pueden crear muchos coches diferentes.

### 2. Atributos o propiedades

Son las características que tendrá un objeto.

Ejemplo de un coche:

* Marca
* Modelo
* Color
* Número de puertas
* Caballos de fuerza

Son equivalentes a las variables dentro de una clase.

### 3. Métodos

Son las acciones que puede realizar un objeto.

Ejemplo de un coche:

* Arrancar
* Frenar
* Acelerar
* Encender luces
* Cambiar de marcha

Son equivalentes a funciones definidas dentro de una clase.

### 4. Objetos

Son instancias creadas a partir de una clase.

Por ejemplo:

* BMW X5 negro
* Seat Panda rojo

Ambos son objetos de tipo `Coche`, pero con diferentes valores en sus atributos.

---

## Principios fundamentales de la POO

### Abstracción

Permite utilizar un objeto sin necesidad de conocer cómo funciona internamente.

Solo se utilizan sus métodos y funcionalidades públicas, ocultando los detalles de implementación. Esto facilita reutilizar código para muchos casos diferentes.

### Herencia

Permite que una clase herede atributos y métodos de otra.

Ejemplo:

```
Vehículo
├── Coche
├── Moto
├── Camión
└── Autobús
```

La clase `Vehículo` contiene características generales y las clases hijas agregan funcionalidades específicas.

### Modularidad

Consiste en dividir una aplicación en pequeñas partes independientes.

Por ejemplo, en una aplicación web podrían existir clases para:

* Usuario
* Producto
* Comentario
* Pedido

Cada clase se encarga de una responsabilidad específica, haciendo el sistema más ordenado y fácil de mantener.

### Encapsulación u ocultación

Los datos internos de un objeto deben protegerse para evitar modificaciones incorrectas desde fuera de la clase.

Para acceder o modificar esos datos se suelen utilizar:

* Getters → obtener valores
* Setters → modificar valores

Esto mejora la seguridad y el control sobre los datos del objeto.

---

## Resumen rápido para entrevista técnica

**POO = paradigma donde todo se modela como objetos.**

Elementos clave:

* **Clase:** plantilla o molde.
* **Objeto:** instancia de una clase.
* **Atributos:** características del objeto.
* **Métodos:** acciones del objeto.
* **Abstracción:** ocultar complejidad.
* **Herencia:** reutilizar características entre clases.
* **Modularidad:** dividir el sistema en componentes.
* **Encapsulación:** proteger datos internos.

### Ejemplo sencillo

```python
class Coche:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def arrancar(self):
        print("El coche ha arrancado")

mi_coche = Coche("BMW", "Negro")
mi_coche.arrancar()
```

Aquí:

* `Coche` → Clase
* `marca` y `color` → Atributos
* `arrancar()` → Método
* `mi_coche` → Objeto

Este ejemplo resume prácticamente toda la explicación de la clase.
