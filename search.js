// Configuration de Typesense
const TYPESENSE_API_URL = 'http://localhost:8108';
const TYPESENSE_API_KEY = 'moiscroquer9';

const collections = ['recommendations', 'questions', 'food', 'articles', 'recipes']; // Liste de vos collections

function search() {
    let query = document.getElementById('searchBox').value;
    let searchPromises = collections.map(collection => searchInCollection(collection, query));
    Promise.all(searchPromises)
        .then(allResults => {
            let consolidatedResults = allResults.flat();
            displayResults(consolidatedResults);
            displayResults_json(consolidatedResults);
        });
}

function searchInCollection(collection, query) {
    return fetch(`${TYPESENSE_API_URL}/collections/${collection}/documents/search?q=${query}&query_by=*&x-typesense-api-key=${TYPESENSE_API_KEY}`)
        .then(response => response.json())
        .then(data => data.hits || []);
}


function displayResults_json(results) {
    let resultsDiv = document.getElementById('results_json');
    // Convertir l'objet de résultats en une chaîne JSON avec une indentation pour une meilleure lisibilité
    let jsonString = JSON.stringify(results, null, 2);
    // Utiliser un élément <pre> pour conserver le formatage du JSON
    resultsDiv.innerHTML = `<pre>${jsonString}</pre>`;
}

function displayResults(results) {
    let resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';
    
    results.forEach(hit => {
        // Modifiez cette partie selon la structure de vos données
        resultsDiv.innerHTML += `<div class="answer"><h4>${hit.document.title || ''}</h4><div class="content">${hit.document.content || ''}</div></div>`;
    });
}

