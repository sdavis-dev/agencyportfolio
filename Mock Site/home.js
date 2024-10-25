function calculateTotal(event) {
    event.preventDefault(); // Prevent form submission

    // Retrieve form data
    const espresso = parseFloat(document.getElementById('espresso').value) * 3.50;
    const cappuccino = parseFloat(document.getElementById('cappuccino').value) * 4.00;
    const latte = parseFloat(document.getElementById('latte').value) * 4.50;
    const honeyCinnamonLatte = parseFloat(document.getElementById('honey-cinnamon-latte').value) * 5.00;
    const herbalTeas = parseFloat(document.getElementById('herbal-teas').value) * 3.00;
    const avocadoToast = parseFloat(document.getElementById('avocado-toast').value) * 6.50;
    const yogurtBowl = parseFloat(document.getElementById('yogurt-bowl').value) * 7.00;
    const breakfastCroissant = parseFloat(document.getElementById('breakfast-croissant').value) * 5.50;
    const oatmeal = parseFloat(document.getElementById('oatmeal').value) * 5.00;
    const pancakes = parseFloat(document.getElementById('pancakes').value) * 8.00;
    const grilledCheese = parseFloat(document.getElementById('grilled-cheese').value) * 9.00;
    const quinoaSalad = parseFloat(document.getElementById('quinoa-salad').value) * 8.50;
    const chickenWrap = parseFloat(document.getElementById('chicken-wrap').value) * 10.00;
    const veganPesto = parseFloat(document.getElementById('vegan-pesto').value) * 9.50;
    const veggieSandwich = parseFloat(document.getElementById('veggie-sandwich').value) * 8.00;
    const honeyCake = parseFloat(document.getElementById('honey-cake').value) * 6.00;
    const lavenderMacarons = parseFloat(document.getElementById('lavender-macarons').value) * 5.00;
    const cookies = parseFloat(document.getElementById('cookies').value) * 3.00;
    const cheesecake = parseFloat(document.getElementById('cheesecake').value) * 7.00;
    const cinnamonRolls = parseFloat(document.getElementById('cinnamon-rolls').value) * 4.50;

    // Calculate total
    const subtotal = espresso + cappuccino + latte + honeyCinnamonLatte + herbalTeas +
        avocadoToast + yogurtBowl + breakfastCroissant + oatmeal + pancakes +
        grilledCheese + quinoaSalad + chickenWrap + veganPesto + veggieSandwich +
        honeyCake + lavenderMacarons + cookies + cheesecake + cinnamonRolls;

    const salesTax = subtotal * 0.07; // 7% sales tax
    const total = subtotal + salesTax;

    // Alert the user with confirmation details
    const customerName = document.getElementById('name').value; // Get the customer's name
    alert(`Order confirmed, ${customerName}!\n\nTotal: $${total.toFixed(2)} (including $${salesTax.toFixed(2)} sales tax)`);
    
    // Here you can add code to send the data to the restaurant
    // For example, using fetch or XMLHttpRequest to send data to a server endpoint.
}