from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("25857891"))
API_HASH = getenv("347a2b979ae1929d43ccf916c77cd8a0")

BOT_TOKEN = getenv("6966176008:AAFMgMGYmJ4QGSGOs7JvT9Y3ShhqOL9Ch20", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6422573030"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("BQGKj2MAKLGgsmem849k1nvpmDeoL-MzC_Q2bMJrL5_4FmOwFKl1E_jRuJt60B07hYz_fn-Dk6owQpJFKhrGu82u-HhOywVt7vRyyqPOdatFLzv3u4ZSVK76FaTCry31tr6gJC8jd9LJgxn_BnsH9e6IUjPgM_DSRz-jTpfRxcer6hmOUceawpyycOKFXc8lr7IhxDHQwOtxKUEM5TITIGfSobsZqHiowZi6cLaAY2lDylNJKVZuWspLna_zGTzj_SkoEsXB0CbFhizbokmnqjx4MVAofhDvKHq_8Y1bd1ePKSDcXFqD31jFPw2CPTlhf0HFby2sb3GxWQqKD1PewSgAAAAGOCMfkAA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tum_se_hii")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ALEXX_ZIP")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
