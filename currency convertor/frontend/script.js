function convertCurrency() {
    let amount = document.getElementById("amount").value;
    let currency = document.getElementById("currency").value;
    let result = document.getElementById("result");

    if (amount === "" || amount <= 0) {
        result.innerHTML = "❌ Please enter a valid amount!";
        return;
    }

    fetch(`http://127.0.0.1:5000/convert?amount=${amount}&currency=${currency}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                result.innerHTML = "❌ Invalid currency!";
            } else {
                result.innerHTML = `✅ Converted Amount: <strong>${data.converted_amount} ${data.currency}</strong>`;
            }
        })
        .catch(error => {
            result.innerHTML = "⚠️ Error fetching exchange rates!";
        });
}
