from app import app
from flask_socketio import SocketIO, send, emit
from model import *
import json
from json import JSONDecoder

socketio = SocketIO(app)


@app.before_request
def before_request():
    initialize_db()


@socketio.on('message')
def handleMessage(msg):
    decoder = JSONDecoder()
    data = decoder.decode(msg)
    if 'text' in data and data['text']:
        Order.create(**data)
    send(msg, broadcast=True)


@socketio.on('delete_post')
def handleDelete(post_id):
    jsonData = json.loads(post_id)
    jsonId=jsonData['id']    
    id_del = Order.select().where(Order.id == jsonId)
    Order.delete().where(Order.id.in_(id_del)).execute()
    emit('delete',post_id, broadcast=True)

@socketio.on('sound')
def handleSound(sound_msg):
    emit('sound', sound_msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=8080)