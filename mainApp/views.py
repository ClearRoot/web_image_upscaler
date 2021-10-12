from django.shortcuts import render

from PIL import Image
import tensorflow_hub as hub
import tensorflow as tf
import urllib.request
import base64
from io import BytesIO


def preprocess_image(image):
  """ Loads image from path and preprocesses to make it model ready
      Args:
        image_path: Path to the image file
  """
  hr_image = tf.image.decode_image(image)
  # If PNG, remove the alpha channel. The model only supports
  # images with 3 color channels.
  if hr_image.shape[-1] == 4:
    hr_image = hr_image[...,:-1]
  hr_size = (tf.convert_to_tensor(hr_image.shape[:-1]) // 4) * 4
  hr_image = tf.image.crop_to_bounding_box(hr_image, 0, 0, hr_size[0], hr_size[1])
  hr_image = tf.cast(hr_image, tf.float32)
  return tf.expand_dims(hr_image, 0)

def save_image(image):
  """
    Saves unscaled Tensor Images.
    Args:
      image: 3D image tensor. [height, width, channels]
      filename: Name of the file to save to.
  """
  if not isinstance(image, Image.Image):
    image = tf.clip_by_value(image, 0, 255)
    image = Image.fromarray(tf.cast(image, tf.uint8).numpy())

  return image


# Create your views here.
def hellow(request):
  model = hub.load("https://tfhub.dev/captain-pool/esrgan-tf2/1")
  img = urllib.request.urlopen("https://user-images.githubusercontent.com/12981474/40157448-eff91f06-5953-11e8-9a37-f6b5693fa03f.png").read()
  hr_image = preprocess_image(img)
  fake_image = model(hr_image)
  fake_image = save_image(tf.squeeze(fake_image))
  buffered = BytesIO()
  fake_image.save(buffered, format="JPEG")
  origin = base64.b64encode(img).decode('utf-8')
  fake = base64.b64encode(buffered.getvalue()).decode('utf-8')
  
  return render(request, 'mainApp/main.html', {'origin': origin, 'fake': fake})

# def upscaler(request):
#   model = hub.load("https://tfhub.dev/captain-pool/esrgan-tf2/1")
  

