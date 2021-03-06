#!/usr/bin/env python
import pika
import sys
sys.path.append('../')
from model_smartphone import SmartphoneConsumer, SmartphoneProducer
import textwrap
import threading

smartphone_consumer = SmartphoneConsumer()

#start conection
def smartphone_start():
	global smartphone_consumer
	smartphone_consumer.button_is_pressed = True
	smartphone_consumer.start()
	
	
#stop conection
def smartphone_stop():
	global smartphone_consumer
	smartphone_consumer.button_is_pressed = False
	#smartphone_consumer.join()

def smartphone_confirm_notification():
	global smartphone_consumer
	smartphone_producer = None
	
	smartphone_consumer.is_notification = False
	smartphone_producer = SmartphoneProducer()
	smartphone_producer.start()
	smartphone_producer.join()

def smartphone_get_notification():
	global smartphone_consumer
	return smartphone_consumer.is_notification

def smartphone_get_message():
	global smartphone_consumer

	message = smartphone_consumer.message
	if '{' in message:
		return eval(message)

	message = message.replace("b'", "")
	message = message.replace('"', '')

	return message