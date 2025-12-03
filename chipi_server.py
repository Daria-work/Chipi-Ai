from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Data file path
DATA_FILE = 'training_data.json'

# Initialize training data
def load_training_data():
    """Load training data from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return get_default_training_data()

def save_training_data(data):
    """Save training data to JSON file"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_default_training_data():
    """Return default training data structure"""
    return {
        "greetings": {
            "patterns": ["hello", "hi", "hey", "greetings", "what's up", "how are you"],
            "responses": [
                "Hello. I am Chipi. I am happy to see you today. How can I help you?",
                "Hi there. It is great to see you here. What would you like to talk about?",
                "Hey. I am Chipi, your friendly AI assistant. How can I help you?"
            ]
        },
        "aboutMe": {
            "patterns": ["who are you", "what are you", "tell me about yourself"],
            "responses": [
                "I am Chipi, an AI chatbot created to help and chat with people.",
                "My name is Chipi and I am a fully self-contained AI assistant."
            ]
        },
        "help": {
            "patterns": ["can you help", "help me", "i need help"],
            "responses": [
                "Of course I can help you. Please tell me what you need.",
                "I would be very happy to help you with whatever you need."
            ]
        },
        "goodbye": {
            "patterns": ["bye", "goodbye", "see you", "farewell"],
            "responses": [
                "Goodbye. It was great chatting with you. Come back anytime.",
                "See you later. Thanks for the conversation. Have a wonderful day."
            ]
        }
    }

# Initialize data
training_data = load_training_data()

# Routes

@app.route('/api/data', methods=['GET'])
def get_training_data():
    """Get all training data"""
    return jsonify({
        'status': 'success',
        'data': training_data,
        'timestamp': datetime.now().isoformat(),
        'categories': list(training_data.keys()),
        'totalCategories': len(training_data)
    })

@app.route('/api/data/<category>', methods=['GET'])
def get_category(category):
    """Get a specific category"""
    if category in training_data:
        return jsonify({
            'status': 'success',
            'category': category,
            'data': training_data[category]
        })
    return jsonify({'status': 'error', 'message': f'Category {category} not found'}), 404

@app.route('/api/data/add-response/<category>', methods=['POST'])
def add_response(category):
    """Add a new response to a category"""
    if category not in training_data:
        return jsonify({'status': 'error', 'message': f'Category {category} not found'}), 404
    
    data = request.json
    response_text = data.get('response')
    
    if not response_text:
        return jsonify({'status': 'error', 'message': 'Response text is required'}), 400
    
    training_data[category]['responses'].append(response_text)
    save_training_data(training_data)
    
    return jsonify({
        'status': 'success',
        'message': f'Response added to {category}',
        'category': category,
        'totalResponses': len(training_data[category]['responses'])
    })

@app.route('/api/data/add-pattern/<category>', methods=['POST'])
def add_pattern(category):
    """Add a new pattern to a category"""
    if category not in training_data:
        return jsonify({'status': 'error', 'message': f'Category {category} not found'}), 404
    
    data = request.json
    pattern = data.get('pattern')
    
    if not pattern:
        return jsonify({'status': 'error', 'message': 'Pattern is required'}), 400
    
    if pattern not in training_data[category]['patterns']:
        training_data[category]['patterns'].append(pattern)
        save_training_data(training_data)
        return jsonify({
            'status': 'success',
            'message': f'Pattern added to {category}',
            'category': category,
            'totalPatterns': len(training_data[category]['patterns'])
        })
    
    return jsonify({'status': 'error', 'message': 'Pattern already exists'}), 400

@app.route('/api/data/create-category', methods=['POST'])
def create_category():
    """Create a new category"""
    data = request.json
    category_name = data.get('name')
    patterns = data.get('patterns', [])
    responses = data.get('responses', [])
    
    if not category_name:
        return jsonify({'status': 'error', 'message': 'Category name is required'}), 400
    
    if category_name in training_data:
        return jsonify({'status': 'error', 'message': 'Category already exists'}), 400
    
    training_data[category_name] = {
        'patterns': patterns,
        'responses': responses
    }
    save_training_data(training_data)
    
    return jsonify({
        'status': 'success',
        'message': f'Category {category_name} created',
        'category': category_name
    })

@app.route('/api/data/update-response/<category>/<int:index>', methods=['PUT'])
def update_response(category, index):
    """Update a specific response"""
    if category not in training_data:
        return jsonify({'status': 'error', 'message': f'Category {category} not found'}), 404
    
    if index >= len(training_data[category]['responses']):
        return jsonify({'status': 'error', 'message': 'Response index out of range'}), 404
    
    data = request.json
    new_response = data.get('response')
    
    if not new_response:
        return jsonify({'status': 'error', 'message': 'Response text is required'}), 400
    
    training_data[category]['responses'][index] = new_response
    save_training_data(training_data)
    
    return jsonify({
        'status': 'success',
        'message': f'Response updated in {category}',
        'category': category,
        'index': index
    })

@app.route('/api/data/delete-response/<category>/<int:index>', methods=['DELETE'])
def delete_response(category, index):
    """Delete a specific response"""
    if category not in training_data:
        return jsonify({'status': 'error', 'message': f'Category {category} not found'}), 404
    
    if index >= len(training_data[category]['responses']):
        return jsonify({'status': 'error', 'message': 'Response index out of range'}), 404
    
    deleted = training_data[category]['responses'].pop(index)
    save_training_data(training_data)
    
    return jsonify({
        'status': 'success',
        'message': 'Response deleted',
        'category': category,
        'deletedResponse': deleted
    })

@app.route('/api/data/delete-category/<category>', methods=['DELETE'])
def delete_category(category):
    """Delete an entire category"""
    if category not in training_data:
        return jsonify({'status': 'error', 'message': f'Category {category} not found'}), 404
    
    if category in ['greetings', 'help', 'goodbye']:
        return jsonify({'status': 'error', 'message': 'Cannot delete core categories'}), 400
    
    del training_data[category]
    save_training_data(training_data)
    
    return jsonify({
        'status': 'success',
        'message': f'Category {category} deleted'
    })

@app.route('/api/data/reset', methods=['POST'])
def reset_data():
    """Reset to default training data"""
    global training_data
    training_data = get_default_training_data()
    save_training_data(training_data)
    
    return jsonify({
        'status': 'success',
        'message': 'Training data reset to default'
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get statistics about the training data"""
    total_categories = len(training_data)
    total_patterns = sum(len(cat['patterns']) for cat in training_data.values())
    total_responses = sum(len(cat['responses']) for cat in training_data.values())
    
    return jsonify({
        'status': 'success',
        'totalCategories': total_categories,
        'totalPatterns': total_patterns,
        'totalResponses': total_responses,
        'categories': list(training_data.keys())
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Chipi AI Server',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    print("Starting Chipi AI Server...")
    print("Server running at http://localhost:5000")
    print("API Documentation available at http://localhost:5000/api/docs")
    app.run(debug=True, port=5000)
