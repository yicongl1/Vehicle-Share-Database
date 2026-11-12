function query() {
    // File
    let vFile = document.getElementById("myfile").files[0];
    // Reader
    let vReader = new FileReader();
    vReader.readAsText(vFile);
    vReader.onload = function(pEvent) {
        // String Input
        let vContent = pEvent.target.result;
        // JSON to object
        let vJson = JSON.parse(vContent);
        // Query
        let vResult = vJson.prenom + " " + vJson.nom + " (" + vJson.age + ")";
        // Adding addresses
        for (let i = 0; i < vJson.adresse.length; i++) {
            vResult += " " + vJson.adresse[i];
        }
        // Output
        document.getElementById("mydiv").appendChild(document.createTextNode(vResult));
    };
}
