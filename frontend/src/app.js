const apiUrl = "http://localhost:5000";

async function fetchCars() {
    const response = await fetch(`${apiUrl}/cars`);
    const cars = await response.json();
    const carList = document.getElementById("car-list");
    carList.innerHTML = cars.map(car => `
        <li>${car.model} - $${car.price_per_day}/day ${car.available ? "" : "(Not Available)"}</li>
    `).join("");
}

document.getElementById("car-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const model = document.getElementById("car-model").value;
    const price = document.getElementById("car-price").value;
    await fetch(`${apiUrl}/cars`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ model, price_per_day: parseFloat(price) })
    });
    fetchCars();
});

fetchCars();