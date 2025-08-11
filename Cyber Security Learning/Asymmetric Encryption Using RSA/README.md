 Lab: Asymmetric Encryption Using RSA (OpenSSL)
📁 Location
technical-assignments/Lab - Asymmetric Encryption Using RSA.docx

🧠 Overview
This lab demonstrates how to use the RSA algorithm for encrypting and decrypting data using OpenSSL in a Linux terminal environment. The exercises cover real-world use of public/private key pairs to protect sensitive information.

🧪 Exercise 1: Encrypt and Decrypt a Small Message
Goal: Encrypt and decrypt a plaintext message using a 2048-bit RSA key pair.

✅ Key Steps:
Generated RSA key pair using openssl genpkey and openssl rsa

Created a plaintext message (message.txt)

Encrypted the message using the public key

Decrypted the ciphertext using the private key

Verified the decrypted output matched the original message

🔐 Exercise 2: RSA File Encryption and Decryption
Goal: Use RSA keys to secure a file containing sensitive information.

✅ Key Steps:
Regenerated a new RSA key pair

Created plaintext.txt containing mock confidential content

Encrypted it into encrypted_data.bin with the public key

Decrypted it into decrypted_data.txt using the private key

Verified decrypted file contents match original input

📸 Artifacts
All terminal screenshots are included in the .docx file:

Public/private key generation

Encryption and decryption commands

Output verification

✅ Status
Complete — All commands executed and validated successfully.