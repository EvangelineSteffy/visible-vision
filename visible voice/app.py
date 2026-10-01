import json
import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse


HOST = "127.0.0.1"
PORT = 5000

OFFICIAL_URL = "https://www.pmuy.gov.in/"


def tamil_answer(message):

    text = (message or "").strip().lower()

    # Eligibility
    if any(k in text for k in [
        "தகுதி",
        "யார்",
        "தகுதியான",
        "eligible",
        "eligibility"
    ]):

        return (
            "தகுதி திட்டத்தைப் பொறுத்து மாறும். 🌸\n\n"

            "தயவுசெய்து இந்த வழிமுறைகளைப் பின்பற்றுங்கள்:\n\n"

            "1. அதிகாரப்பூர்வ அரசு இணையதளத்தைத் திறக்கவும்.\n"
            "2. அந்தத் திட்டத்தின் தற்போதைய தகுதி விதிகளைப் பார்க்கவும்.\n"
            "3. தேவையான ஆவணங்களைச் சரிபார்க்கவும்.\n"
            "4. அதிகாரப்பூர்வ வழிமுறைகளின்படி விண்ணப்பிக்கவும்.\n\n"

            "⚠️ முக்கியம்:\n"
            "Aadhaar எண், OTP, கடவுச்சொல் அல்லது வங்கி PIN-ஐ "
            "visible vision-ல் பகிர வேண்டாம்.\n\n"

            "அதிகாரப்பூர்வ PMUY இணையதளம்:\n"
            + OFFICIAL_URL
        )


    # Documents
    if any(k in text for k in [
        "ஆவணம்",
        "டாக்குமெண்ட்",
        "documents",
        "document"
    ]):

        return (
            "தேவையான ஆவணங்கள் திட்டத்தைப் பொறுத்து மாறலாம். 📄\n\n"

            "பொதுவாக:\n\n"

            "1. அதிகாரப்பூர்வ திட்டப் பக்கத்தைத் திறக்கவும்.\n"
            "2. 'Eligibility' பகுதியைப் பார்க்கவும்.\n"
            "3. 'Documents Required' பகுதியைப் பார்க்கவும்.\n"
            "4. அதிகாரப்பூர்வமாக குறிப்பிடப்பட்டுள்ள "
            "ஆவணங்களை மட்டும் தயாராக வைத்துக்கொள்ளவும்.\n\n"

            "Aadhaar எண், OTP, கடவுச்சொல் அல்லது வங்கி PIN-ஐ "
            "visible vision-ல் பகிர வேண்டாம்."
        )


    # Application
    if any(k in text for k in [
        "விண்ணப்ப",
        "apply",
        "எப்படி",
        "செய்வது",
        "application"
    ]):

        return (
            "விண்ணப்பிக்கும் பொதுவான நடைமுறை: 📝\n\n"

            "1. அதிகாரப்பூர்வ அரசு இணையதளத்தைத் திறக்கவும்.\n"
            "2. தகுதியைச் சரிபார்க்கவும்.\n"
            "3. தேவையான ஆவணங்களைச் சரிபார்க்கவும்.\n"
            "4. அதிகாரப்பூர்வ விண்ணப்ப முறையைப் பின்பற்றவும்.\n"
            "5. விண்ணப்ப நிலையை அதிகாரப்பூர்வ தளத்திலேயே "
            "சரிபார்க்கவும்.\n\n"

            "visible vision உங்கள் சார்பாக விண்ணப்பத்தை "
            "சமர்ப்பிக்காது அல்லது ஒப்புதல் கிடைத்ததாகக் கூறாது."
        )


    # PMUY
    if any(k in text for k in [
        "pmuy",
        "உஜ்வலா",
        "எரிவாயு",
        "சமையல்",
        "lpg",
        "gas",
        "scheme"
    ]):

        return (
            "🔥 PMUY - பிரதான் மந்திரி உஜ்வலா யோஜனா\n\n"

            "இது சமையல் எரிவாயு தொடர்பான அரசு திட்டமாகும்.\n\n"

            "தற்போதைய தகுதி, ஆவணங்கள் மற்றும் விண்ணப்ப "
            "வழிமுறைகளை அதிகாரப்பூர்வ PMUY இணையதளத்தில் "
            "சரிபார்க்கவும்.\n\n"

            + OFFICIAL_URL
        )


    # Education
    if any(k in text for k in [
        "கல்வி",
        "education",
        "student",
        "மாணவி",
        "மாணவர்"
    ]):

        return (
            "📚 கல்வி தொடர்பான அரசு திட்டங்களை அறிய:\n\n"

            "1. உங்கள் கல்வி நிலையைத் தெரிந்துகொள்ளுங்கள்.\n"
            "2. குடும்பம் மற்றும் வருமானம் தொடர்பான "
            "தகுதி விதிகளைச் சரிபார்க்கவும்.\n"
            "3. அதிகாரப்பூர்வ அரசு இணையதளத்தில் "
            "திட்ட விவரங்களைப் பார்க்கவும்.\n\n"

            "குறிப்பு: தற்போதைய தகுதி மற்றும் உதவித்தொகை "
            "விவரங்களை அதிகாரப்பூர்வ அரசு தளத்தில் சரிபார்க்கவும்."
        )


    # Health
    if any(k in text for k in [
        "சுகாதாரம்",
        "health",
        "hospital",
        "மருத்துவ"
    ]):

        return (
            "🏥 சுகாதாரம் தொடர்பான அரசு திட்டங்களைப் பற்றி "
            "அறிய, அதிகாரப்பூர்வ அரசு சுகாதார இணையதளங்களில் "
            "தற்போதைய தகுதி மற்றும் சேவைகளைச் சரிபார்க்கவும்.\n\n"

            "உங்கள் தனிப்பட்ட மருத்துவ தகவல்களை இங்கே பகிர வேண்டாம்."
        )


    # Housing
    if any(k in text for k in [
        "வீடு",
        "housing",
        "house"
    ]):

        return (
            "🏠 வீடு தொடர்பான அரசு திட்டங்களின் தகுதி "
            "மற்றும் விண்ணப்ப முறைகள் திட்டத்தைப் பொறுத்து மாறும்.\n\n"

            "அதிகாரப்பூர்வ அரசு தளத்தில் தற்போதைய தகவல்களை "
            "சரிபார்த்து விண்ணப்பிக்கவும்."
        )


    # Default response
    return (
        "வணக்கம்! 🌸 நான் visible vision.\n\n"

        "அரசுத் திட்டங்களை எளிய தமிழில் புரிந்துகொள்ள "
        "உங்களுக்கு வழிகாட்டுகிறேன்.\n\n"

        "நீங்கள் கேட்கலாம்:\n\n"

        "🔥 PMUY / LPG திட்டம் பற்றி சொல்லுங்கள்\n"
        "📚 கல்வி திட்டங்கள் பற்றி சொல்லுங்கள்\n"
        "🏥 சுகாதார திட்டங்கள் பற்றி சொல்லுங்கள்\n"
        "🏠 வீட்டு திட்டங்கள் பற்றி சொல்லுங்கள்\n"
        "✅ நான் தகுதியானவரா?\n"
        "📄 என்னென்ன ஆவணங்கள் தேவை?\n"
        "📝 எப்படி விண்ணப்பிப்பது?\n\n"

        "⚠️ Aadhaar எண், OTP, கடவுச்சொல் அல்லது "
        "வங்கி PIN-ஐ பகிர வேண்டாம்."
    )


class Handler(SimpleHTTPRequestHandler):

    def do_GET(self):

        path = urlparse(self.path).path

        if path == "/":
            self.path = "/template/index.html"

        return super().do_GET()


    def do_POST(self):

        path = urlparse(self.path).path

        if path != "/api/ask":

            self.send_error(404)

            return


        try:

            content_length = int(
                self.headers.get(
                    "Content-Length",
                    "0"
                )
            )

            body = self.rfile.read(
                content_length
            )

            data = json.loads(
                body.decode("utf-8")
            )

            message = str(
                data.get(
                    "message",
                    ""
                )
            ).strip()


            print(
                "User:",
                message
            )


            answer = tamil_answer(
                message
            )


            response = json.dumps(
                {
                    "answer": answer
                },
                ensure_ascii=False
            ).encode("utf-8")


            self.send_response(200)

            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )

            self.send_header(
                "Content-Length",
                str(len(response))
            )

            self.send_header(
                "Cache-Control",
                "no-cache"
            )

            self.end_headers()

            self.wfile.write(
                response
            )


            print("Answer sent successfully.")


        except Exception as error:

            print(
                "ERROR:",
                error
            )


            response = json.dumps(
                {
                    "answer":
                    "மன்னிக்கவும். தற்போது பதில் வழங்க முடியவில்லை."
                },
                ensure_ascii=False
            ).encode("utf-8")


            self.send_response(500)

            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )

            self.send_header(
                "Content-Length",
                str(len(response))
            )

            self.end_headers()

            self.wfile.write(
                response
            )


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    print("=" * 45)
    print("       VISIBLE VISION")
    print("=" * 45)

    print(f"Running on port: {port}")

    print(
        "Gemini:",
        "ON"
        if os.environ.get("GEMINI_API_KEY")
        else "OFF - Demo Mode"
    )

    print("Press Ctrl+C to stop.")

    print("=" * 45)

    server = ThreadingHTTPServer(
        ("0.0.0.0", port),
        Handler
    )

    server.serve_forever()