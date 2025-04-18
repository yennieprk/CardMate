$(document).ready(function() {
    $("#add-card-form").submit(function(event) {
        event.preventDefault();

        let newCard = {
            name: $("#name").val().trim(),
            issuer: $("#issuer").val().trim(),
            reward_type: $("#reward_type").val().trim(),
            annual_fee: $("#annual_fee").val().trim(),
            credit_score_required: $("#credit_score").val().trim(),
            interest_rate: $("#interest_rate").val().trim(),
            image: $("#image_url").val().trim(),
            apply_link: $("#apply_link").val().trim(),
            benefits: $("#benefits").val().trim()
        };

        if (Object.values(newCard).some(val => val === "")) {
            alert("All fields are required.");
            return;
        }

        $.ajax({
            url: "/add",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(newCard),
            success: function(response) {
                alert(response.message);
                window.location.href = "/view/" + response.card.id;
            },
            error: function(xhr) {
                alert(xhr.responseJSON.error);
            }
        });
    });


    // 🔹 Edit Credit Card
    $("#edit-card-form").submit(function(event) {
        event.preventDefault();
        let cardId = $("#card-id").val();
        let updatedCard = {
            name: $("#name").val().trim(),
            issuer: $("#issuer").val().trim(),
            reward_type: $("#reward_type").val().trim(),
            annual_fee: $("#annual_fee").val().trim(),
            credit_score_required: $("#credit_score").val().trim(),
            interest_rate: $("#interest_rate").val().trim(),
            image: $("#image_url").val().trim(),
            apply_link: $("#apply_link").val().trim(),
            benefits: $("#benefits").val().trim()
        };
    
        if (Object.values(updatedCard).some(val => val === "")) {
            alert("All fields are required.");
            return;
        }
    
        $.ajax({
            url: "/edit/" + cardId,
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(updatedCard),
            success: function(response) {
                alert(response.message);
                window.location.href = "/view/" + response.card.id;
            },
            error: function(xhr) {
                alert(xhr.responseJSON.error);
            }
        });
    });
    
    // Confirm discard changes
    $("#discard-changes").click(function(event) {
        event.preventDefault();
        if (confirm("Discard changes?")) window.history.back();
    });    
});

function compareCards() {
    const card1Id = document.getElementById('card1').value;
    const card2Id = document.getElementById('card2').value;

    if (!card1Id || !card2Id) {
        alert('Please select two cards to compare');
        return;
    }

    if (card1Id === card2Id) {
        alert('Please select different cards to compare');
        return;
    }

    window.location.href = `/compare/${card1Id}/${card2Id}`;
}
