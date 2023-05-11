from flask import Flask, render_template, request, jsonify
from icebreaker import ice_break

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    summary_facts, interests, icebreakers, profile_pic_url = ice_break(name=name)

    return jsonify(
        {
            "summary_facts": summary_facts.to_dict(), 
            "topics_of_interest": interests.to_dict(), 
            "ice_breakers": icebreakers.to_dict(),
            "profile_pic_url": profile_pic_url
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

