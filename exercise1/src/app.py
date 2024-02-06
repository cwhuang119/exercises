"""Server for hosting index.html and provide API for the frontend."""

from flask import Flask, jsonify, request, send_from_directory


app = Flask(__name__, static_folder="static")

# Dummy data for U.S. states
states = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming",
]
# Host html.index
@app.route("/")
def index():
    """Serve the index.html file."""
    return send_from_directory("static", "index.html")

# API endpoint to retrieve states
@app.route("/states")
def get_states_api():
    """GET STATES API endpoint."""
    search_term = request.args.get("q", "").lower()
    filtered_states = [state for state in states if search_term in state.lower()]
    limited_results = filtered_states[:8]
    return jsonify(limited_results)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5001,debug=False)
