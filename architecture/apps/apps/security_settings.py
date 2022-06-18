SECRET_KEY = 'django-insecure-fejvtsc8@bu9qj0zh=9@9l#q2@$3t$s(gjj(9#2cm#w-c2xtpe'

DATABASES = { 
	'default': { 
    	'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'video_db',
        'USER': 'admin',
        'PASSWORD': 'admin123!',
        'HOST': 'database-1.cj3cphm2af5z.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
        }
    } 
}