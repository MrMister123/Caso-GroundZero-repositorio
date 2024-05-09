const header = document.querySelector("header");
const footer = document.querySelector("footer");

header.innerHTML = 
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="Menu.html">
                <img src="img/Logo.webp" alt="GroundZero" width="40" height="35"></img>
            </a>
            <a class="navbar-brand" href="Menu.html">Ground Zero</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="Menu.html">Inicio</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="REGISTER.html">Registro</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="VistaArtistas.html">Artistas</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="VistaMercado.html">Mercado</a>
                </li>
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                    Articulos
                    </a>
                    <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="VistaCarrusel.html">Pinceles</a></li>
                    <li><a class="dropdown-item" href="VistaCarrusel.html">Pinturas</a></li>
                    <li><a class="dropdown-item" href="VistaCarrusel.html">Atriles</a></li>
                    <li><a class="dropdown-item" href="VistaCarrusel.html">Telas</a></li>
                    </ul>
                </li>
                <form class="d-flex" role="search">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"></input>
                    <button class="btn btn-outline-success" type="submit">Buscar</button>
                </form>
                <div class="position-absolute top-30 end-0">
                    <a class="btn btn-outline-success" href="LOGIN.html" role="button">Inicio Sesion</a>  
                </div>
                </ul> 
            </div>
        </div>
    </nav> 
;

footer.innerHTML = 
a
;