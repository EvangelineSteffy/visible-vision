const chat =
    document.getElementById("chat");

const form =
    document.getElementById("askForm");

const input =
    document.getElementById("message");

const speakBtn =
    document.getElementById("speakBtn");

const mainSpeakBtn =
    document.getElementById("mainSpeakBtn");


/* ADD MESSAGE */

function addMessage(text, who) {

    const box =
        document.createElement("div");

    box.className =
        `message ${who}`;


    const label =
        document.createElement("strong");

    label.textContent =
        who === "user"
            ? "நீங்கள்:"
            : "visible vision:";


    const content =
        document.createElement("div");

    content.textContent = text;


    box.appendChild(label);

    box.appendChild(content);

    chat.appendChild(box);


    chat.scrollTop =
        chat.scrollHeight;
}


/* ASK QUESTION */

async function askQuestion(question) {

    const text =
        question.trim();


    if (!text) {
        return;
    }


    addMessage(
        text,
        "user"
    );


    input.value = "";


    try {

        const response =
            await fetch(
                "/api/ask",
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        message: text
                    })
                }
            );


        const data =
            await response.json();


        const answer =
            data.answer ||
            "மன்னிக்கவும். பதில் கிடைக்கவில்லை.";


        addMessage(
            answer,
            "bot"
        );


        speakTamil(answer);


    } catch (error) {

        console.error(error);

        addMessage(
            "சேவையகத்துடன் இணைக்க முடியவில்லை. Python server இயங்குகிறதா என்பதை சரிபார்க்கவும்.",
            "bot"
        );

    }
}


/* TEXT FORM */

form.addEventListener(
    "submit",
    function(event) {

        event.preventDefault();

        askQuestion(
            input.value
        );

    }
);


/* ALL QUICK BUTTONS */

document
    .querySelectorAll(
        "[data-question]"
    )
    .forEach(
        function(button) {

            button.addEventListener(
                "click",
                function() {

                    askQuestion(
                        button.dataset.question
                    );

                }
            );

        }
    );


/* TAMIL VOICE OUTPUT */

function speakTamil(text) {

    if (
        !("speechSynthesis" in window) ||
        !text
    ) {
        return;
    }


    window.speechSynthesis.cancel();


    const utterance =
        new SpeechSynthesisUtterance(
            text
        );


    utterance.lang =
        "ta-IN";


    utterance.rate =
        0.9;


    window.speechSynthesis.speak(
        utterance
    );
}


/* SPEECH RECOGNITION */

const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;


if (SpeechRecognition) {

    const recognition =
        new SpeechRecognition();


    recognition.lang =
        "ta-IN";


    recognition.interimResults =
        false;


    recognition.continuous =
        false;


    recognition.onstart =
        function() {

            speakBtn.textContent =
                "🔴 கேட்கிறது...";

            mainSpeakBtn.textContent =
                "🔴 கேட்கிறது...";

            speakBtn.classList.add(
                "recording"
            );

            mainSpeakBtn.classList.add(
                "recording"
            );

        };


    recognition.onend =
        function() {

            speakBtn.textContent =
                "🎙️ பேசுங்கள்";

            mainSpeakBtn.textContent =
                "🎙️ தமிழில் பேசித் தேடுங்கள்";

            speakBtn.classList.remove(
                "recording"
            );

            mainSpeakBtn.classList.remove(
                "recording"
            );

        };


    recognition.onerror =
        function() {

            speakBtn.textContent =
                "🎙️ பேசுங்கள்";

            mainSpeakBtn.textContent =
                "🎙️ தமிழில் பேசித் தேடுங்கள்";

            speakBtn.classList.remove(
                "recording"
            );

            mainSpeakBtn.classList.remove(
                "recording"
            );

        };


    recognition.onresult =
        function(event) {

            const spokenText =
                event.results[0][0]
                    .transcript;


            input.value =
                spokenText;


            askQuestion(
                spokenText
            );

        };


    function startVoice() {

        try {

            recognition.start();

        } catch (error) {

            console.log(
                "Voice already running."
            );

        }

    }


    speakBtn.addEventListener(
        "click",
        startVoice
    );


    mainSpeakBtn.addEventListener(
        "click",
        startVoice
    );


} else {

    function voiceNotAvailable() {

        alert(
            "உங்கள் browser-ல் voice recognition கிடைக்கவில்லை. Chrome-ல் முயற்சி செய்யவும்."
        );

    }


    speakBtn.addEventListener(
        "click",
        voiceNotAvailable
    );


    mainSpeakBtn.addEventListener(
        "click",
        voiceNotAvailable
    );

}