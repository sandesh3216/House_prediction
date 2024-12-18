async function predictPrice() {
    const data = {
        "Lot Area": parseInt(document.getElementById('lot_area').value),
        "Overall Qual": parseInt(document.getElementById('overall_qual').value),
        "Year Built": parseInt(document.getElementById('year_built').value),
        "Gr Liv Area": parseInt(document.getElementById('gr_liv_area').value),
        "Garage Area": parseInt(document.getElementById('garage_area').value),
        "Total Bsmt SF": parseInt(document.getElementById('total_bsmt_sf').value)
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        document.getElementById("result").innerText =
            result.predicted_price
            ? `Predicted Price: $${result.predicted_price}`
            : `Error: ${JSON.stringify(result)}`;
    } catch (error) {
        document.getElementById("result").innerText = 
            `Error: Could not fetch prediction.`;
        console.error(error);
    }
}
