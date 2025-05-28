
#[id, nombre, detalle, precio]

productos = [
    ["001", "telefono","detalle",100],
    ["002", "telefono","detalle",100],
    ["003", "telefo","detalle",100],
    ["004", "telefono","detalle",100]
]


productos.append(["005", "telefono","detalle",100])

productos[0][1] = "telefono"

productos[2][1] = "telefono"

navidad = ["8","navidad","nuevo",100]
navidad2 = ["9","cena navidad","nuevo",100]



print(productos)