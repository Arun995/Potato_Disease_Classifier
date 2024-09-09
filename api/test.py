import tensorflow as tf

# Load the .h5 model
model = tf.keras.models.load_model('D:/Data Science/Projects/potato-disease/saved_models/1.keras')

# Export the model in SavedModel format
model.export('D:/Data Science/Projects/potato-disease/saved_model/1')
