function searchArtworks() {
    const keyword = document.getElementById("searchInput").value;
    const url = `https://collectionapi.metmuseum.org/public/collection/v1/search?q=${keyword}`;

    fetch(url)
    .then(response => response.json())
    .then(data => {
        const objectIDs = data.objectIDs;
        const artworksDiv = document.getElementById("artworks");
        artworksDiv.innerHTML = "";

        objectIDs.slice(0, 5).forEach(objectID => {
            fetch(`https://collectionapi.metmuseum.org/public/collection/v1/objects/${objectID}`)
            .then(response => response.json())
            .then(artwork => {
                const artworkDiv = document.createElement("div");
                artworkDiv.classList.add("artwork");

                const title = document.createElement("h2");
                title.textContent = artwork.title;
                artworkDiv.appendChild(title);

                const artist = document.createElement("p");
                artist.textContent = `Artista: ${artwork.artistDisplayName}`;
                artworkDiv.appendChild(artist);

                const date = document.createElement("p");
                date.textContent = `Fecha: ${artwork.objectDate}`;
                artworkDiv.appendChild(date);

                const img = document.createElement("img");
                img.src = artwork.primaryImage;
                artworkDiv.appendChild(img);

                artworksDiv.appendChild(artworkDiv);
            });
        });
    })
    .catch(error => console.error("Error al buscar obras de arte:", error));
}
