# **🛡️ File Integrity Monitor (FIM) – Real-Time Change Detection System**

**COMPANY: CODETECH IT SOLUTIONS**

**NAME: GYANMOTAY VIKAS**

**INTERN ID: CT12RGV**

**DOMAIN: CYBER SECURITY & ETHICAL HACKING**

**DURATION: 8 WEEKS**

**MENTOR: NELLA SANTOSH**

# **🔍 Overview**
### In the ever-evolving landscape of cybersecurity, ensuring the integrity of files is non-negotiable. Cyber threats like malware injections, ransomware attacks, and unauthorized data tampering pose severe risks to businesses and individuals alike.

### The File Integrity Monitor (FIM) is a powerful, automated security tool designed to track and detect unauthorized changes in critical system files and directories. By leveraging cryptographic hashing and real-time monitoring, this tool ensures that organizations can prevent security breaches, maintain compliance (ISO 27001, PCI-DSS, HIPAA), and safeguard sensitive data.

### Whether you're a system administrator, ethical hacker, or security professional, this tool empowers you to detect file tampering before it becomes a major security incident.

# **🚀 Key Features**
### ✅ Automated File Integrity Checking – Instantly detects unauthorized modifications.
### ✅ Real-Time Change Detection – Alerts users of file modifications, deletions, and creations.
### ✅ Multi-Algorithm Support – Choose between SHA-256, SHA-512, and MD5 for hashing verification.
### ✅ Comprehensive Logging – Stores event details for forensics and compliance auditing.
### ✅ Lightweight & Efficient – Minimal system resource usage while providing high reliability.
### ✅ User-Friendly CLI – Easy-to-use interface for seamless interaction.

# **🛠️ How It Works?**
## 🔹 Step 1: Input Directory Path
### Users specify the directory to monitor.

## 🔹 Step 2: Baseline Hash Computation
### The system generates cryptographic hashes for all existing files.

## 🔹 Step 3: Real-Time Monitoring with Watchdog
### The Watchdog library continuously tracks file events:
### ✔ New file creation ✅
### ✔ File modifications ✏️
### ✔ File deletions ❌

## 🔹 Step 4: Hash Comparison & Alerting
### Whenever a change is detected, the system recalculates the file’s hash and compares it to the original. If mismatched, an alert is triggered and logged.

## 🔹 Step 5: Logging & Report Generation
### All detected changes are stored in file_integrity.log, including timestamps, file paths, and event details.

# **🌍 Why This Project is Important?**
### 🔒 Cybersecurity Threats: Data breaches due to unauthorized file modifications cost companies billions. Preventing tampering is critical.

### ⚡ Regulatory Compliance: Security frameworks like ISO 27001, HIPAA, PCI-DSS, and NIST require organizations to monitor file integrity.

### 🔍 Incident Response & Forensics: Provides a detailed log of changes, helping security teams investigate breaches efficiently.

### 🔧 Secure System Administration: Ensures that critical system files remain unchanged, preventing cyberattacks.

# **📊 Example Output**
### bash
### Copy
### Edit
### [+] Monitoring started on /var/www/html/
### [*] Detected file modification: config.php (SHA-256 mismatch)
### [*] File Deleted: sensitive_data.txt
### [*] New File Created: user_backup.json
### [+] Event log updated: file_integrity.log

# **📌 Ethical Considerations & Disclaimer**
### ⚠ This tool is for legal and ethical use only.
### ✔ Always obtain explicit permission before monitoring system files.
### 🚨 Unauthorized monitoring is illegal and may result in legal consequences.

# **🚀 Future Enhancements**
### 🔹 Email & SMS Alerts – Immediate notifications to system admins.
### 🔹 GUI Dashboard – A visual interface for better usability.
### 🔹 AI-Powered Anomaly Detection – Machine learning models to predict abnormal file behavior.
### 🔹 Cloud Monitoring Support – Monitor files stored in cloud environments (AWS, GCP, Azure).

# **✅ Conclusion**
### Cybersecurity isn’t a luxury—it’s a necessity! The File Integrity Monitor (FIM) offers a powerful, automated solution for protecting critical files against unauthorized modifications and cyber threats.

### By integrating real-time change detection, cryptographic hashing, and event logging, this tool helps developers, ethical hackers, and security professionals stay ahead of threats and secure their digital environments.

## 🔒 Protect your files before attackers compromise them! 🔥

## 💡 Want to monitor your files? Run the FIM & stay secure! 🚀

# **🛠️ Technologies Used**
### 🔹 Python (Core programming)
### 🔹 Watchdog (Real-time file monitoring)
### 🔹 Hashlib (Cryptographic hashing – SHA-256, MD5, SHA-512)
### 🔹 Logging (Event tracking & reporting)
