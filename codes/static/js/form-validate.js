

const validators = [];

$(() => {
    // -------------------- for component BoxSelect --------------------
    $(".checkbox-group").map((_, elem) => {
        const checkboxError = $(elem).children('[role="alert"]');
        const minChecked = Number(elem.dataset["min"]);
        const maxChecked = Number(elem.dataset["max"]);
        const validate = () => {
            console.log("validating")
            const num_checked = $(elem).find('input[type="checkbox"]:checked').length;
            if (num_checked < minChecked || num_checked > maxChecked) {
                checkboxError.css("display", "block");
                return false;
            } else {
                checkboxError.css("display", "none");
                return true;
            }
        }
        console.log($(elem).find('input[type="checkbox"]'))

        // create listeners
        $(elem).find('input[type="checkbox"]').click(() => { validate(); });
        validators.push(validate);
    })
});

function validateForm() {
    for (const validator of validators) {
        if (validator() === false) {
            return false;
        }
    }
    return true;
}
