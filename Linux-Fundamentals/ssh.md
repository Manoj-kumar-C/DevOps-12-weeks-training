# SSH Concepts – Complete Markdown Notes

## 1. SSH vs Telnet

| Feature | SSH (Secure Shell) | Telnet |
|---------|-------------------|--------|
| **Security** | ✅ Encrypted | ❌ Not encrypted |
| **Data Protection** | Protects passwords & data | Password sent as plain text |
| **Recommended** | ✔️ Yes | ❌ No |
| **Default Port** | 22 | 23 |
| **Authentication Methods** | Password, SSH keys | Only password |
| **Usage** | Servers, DevOps, cloud | Legacy or insecure systems |

### Simple Difference

- **Telnet** = old, unsafe, plain-text communication
- **SSH** = modern, encrypted, secure remote login

---

## 2. SSH Key Authentication

SSH keys allow **password-less** and **more secure** login.

### Two keys are generated:

- **Public key** (`id_rsa.pub`) → shared with server
- **Private key** (`id_rsa`) → kept secret on your device

### How it works:

1. You store your **public key** on the server.
2. When connecting, SSH **challenges** your machine.
3. Your **private key** answers the challenge.
4. If they match → **login successful**, no password needed.

### Benefits

✔️ More secure than password  
✔️ Cannot be brute-forced  
✔️ Used in DevOps, GitHub, cloud servers  
✔️ Fast & convenient

---

## 3. How to Create SSH Keys

### Step 1 — Generate a key pair

```bash
ssh-keygen
```

### Step 2 — Save the keys

Press Enter to accept:

```bash
~/.ssh/id_rsa
```

### Step 3 — Copy public key to remote server

```bash
ssh-copy-id user@server-ip
```

If `ssh-copy-id` is not available:

```bash
cat ~/.ssh/id_rsa.pub
```

Copy the content into:

```bash
~/.ssh/authorized_keys
```

### Step 4 — Login without password

```bash
ssh user@server-ip
```

---

## 4. How SSH Works Internally (Handshake & Encryption)

SSH creates a **secure, encrypted communication channel**.

### Internal Steps

#### Step 1 — TCP Connection

Client connects to server on **port 22**.

#### Step 2 — Server Authentication (Host Key)

Server sends its **host key** → client checks if it's trusted.

If first time:

```
Are you sure you want to continue connecting (yes/no)?
```

#### Step 3 — Key Exchange

SSH uses algorithms like:

- Diffie–Hellman
- ECDH
- Curve25519

This step:  
✔️ Creates shared secret  
✔️ Derives encryption keys  
✔️ Prevents eavesdropping

#### Step 4 — Encryption Starts

All data now encrypted with:

- AES
- ChaCha20
- Or other ciphers

**No one can read the communication**, even with packet sniffers.

#### Step 5 — User Authentication

Two options:

**(a) Password Auth**

Encrypted password sent through SSH.

**(b) Key-Based Auth (More secure)**

- Client signs challenge using its **private key**
- Server verifies using **public key**

#### Step 6 — Secure Shell Session Established

You now interact securely:

- Commands encrypted
- Outputs encrypted
- No one can intercept

---

## Summary

- **SSH is secure**; Telnet is not.
- **SSH keys** provide strong authentication.
- `ssh-keygen` generates key pair.
- **SSH handshake** involves:
  - Host key verification
  - Key exchange
  - Encryption setup
  - User authentication
- All communication is **encrypted end-to-end**.

---

**You can now copy this entire content and save it as a `.md` file!**