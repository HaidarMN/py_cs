import ftplib

def annonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login("anonymous")
        print("\n [+] " + str(hostname) + " FTP Anonymous Login Success")
        ftp.quit()
        return True
    except Exception:
        print("\n [-] " + str(hostname) + " FTP Anonymous Login Fails")
        return False

if __name__ == "__main__":
    annonLogin("90.130.70.73")

# NOT WORKING