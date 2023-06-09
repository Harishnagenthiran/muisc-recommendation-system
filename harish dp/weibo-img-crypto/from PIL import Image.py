from PIL import Image
import numpy as np

# Encryption function
def encrypt_image(image_path, key):
    # Open the image
    image = Image.open("C:\Users\HARISH\Documents\sai Dp\download_1.jpg")
    
    # Convert the image to a numpy array
    img_array = np.array(image)
    
    # XOR the image array with the encryption key
    encrypted_array = np.bitwise_xor(img_array, key)
    
    # Convert the encrypted array back to an image
    encrypted_image = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_image.save("encrypted_image.png")

# Decryption function
def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    
    # Convert the encrypted image to a numpy array
    encrypted_array = np.array(encrypted_image)
    
    # XOR the encrypted array with the decryption key
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    
    # Convert the decrypted array back to an image
    decrypted_image = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_image.save("decrypted_image.png")

# Example usage
image_path = "original_image.png"
encrypted_image_path = "encrypted_image.png"
key = np.random.randint(0, 255, size=(512, 512, 3), dtype=np.uint8)

# Encrypt the image
encrypt_image(image_path, key)

# Decrypt the image
decrypt_image(encrypted_image_path, key)
