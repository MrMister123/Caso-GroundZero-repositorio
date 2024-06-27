const carrito = [];
let descuentoAplicado = false;

function agregarAlCarrito(nombre, precio) {
    carrito.push({ nombre, precio });
    actualizarCarrito();
    
}

function removerDelCarrito(index) {
    carrito.splice(index, 1);
    actualizarCarrito();
}

function actualizarCarrito() {
    const carritoDiv = document.getElementById('carrito');
    carritoDiv.innerHTML = '';

    if (carrito.length === 0) {
        carritoDiv.innerHTML = '<p>No hay productos seleccionados</p>';
    } else {
        const lista = document.createElement('ul');
        let total = 0;

        carrito.forEach((item, index) => {
            const li = document.createElement('li');
            li.textContent = `${item.nombre} - $${item.precio}`;
            const botonEliminar = document.createElement('button');
            botonEliminar.textContent = 'Eliminar';
            botonEliminar.onclick = () => removerDelCarrito(index);
            li.appendChild(botonEliminar);
            lista.appendChild(li);
            total += item.precio;
        });

        carritoDiv.appendChild(lista);

     // 18% solo para que funcione
        const impuesto = total * 0.18;  
        total += impuesto;
    //  10% solo para que funcione
        if (descuentoAplicado) {
            total *= 0.9;  
        }

        const totalDiv = document.createElement('div');
        totalDiv.textContent = `Impuesto: $${impuesto.toFixed(2)} - Total: $${total.toFixed(2)}`;
        carritoDiv.appendChild(totalDiv);

        document.getElementById('total').textContent = total.toFixed(2);
    }
}

function aplicarDescuento() {
    const codigoDescuento = document.getElementById('descuento').value;
    if (codigoDescuento === 'GROUNDZERO') {
        descuentoAplicado = true;
        actualizarCarrito();
    } else {
        alert('Código de descuento no válido.');
    }
}

function pagar() {
    if (carrito.length === 0) {
        alert('No hay productos en el carrito para pagar.');
        return;
    }

    const total = document.getElementById('total').textContent;
    alert(`Gracias por tu compra. El total a pagar es $${total}.`);

    // Limpia el carrito después del pago
    carrito.length = 0;
    descuentoAplicado = false;
    document.getElementById('descuento').value = '';
    actualizarCarrito();
}
